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
$InstallDir = "$env:USERPROFILE\.agents\skills\skilless"
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
$TempDir = New-TemporaryFile | ForEach-Object { Remove-Item $_; New-Item -ItemType Directory -Path $_ }
$ZipPath = Join-Path $TempDir $AssetName

try {
    Invoke-WebRequest -Uri $DownloadUrl -OutFile $ZipPath -UseBasicParsing
} catch {
    Write-Host "  ✗ Failed to download: $DownloadUrl" -ForegroundColor Red
    Write-Host "  See https://github.com/$Repo/releases for available releases."
    exit 1
}
Write-Host "  ✓ Downloaded"

# ---- Extract ----
Write-Host "  ↓ Extracting..."
if (Test-Path $InstallDir) {
    Remove-Item -Recurse -Force $InstallDir
}
New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null

$ExtractTemp = New-TemporaryFile | ForEach-Object { Remove-Item $_; New-Item -ItemType Directory -Path $_ }
Expand-Archive -Path $ZipPath -DestinationPath $ExtractTemp -Force

if ($Dev) {
    $InnerDir = Get-ChildItem -Path $ExtractTemp -Directory | Select-Object -First 1
    Copy-Item -Path "$($InnerDir.FullName)\*" -Destination $InstallDir -Recurse -Force
    Copy-Item -Path "$($InnerDir.FullName)\.*" -Destination $InstallDir -Recurse -Force -ErrorAction SilentlyContinue
} else {
    Copy-Item -Path "$ExtractTemp\*" -Destination $InstallDir -Recurse -Force
}
Remove-Item -Recurse -Force $ExtractTemp -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force $TempDir -ErrorAction SilentlyContinue

Write-Host "  ✓ Extracted to $InstallDir"

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
$PyVer = & "$InstallDir\.venv\Scripts\python.exe" --version 2>&1
Write-Host "  ✓ Virtual environment ready ($PyVer)"

# ---- Install dependencies ----
Write-Host "  ↓ Installing dependencies..."
$PythonExe = "$InstallDir\.venv\Scripts\python.exe"

if (Test-Path "$InstallDir\pyproject.toml") {
    uv pip install --python $PythonExe -e $InstallDir --index-url $UvIndexUrl --quiet 2>$null
} else {
    uv pip install --python $PythonExe `
        "fastmcp>=2.0.0" "httpx>=0.27.0" "feedparser>=6.0.0" `
        "yt-dlp>=2024.0.0" "pyyaml>=6.0.0" "rich>=13.0.0" `
        --index-url $UvIndexUrl `
        --quiet 2>$null
}
Write-Host "  ✓ Dependencies installed"

# ---- Install skill files ----
$SkillsDir = "$env:USERPROFILE\.agents\skills"
$SkillSearchPaths = if ($Dev) { @((Join-Path $InstallDir "src")) } else { @($InstallDir) }
foreach ($BasePath in $SkillSearchPaths) {
    if (Test-Path $BasePath) {
        Get-ChildItem -Path $BasePath -Directory -Filter "skilless.ai-*" | ForEach-Object {
            $SkillDest = Join-Path $SkillsDir $_.Name
            New-Item -ItemType Directory -Path $SkillDest -Force | Out-Null
            Copy-Item "$($_.FullName)\SKILL.md" "$SkillDest\SKILL.md" -ErrorAction SilentlyContinue
        }
    }
}

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
