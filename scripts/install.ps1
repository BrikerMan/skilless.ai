# Skilless Installer for Windows
# Usage: irm https://skilless.ai/install.ps1 | iex
# Dev:   & ([scriptblock]::Create((irm https://skilless.ai/install.ps1))) -Dev
# China: & ([scriptblock]::Create((irm https://skilless.ai/install.ps1))) -China

param(
  [switch]$Dev,
  [switch]$China
)

$ErrorActionPreference = "Stop"

$Repo = "brikerman/skilless.ai"
$SkillsDir = "$env:USERPROFILE\.agents\skills"
$InstallDir = "$SkillsDir\skilless"
$GithubApi = "https://api.github.com/repos/$Repo/releases/latest"
$GithubRelease = "https://github.com/$Repo/releases/latest/download"

# ---- Header ----
Write-Host ""
Write-Host "  ✨ Skilless Installer" -ForegroundColor Cyan
Write-Host "  ─────────────────────"
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
        $LatestVersion = $Release.tag_name -replace '^v', ''
    } catch {
        Write-Host "  ✗ Failed to fetch latest version from GitHub" -ForegroundColor Red
        exit 1
    }

    Write-Host "  Latest : v$LatestVersion"
    Write-Host ""

    if ($CurrentVersion -and $CurrentVersion -eq $LatestVersion) {
        Write-Host "  ✓ Already up to date (v$CurrentVersion)" -ForegroundColor Green
        Write-Host ""
        exit 0
    }

    $AssetName = "skilless-windows-$Arch.zip"
    $DownloadUrl = "$GithubRelease/$AssetName"
}

# ---- Download ----
Write-Host "  ↓ Downloading..."
$WorkDir = New-TemporaryFile | ForEach-Object { Remove-Item $_; New-Item -ItemType Directory -Path $_ }
$ZipPath = Join-Path $WorkDir $AssetName

try {
    Invoke-WebRequest -Uri $DownloadUrl -OutFile $ZipPath -UseBasicParsing
} catch {
    Write-Host "  ✗ Failed to download: $DownloadUrl" -ForegroundColor Red
    Write-Host "  See https://github.com/$Repo/releases for available releases."
    Remove-Item -Recurse -Force $WorkDir -ErrorAction SilentlyContinue
    exit 1
}
Write-Host "  ✓ Downloaded"

# ---- Extract to skilless-repo ----
Write-Host "  ↓ Extracting..."
$RepoDir = Join-Path $WorkDir "skilless-repo"
New-Item -ItemType Directory -Path $RepoDir -Force | Out-Null
Expand-Archive -Path $ZipPath -DestinationPath $RepoDir -Force

# GitHub archive ZIPs have an inner dir (e.g. skilless.ai-main/); release ZIPs do not
if ($Dev) {
    $SrcDir = (Get-ChildItem -Path $RepoDir -Directory | Select-Object -First 1).FullName
} else {
    $SrcDir = $RepoDir
}
Write-Host "  ✓ Extracted"

# ---- Copy src/* -> ~/.agents/skills/ ----
Write-Host "  ↓ Installing files..."
New-Item -ItemType Directory -Path $SkillsDir -Force | Out-Null
$SrcPath = Join-Path $SrcDir "src"
Get-ChildItem -Path $SrcPath | ForEach-Object {
    $Dest = Join-Path $SkillsDir $_.Name
    if (Test-Path $Dest) { Remove-Item -Recurse -Force $Dest }
    Copy-Item -Path $_.FullName -Destination $Dest -Recurse -Force
}

# Cleanup work dir
Remove-Item -Recurse -Force $WorkDir -ErrorAction SilentlyContinue
Write-Host "  ✓ Files installed"

# ---- Check / install uv ----
if (Get-Command uv -ErrorAction SilentlyContinue) {
    $UvVer = uv --version
    Write-Host "  ✓ uv found: $UvVer"
} else {
    Write-Host "  ↓ Installing uv (Python package manager)..."
    irm https://astral.sh/uv/install.ps1 | iex
    $env:PATH = "$env:USERPROFILE\.local\bin;$env:PATH"
    $UvVer = uv --version
    Write-Host "  ✓ uv installed: $UvVer"
}

# ---- Mirror selection ----
$UvIndexUrl = "https://pypi.org/simple"
if ($China) {
    $UvIndexUrl = "https://pypi.tuna.tsinghua.edu.cn/simple"
    Write-Host "  → Using China mirror (Tsinghua)"
} else {
    try {
        $null = Invoke-WebRequest -Uri "https://pypi.org" -Method Head -TimeoutSec 3 -UseBasicParsing
    } catch {
        Write-Host "  → China network detected, switching to Tsinghua mirror"
        $UvIndexUrl = "https://pypi.tuna.tsinghua.edu.cn/simple"
    }
}

# ---- Virtual environment ----
Write-Host "  ↓ Setting up virtual environment..."
uv venv "$InstallDir\.venv" --python ">=3.12" --quiet 2>$null
$PythonExe = "$InstallDir\.venv\Scripts\python.exe"
$PyVer = & $PythonExe --version 2>&1
Write-Host "  ✓ Virtual environment ready ($PyVer)"

# ---- Install dependencies ----
Write-Host "  ↓ Installing dependencies..."
uv pip install --python $PythonExe $InstallDir --index-url $UvIndexUrl --quiet 2>$null
Write-Host "  ✓ Dependencies installed"

# ---- Done ----
$NewVersion = if (Test-Path "$InstallDir\VERSION") { (Get-Content "$InstallDir\VERSION") -replace '^\s+|\s+$', '' } else { "unknown" }
if ($Dev) { $NewVersion = "$NewVersion-dev" }

Write-Host ""
Write-Host "  ✓ Skilless v$NewVersion installed!" -ForegroundColor Green
Write-Host ""
Write-Host "  Usage:"
Write-Host "    $InstallDir\skilless doctor"
Write-Host "    $InstallDir\skilless search <query>"
Write-Host ""
