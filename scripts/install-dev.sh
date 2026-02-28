#!/usr/bin/env bash
# Skilless Developer Installer
# Copies from local repo to install directory for development

set -e

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.."
REPO_DIR="$SCRIPT_DIR"

INSTALL_DIR="$HOME/.agents/skills/skilless.ai"

echo "Installing Skilless from local repo to $INSTALL_DIR..."

# Remove existing installation if it exists
rm -rf "$INSTALL_DIR"

# Create directories for skilless
mkdir -p "$INSTALL_DIR/scripts"

# Detect uv, install if not found
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi

# Detect network (check if pypi.org is accessible)
if curl -sI https://pypi.org &>/dev/null; then
    UV_INDEX_URL="https://pypi.org/simple"
else
    echo "Detected China network, using mirror..."
    UV_INDEX_URL="https://pypi.tuna.tsinghua.edu.cn/simple"
fi

# Create venv with Python 3.12+
echo "Creating virtual environment..."
uv venv "$INSTALL_DIR/.venv" --python ">=3.12"

# Sync dependencies using uv (installs from pyproject.toml)
echo "Installing dependencies..."
uv pip install --python "$INSTALL_DIR/.venv/bin/python" -e "$REPO_DIR" --index-url "$UV_INDEX_URL"

# Copy skill files (each skill gets its own directory alongside skilless)
echo "Copying skills..."
SKILLS_DIR="$HOME/.agents/skills"

# Install skilless meta skill
cp "$REPO_DIR/src/skilless/SKILL.md" "$INSTALL_DIR/SKILL.md"
cp "$REPO_DIR/src/skilless/VERSION" "$INSTALL_DIR/VERSION"

# Install sub-skills (src/skilless.ai-brainstorming -> skilless.ai-brainstorming)
for skill in skilless.ai-brainstorming skilless.ai-research skilless.ai-writing; do
    mkdir -p "$SKILLS_DIR/$skill"
    cp "$REPO_DIR/src/$skill/SKILL.md" "$SKILLS_DIR/$skill/SKILL.md"
done

# Create CLI wrapper
cat > "$INSTALL_DIR/skilless.ai" << 'EOF'
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
export PYTHONPATH="$SCRIPT_DIR/scripts:$PYTHONPATH"
exec "$SCRIPT_DIR/.venv/bin/python" "$SCRIPT_DIR/scripts/cli.py" "$@"
EOF
chmod +x "$INSTALL_DIR/skilless.ai"

# Copy scripts
echo "Copying CLI..."
cp "$REPO_DIR/src/skilless/scripts/"*.py "$INSTALL_DIR/scripts/"
chmod +x "$INSTALL_DIR/scripts/"*.py

# Create config
cat > "$INSTALL_DIR/config.yaml" << EOF
version: "1.0"
repo: "$REPO_DIR"
skills:
  - skilless.ai-brainstorming
  - skilless.ai-research
  - skilless.ai-writing
EOF

echo ""
echo "✓ Skilless installed successfully!"
echo ""

# Run doctor check
echo "Running diagnostics..."
echo ""
"$INSTALL_DIR/skilless.ai" doctor

echo ""
echo "Usage:"
echo "  $INSTALL_DIR/skilless.ai doctor"
echo "  $INSTALL_DIR/skilless.ai explain skilless.ai-brainstorming"
echo "  $INSTALL_DIR/skilless.ai search <query>"

