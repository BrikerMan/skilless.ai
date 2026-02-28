# Skilless Installer for Windows
# Downloads latest release from GitHub and sets up isolated environment
# Usage: irm https://skilless.ai/install.ps1 | iex
# Dev:   & ([scriptblock]::Create((irm https://skilless.ai/install.ps1))) -Dev
# China: & ([scriptblock]::Create((irm https://skilless.ai/install.ps1))) -China

param(
  [switch]$Dev,
  [switch]$China
)

$ErrorActionPreference = "Stop"

$Repo = "brikerman/skilless.ai"
$InstallDir = "$env:USERPROFILE\.agents\skills\skilless.ai"
$GithubRelease = "https://github.com/$Repo/releases/latest/download"

Write-Host ""
Write-Host "  ✨ skilless.ai installer" -ForegroundColor Cyan
Write-Host "  ─────────────────────────"
Write-Host ""

# ---- Detect architecture ----
$Arch = if ([System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture -eq [System.Runtime.InteropServices.Architecture]::Arm64) {
    "aarch64"
} else {
    "x86_64"
}

if ($Dev) {
    $AssetName = "main.zip"
    $DownloadUrl = "https://github.com/$Repo/archive/refs/heads/main.zip"
    Write-Host "  Platform: windows/$Arch (dev)"
} else {
    $AssetName = "skilless-windows-$Arch.zip"
    $DownloadUrl = "$GithubRelease/$AssetName"
    Write-Host "  Platform: windows/$Arch"
}

# ---- Check existing installation ----
if (Test-Path "$InstallDir\VERSION") {
    $CurrentVersion = Get-Content "$InstallDir\VERSION" -ErrorAction SilentlyContinue
    Write-Host "  Existing: v$CurrentVersion"
    Write-Host "  Upgrading to latest..."
} else {
    Write-Host "  Fresh install"
}
Write-Host ""

# ---- Download ----
Write-Host "  ↓ Downloading from GitHub Releases..."

$TempDir = New-TemporaryFile | ForEach-Object { Remove-Item $_; New-Item -ItemType Directory -Path $_ }
$ZipPath = Join-Path $TempDir $AssetName

try {
    Invoke-WebRequest -Uri $DownloadUrl -OutFile $ZipPath -UseBasicParsing
} catch {
    Write-Host "  ✗ Failed to download: $DownloadUrl" -ForegroundColor Red
    Write-Host "  Check https://github.com/$Repo/releases for available releases."
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

Write-Host "  ✓ Extracted to $InstallDir"

# ---- Install uv if needed ----
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "  ↓ Installing uv (Python package manager)..."
    irm https://astral.sh/uv/install.ps1 | iex
    $env:PATH = "$env:USERPROFILE\.local\bin;$env:PATH"
    Write-Host "  ✓ uv installed"
}

# ---- Create virtual environment ----
Write-Host "  ↓ Setting up virtual environment..."
uv venv "$InstallDir\.venv" --python ">=3.12" --quiet 2>$null

# ---- Install dependencies ----
Write-Host "  ↓ Installing dependencies..."

$PythonExe = "$InstallDir\.venv\Scripts\python.exe"
$UvIndexUrl = "https://pypi.org/simple"
if ($China) {
    $UvIndexUrl = "https://pypi.tuna.tsinghua.edu.cn/simple"
    Write-Host "  → Using China mirror (Tsinghua)"
}

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
$NewVersion = if (Test-Path "$InstallDir\VERSION") { Get-Content "$InstallDir\VERSION" } else { "unknown" }
if ($Dev) { $NewVersion = "$NewVersion-dev" }

Write-Host ""
Write-Host "  ✓ skilless.ai v$NewVersion installed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "  Usage:"
Write-Host "    $InstallDir\skilless.ai doctor"
Write-Host "    $InstallDir\skilless.ai search <query>"
Write-Host ""

# Cleanup
Remove-Item -Recurse -Force $TempDir -ErrorAction SilentlyContinue
