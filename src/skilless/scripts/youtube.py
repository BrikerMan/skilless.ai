#!/usr/bin/env python3
"""YouTube tool - Extract video info and subtitles via yt-dlp."""

from __future__ import annotations

import json
import sys

try:
    from skilless.scripts.base import BaseTool, DoctorResult
except ImportError:
    from base import BaseTool, DoctorResult


class YouTubeTool(BaseTool):
    name = "ytd"
    description = (
        "Extract video subtitles and metadata "
        "(YouTube, Bilibili, TikTok, Twitter, Vimeo, Twitch, 1700+ platforms)"
    )
    usage = "cd ~/.agents/skills/skilless/ && uv run scripts/youtube.py <url>"
    how = "Uses yt-dlp to extract video metadata and subtitles; supports 1700+ platforms"

    def doctor(self) -> DoctorResult:
        try:
            import yt_dlp

            ydl_opts = {
                "quiet": True,
                "no_warnings": True,
                "extract_flat": False,
                "skip_download": True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(
                    "https://www.bilibili.com/video/BV1GJ411x7h7",
                    download=False,
                )
                if info and info.get("title"):
                    title = info["title"][:30]
                    return DoctorResult("OK", f"tested with '{title}...'")
            return DoctorResult("FAIL", "could not extract video info")
        except Exception:
            try:
                import yt_dlp

                version = yt_dlp.version.__version__
                return DoctorResult("OK", f"version {version} (network test failed)")
            except Exception as e:
                return DoctorResult("FAIL", str(e))

    def run(self, args: list[str]) -> str:
        if not args:
            raise ValueError("Usage: cd ~/.agents/skills/skilless/ && uv run scripts/youtube.py <url>")

        from pathlib import Path

        import yt_dlp

        url = args[0]
        ydl_opts = {
            "quiet": True,
            "dump_single_json": True,
            "skip_download": True,
            "writeinfojson": False,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        # Save full metadata to CWD for later reference
        video_id = info.get("id", "unknown")
        out_path = Path.cwd() / f"ytd_{video_id}.json"
        out_path.write_text(json.dumps(info, indent=2, ensure_ascii=False))

        # Return only key fields to avoid flooding AI context
        title = info.get("title", "")
        uploader = info.get("uploader", "")
        duration = info.get("duration")
        upload_date = info.get("upload_date", "")
        description = (info.get("description") or "")[:500]
        webpage_url = info.get("webpage_url", url)

        subtitles = info.get("subtitles") or {}
        auto_captions = info.get("automatic_captions") or {}
        available_langs = list(subtitles.keys()) or list(auto_captions.keys())

        lines = [
            f"# {title}",
            f"Uploader: {uploader}",
            f"URL: {webpage_url}",
        ]
        if duration:
            mins, secs = divmod(int(duration), 60)
            lines.append(f"Duration: {mins}:{secs:02d}")
        if upload_date:
            lines.append(f"Upload date: {upload_date}")
        if description:
            lines.append(f"\nDescription:\n{description}")
        if available_langs:
            lines.append(f"\nAvailable subtitles: {', '.join(available_langs[:10])}")
        lines.append(f"\nFull metadata saved to: {out_path}")

        return "\n".join(lines)

    @property
    def troubleshooting(self) -> list[tuple[str, str]]:
        from pathlib import Path
        _venv = Path.home() / ".agents/skills/skilless/.venv"
        _pip = f"uv pip install --python {_venv}"
        return [
            ("yt-dlp not installed", f"Run: {_pip} yt-dlp"),
            (
                "Cannot extract subtitles/metadata",
                "Video may have no subtitles, or is geo-/platform-restricted",
            ),
            (
                "YouTube: 'Sign in' or 'not a bot' error",
                "IP flagged by YouTube; try: 1) enable proxy 2) switch to TUN/global mode "
                "3) pass cookies: yt-dlp --cookies-from-browser chrome <url>",
            ),
            (
                "YouTube connection timeout (China network)",
                "YouTube requires a proxy; switch to TUN mode, or set: "
                "export HTTPS_PROXY=http://127.0.0.1:<port>",
            ),
            ("Network error (non-YouTube)", "Check network; some platforms require a proxy"),
            ("yt-dlp version outdated", f"Run: {_pip} -U yt-dlp"),
        ]


def main():
    tool = YouTubeTool()
    try:
        print(tool.run(sys.argv[1:]))
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
