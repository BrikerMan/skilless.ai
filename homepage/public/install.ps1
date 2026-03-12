# Skilless Installer for Windows
# Usage: irm https://skilless.ai/install.ps1 | iex
# Dev:   & ([scriptblock]::Create((irm https://skilless.ai/install.ps1))) -Dev
# China: & ([scriptblock]::Create((irm https://skilless.ai/install.ps1))) -China

param(
  [switch]$Dev,
  [switch]$China
)

function Invoke-SkillessInstall {
  param(
    [switch]$Dev,
    [switch]$China
  )

  $ErrorActionPreference = "Stop"

# ---- Fix console encoding for Unicode/Emoji output on Windows ----
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001 | Out-Null

# ---- Detect whether terminal font supports Unicode box/emoji chars ----
# Windows Terminal / WT supports Unicode; legacy conhost (cmd/old PS) often does not.
$UseUnicode = $false
if ($env:WT_SESSION -or $env:TERM_PROGRAM -eq "vscode" -or $env:ConEmuPID) {
    $UseUnicode = $true
}

function icon_ok    { if ($UseUnicode) { return "  [+]" } else { return "  [+]" } }
function icon_err   { if ($UseUnicode) { return "  [x]" } else { return "  [x]" } }
function icon_down  { if ($UseUnicode) { return "  [~]" } else { return "  [~]" } }
function icon_star  { if ($UseUnicode) { return "  [*]" } else { return "  [*]" } }
function icon_arrow { if ($UseUnicode) { return "   ->" } else { return "   ->" } }
function separator  { if ($UseUnicode) { return "  ---------------------" } else { return "  ---------------------" } }

$Repo = "brikerman/skilless.ai"
$SkillsDir = "$env:USERPROFILE\.agents\skills"
$InstallDir = "$SkillsDir\skilless"
$GithubApi = "https://api.github.com/repos/$Repo/releases/latest"
$GithubRelease = "https://github.com/$Repo/releases/latest/download"

# ---- Header ----
Write-Host ""
Write-Host "$(icon_star) Skilless Installer" -ForegroundColor Cyan
Write-Host "$(separator)"
Write-Host ""

# ---- System info ----
$Arch = if ([System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture -eq [System.Runtime.InteropServices.Architecture]::Arm64) {
    "aarch64"
} else {
    "x86_64"
}
Write-Host "  System : windows/$Arch"

# ---- Local version ----
$CurrentVersion = ""
$VersionFile = Join-Path $InstallDir "VERSION"
if (Test-Path $VersionFile) {
    $CurrentVersion = (Get-Content $VersionFile -ErrorAction SilentlyContinue) -replace '^\s+|\s+$', ''
    Write-Host "  Local  : v$CurrentVersion"
} else {
    Write-Host "  Local  : not installed"
}

# ---- Determine download source ----
if ($Dev) {
    $AssetName = "main.zip"
    $DownloadUrl = "https://github.com/$Repo/archive/refs/heads/main.zip"
    $LatestVersion = "dev"
    Write-Host "  Mode   : dev (main branch)"
    Write-Host ""
} else {
    Write-Host "  Checking latest release..."
    try {
        $Release = Invoke-RestMethod -Uri $GithubApi -UseBasicParsing
        $LatestVersion = $Release.tag_name -replace '^release/v?', ''
    } catch {
        Write-Host "$(icon_err) Failed to fetch latest version from GitHub" -ForegroundColor Red
        return
    }

    Write-Host "  Latest : v$LatestVersion"
    Write-Host ""

    if ($CurrentVersion -and $CurrentVersion -eq $LatestVersion) {
        Write-Host "$(icon_ok) Already up to date (v$CurrentVersion)" -ForegroundColor Green
        Write-Host ""
        Write-Host "  Usage:"
        Write-Host "    cd $InstallDir; uv run scripts/cli.py doctor"
        Write-Host "    cd $InstallDir; uv run scripts/cli.py search <query>"
        Write-Host ""
        return
    }

    $AssetName = "skilless.zip"
    $DownloadUrl = "$GithubRelease/$AssetName"
}

# ---- Download ----
Write-Host "$(icon_down) Downloading..."
$WorkDir = New-TemporaryFile | ForEach-Object { Remove-Item $_; New-Item -ItemType Directory -Path $_ }
$ZipPath = Join-Path $WorkDir $AssetName

try {
    Invoke-WebRequest -Uri $DownloadUrl -OutFile $ZipPath -UseBasicParsing
} catch {
    Write-Host "$(icon_err) Failed to download: $DownloadUrl" -ForegroundColor Red
    Write-Host "  See https://github.com/$Repo/releases for available releases."
    Remove-Item -Recurse -Force $WorkDir -ErrorAction SilentlyContinue
    return
}
Write-Host "$(icon_ok) Downloaded"

# ---- Extract to skilless-repo ----
Write-Host "$(icon_down) Extracting..."
$RepoDir = Join-Path $WorkDir "skilless-repo"
New-Item -ItemType Directory -Path $RepoDir -Force | Out-Null
Expand-Archive -Path $ZipPath -DestinationPath $RepoDir -Force

# GitHub archive ZIPs have an inner dir (e.g. skilless.ai-main/); release ZIPs do not
if ($Dev) {
    $SrcDir = (Get-ChildItem -Path $RepoDir -Directory | Select-Object -First 1).FullName
} else {
    $SrcDir = $RepoDir
}
Write-Host "$(icon_ok) Extracted"

# ---- Copy src/* -> ~/.agents/skills/ ----
Write-Host "$(icon_down) Installing files..."
New-Item -ItemType Directory -Path $SkillsDir -Force | Out-Null
$SrcPath = Join-Path $SrcDir "src"
Get-ChildItem -Path $SrcPath | ForEach-Object {
    $Dest = Join-Path $SkillsDir $_.Name
    if (Test-Path $Dest) { Remove-Item -Recurse -Force $Dest }
    Copy-Item -Path $_.FullName -Destination $Dest -Recurse -Force
}
# Copy README files to skilless/
Get-ChildItem -Path $SrcDir -Filter "README*.md" | ForEach-Object {
    Copy-Item -Path $_.FullName -Destination $InstallDir -Force
}

# Cleanup work dir
Remove-Item -Recurse -Force $WorkDir -ErrorAction SilentlyContinue
Write-Host "$(icon_ok) Files installed"

# ---- Link skills to ~/.claude/skills/ ----
$ClaudeDir = "$env:USERPROFILE\.claude"
if ((Get-Command claude -ErrorAction SilentlyContinue) -or (Test-Path $ClaudeDir)) {
    Write-Host "$(icon_down) Linking skills to Claude (~\.claude\skills\)..."
    $ClaudeSkillsDir = "$ClaudeDir\skills"
    foreach ($skill in @("skilless.ai-brainstorming", "skilless.ai-research", "skilless.ai-writing")) {
        $Src = "$SkillsDir\$skill\SKILL.md"
        $DstDir = "$ClaudeSkillsDir\$skill"
        if (Test-Path $Src) {
            New-Item -ItemType Directory -Path $DstDir -Force | Out-Null
            $DstLink = "$DstDir\SKILL.md"
            if (Test-Path $DstLink) { Remove-Item -Force $DstLink }
            New-Item -ItemType SymbolicLink -Path $DstLink -Target $Src | Out-Null
            Write-Host "$(icon_ok) Linked $skill"
        }
    }
}

Write-Host ""
Write-Host "$(icon_down) Installing dependencies & running diagnostics..."

# ---- Check / install uv ----
if (Get-Command uv -ErrorAction SilentlyContinue) {
    $UvVer = uv --version
    Write-Host "$(icon_ok) uv found: $UvVer"
} else {
    Write-Host "$(icon_down) Installing uv (Python package manager)..."
    irm https://astral.sh/uv/install.ps1 | iex
    $env:PATH = "$env:USERPROFILE\.local\bin;$env:PATH"
    $UvVer = uv --version
    Write-Host "$(icon_ok) uv installed: $UvVer"
}

# ---- Mirror selection ----
$UvIndexUrl = "https://pypi.org/simple"
if ($China) {
    $UvIndexUrl = "https://pypi.tuna.tsinghua.edu.cn/simple"
    Write-Host "$(icon_arrow) Using China mirror (Tsinghua)"
} else {
    try {
        $null = Invoke-WebRequest -Uri "https://pypi.org" -Method Head -TimeoutSec 3 -UseBasicParsing
    } catch {
        Write-Host "$(icon_arrow) China network detected, switching to Tsinghua mirror"
        $UvIndexUrl = "https://pypi.tuna.tsinghua.edu.cn/simple"
    }
}

# ---- Virtual environment ----
Write-Host "$(icon_down) Setting up virtual environment..."
uv venv "$InstallDir\.venv" --python "3.13" --quiet 2>$null
$PythonExe = "$InstallDir\.venv\Scripts\python.exe"
$PyVer = & $PythonExe --version 2>&1
Write-Host "$(icon_ok) Virtual environment ready ($PyVer)"

# ---- Install dependencies ----
Write-Host "$(icon_down) Installing dependencies..."
uv pip install --python $PythonExe $InstallDir --index-url $UvIndexUrl --quiet 2>$null
Write-Host "$(icon_ok) Dependencies installed"

# ---- Diagnostics ----
Write-Host "$(icon_down) Running diagnostics..."
Write-Host ""
Push-Location $InstallDir
uv run scripts/cli.py doctor
Pop-Location

# ---- Done ----
$NewVersion = if (Test-Path "$InstallDir\VERSION") { (Get-Content "$InstallDir\VERSION") -replace '^\s+|\s+$', '' } else { "unknown" }
if ($Dev) { $NewVersion = "$NewVersion-dev" }

Write-Host ""
Write-Host "$(icon_ok) Skilless v$NewVersion installed!" -ForegroundColor Green
Write-Host ""
Write-Host "  Usage:"
Write-Host "    cd $InstallDir; uv run scripts/cli.py doctor"
Write-Host "    cd $InstallDir; uv run scripts/cli.py search <query>"
Write-Host ""
Write-Host "  Please restart VS Code / OpenCode / Copilot or reload your Agent to enable the skills."
Write-Host ""
}

Invoke-SkillessInstall @PSBoundParameters