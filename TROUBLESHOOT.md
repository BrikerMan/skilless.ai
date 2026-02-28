# Troubleshooting Guide / 排障指南

## uv Installation Failure / uv 安装失败

**Symptom**: `curl` command hangs or fails during uv download.

**Solution**:
```bash
# Install uv manually
curl -LsSf https://astral.sh/uv/install.sh | sh
# Then re-run the Skilless installer
curl -LsSf https://skilless.ai/install | bash
```

---

## Network Issues (China) / 网络问题（中国大陆）

**Symptom**: Downloads are extremely slow or time out.

The installer automatically detects if `pypi.org` is unreachable and switches to the Tsinghua TUNA mirror. If this auto-detection fails:

```bash
# Set mirror manually before installing
export UV_INDEX_URL="https://pypi.tuna.tsinghua.edu.cn/simple"
curl -LsSf https://skilless.ai/install | bash
```

---

## Permission Errors / 权限错误

**Symptom**: `Permission denied` during installation.

**Solution**:
```bash
# Ensure ~/.local/bin is writable
mkdir -p ~/.local/bin
chmod 755 ~/.local/bin

# Ensure ~/.agents is writable
mkdir -p ~/.agents/skills
chmod -R 755 ~/.agents
```

> **Note**: Skilless does NOT require `sudo`. If you're being asked for sudo, something is wrong with your directory permissions.

---

## yt-dlp / ffmpeg Issues / 视频工具问题

**Symptom**: `skilless.ai ytd` fails with ffmpeg-related errors.

**Solution**:
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows (via winget)
winget install ffmpeg
```

yt-dlp is installed automatically, but ffmpeg must be available on your system PATH for video processing.

---

## Python Version Issues / Python 版本问题

**Symptom**: `No interpreter found for Python >=3.12`

Skilless requires Python 3.12+. The installer uses `uv` to manage Python, but if it can't find a suitable version:

```bash
# Install Python 3.12+ via uv
uv python install 3.12

# Then re-run installer
curl -LsSf https://skilless.ai/install | bash
```

---

## Verify Installation / 验证安装

Run the built-in health check:

```bash
skilless.ai doctor
```

This will verify:
- ✅ uv is installed and accessible
- ✅ Virtual environment exists
- ✅ All Python dependencies are installed
- ✅ CLI tools (search, web, ytd, rss) are functional
- ✅ ffmpeg is available (optional, for video processing)

---

## Uninstall / 卸载

To completely remove Skilless:

```bash
rm -rf ~/.agents/skills/skilless.ai
rm -rf ~/.agents/skills/skilless.ai-brainstorming
rm -rf ~/.agents/skills/skilless.ai-research
rm -rf ~/.agents/skills/skilless.ai-writing
```

---

## Still Need Help? / 还需要帮助？

- Open an issue: https://github.com/brikerman/skilless.ai/issues
- Check existing issues for similar problems
- Include the output of `skilless.ai doctor` in your report
