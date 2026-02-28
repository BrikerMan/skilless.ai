#!/usr/bin/env python3
"""FFmpeg tool - Convert and compress media files."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

try:
    from skilless.scripts.base import BaseTool, DoctorResult
except ImportError:
    from base import BaseTool, DoctorResult


class FFmpegTool(BaseTool):
    name = "media"
    description = "Convert and compress video/audio files"
    usage = "uv run scripts/ffmpeg.py <input> <output> [options]"
    how = "Uses FFmpeg to convert between formats (mp4, mkv, mp3, aac, wav) or compress files"

    def doctor(self) -> DoctorResult:
        try:
            # Try static_ffmpeg first, then system ffmpeg
            try:
                import static_ffmpeg
                static_ffmpeg.add_paths()
            except ImportError:
                pass

            result = subprocess.run(
                ["ffmpeg", "-version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                # Extract version from output
                version_line = result.stdout.split("\n")[0]
                return DoctorResult("OK", version_line)
            return DoctorResult("FAIL", "ffmpeg not found")
        except FileNotFoundError:
            return DoctorResult("FAIL", "ffmpeg not installed")
        except Exception as e:
            return DoctorResult("FAIL", str(e))

    def run(self, args: list[str]) -> str:
        if len(args) < 2:
            raise ValueError(
                "Usage: uv run scripts/ffmpeg.py <input> <output> [options]\n"
                "\n"
                "Examples:\n"
                "  uv run scripts/ffmpeg.py video.mkv output.mp4      # Convert format\n"
                "  uv run scripts/ffmpeg.py audio.wav output.mp3    # Audio conversion\n"
                "  uv run scripts/ffmpeg.py video.mp4 output.mp4 -crf 28  # Compress"
            )

        # Try to add static_ffmpeg paths
        try:
            import static_ffmpeg
            static_ffmpeg.add_paths()
        except ImportError:
            pass

        input_file = args[0]
        output_file = args[1]
        ffmpeg_args = args[2:] if len(args) > 2 else []

        # Validate input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")

        # Build ffmpeg command
        cmd = ["ffmpeg", "-i", input_file, "-y", "-progress", "pipe:1"]

        # Auto-detect output format and apply appropriate encoding
        output_ext = Path(output_file).suffix.lower()
        
        # Add format-specific options
        if output_ext == ".mp4":
            # Default to H.264 with good quality/size balance
            if not any("-c:v" in arg for arg in ffmpeg_args):
                cmd.extend(["-c:v", "libx264", "-crf", "23", "-preset", "medium"])
            if not any("-c:a" in arg for arg in ffmpeg_args):
                cmd.extend(["-c:a", "aac", "-b:a", "128k"])
        elif output_ext == ".mp3":
            if not any("-c:a" in arg for arg in ffmpeg_args):
                cmd.extend(["-c:a", "libmp3lame", "-b:a", "192k"])
        elif output_ext == ".aac":
            if not any("-c:a" in arg for arg in ffmpeg_args):
                cmd.extend(["-c:a", "aac", "-b:a", "128k"])
        elif output_ext == ".wav":
            if not any("-c:a" in arg for arg in ffmpeg_args):
                cmd.extend(["-c:a", "pcm_s16le"])

        # Add any user-provided args
        cmd.extend(ffmpeg_args)

        # Add output file
        cmd.append(output_file)

        # Run ffmpeg
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=600  # 10 minutes max
        )

        if result.returncode != 0:
            raise RuntimeError(
                f"FFmpeg failed (exit code {result.returncode}):\n"
                f"{result.stderr}"
            )

        # Get output file size
        output_size = os.path.getsize(output_file)
        input_size = os.path.getsize(input_file)
        ratio = (output_size / input_size) * 100 if input_size > 0 else 0

        return (
            f"✓ Converted {input_file} → {output_file}\n"
            f"  Input:  {input_size:,} bytes\n"
            f"  Output: {output_size:,} bytes ({ratio:.1f}% of original)"
        )

    @property
    def troubleshooting(self) -> list[tuple[str, str]]:
        return [
            ("ffmpeg not found", "Run: brew install ffmpeg (macOS) or sudo apt install ffmpeg (Linux)"),
            ("Output file too large", "Add compression: uv run scripts/ffmpeg.py input.mp4 output.mp4 -crf 28"),
            ("Format not supported", "Check FFmpeg supports: ffmpeg -formats"),
            ("Conversion too slow", "Add preset: -preset ultrafast (faster) or -preset slow (better quality)"),
        ]


def main():
    tool = FFmpegTool()
    if len(sys.argv) < 2:
        print(tool.description)
        print(f"\nUsage: {tool.usage}")
        sys.exit(1)
    try:
        result = tool.run(sys.argv[1:])
        print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
