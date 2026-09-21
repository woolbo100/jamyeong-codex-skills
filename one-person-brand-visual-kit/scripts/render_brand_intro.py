#!/usr/bin/env python3
"""Render a deterministic 8-second branded intro without an external API."""

from __future__ import annotations

import argparse
import math
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageColor, ImageDraw, ImageFont


WIDTH, HEIGHT, FPS, DURATION = 1920, 1080, 30, 8


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--logo", required=True, type=Path, help="Transparent PNG logo")
    parser.add_argument("--brand-name", required=True)
    parser.add_argument("--slogan", default="")
    parser.add_argument("--primary", default="#241535")
    parser.add_argument("--secondary", default="#D6B36A")
    parser.add_argument("--font", type=Path, help="TTF/OTF font; required for non-ASCII text")
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def ease(value: float) -> float:
    value = max(0.0, min(1.0, value))
    return value * value * (3.0 - 2.0 * value)


def load_font(path: Path | None, size: int, text: str) -> ImageFont.FreeTypeFont:
    if any(ord(char) > 127 for char in text) and path is None:
        raise SystemExit("Non-ASCII text requires --font with a suitable licensed font file.")
    candidate = path or Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    if not candidate.exists():
        raise SystemExit(f"Font not found: {candidate}")
    return ImageFont.truetype(str(candidate), size)


def fit_logo(logo: Image.Image, max_width: int, max_height: int) -> Image.Image:
    scale = min(max_width / logo.width, max_height / logo.height)
    return logo.resize((max(1, int(logo.width * scale)), max(1, int(logo.height * scale))), Image.Resampling.LANCZOS)


def centered_text(draw: ImageDraw.ImageDraw, y: int, text: str, font: ImageFont.FreeTypeFont, fill: tuple[int, int, int, int]) -> None:
    box = draw.textbbox((0, 0), text, font=font)
    x = (WIDTH - (box[2] - box[0])) // 2
    draw.text((x, y), text, font=font, fill=fill)


def main() -> int:
    args = parse_args()
    if shutil.which("ffmpeg") is None:
        raise SystemExit("FFmpeg is required but was not found.")
    if not args.logo.exists():
        raise SystemExit(f"Logo not found: {args.logo}")
    args.output.parent.mkdir(parents=True, exist_ok=True)

    primary = ImageColor.getrgb(args.primary)
    secondary = ImageColor.getrgb(args.secondary)
    logo_base = fit_logo(Image.open(args.logo).convert("RGBA"), 700, 360)
    name_font = load_font(args.font, 72, args.brand_name)
    slogan_font = load_font(args.font, 34, args.slogan)

    command = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{WIDTH}x{HEIGHT}", "-r", str(FPS), "-i", "-",
        "-an", "-t", str(DURATION), "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", str(args.output),
    ]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    assert process.stdin is not None

    for frame_index in range(FPS * DURATION):
        t = frame_index / FPS
        canvas = Image.new("RGB", (WIDTH, HEIGHT), primary)
        layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
        draw = ImageDraw.Draw(layer)

        # Subtle orbit and line motifs derived from the secondary brand color.
        motif_alpha = int(70 * ease(min(t / 2.0, (DURATION - t) / 0.8)))
        radius = 260 + int(18 * math.sin(t * 1.4))
        cx, cy = WIDTH // 2, HEIGHT // 2 - 45
        draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), outline=(*secondary, motif_alpha), width=3)
        draw.line((180, HEIGHT - 170, WIDTH - 180, HEIGHT - 170), fill=(*secondary, motif_alpha // 2), width=2)

        logo_progress = ease((t - 1.0) / 1.5)
        outro = ease((DURATION - t) / 0.55)
        logo_alpha = int(255 * logo_progress * outro)
        scale = 0.88 + 0.12 * logo_progress
        logo = logo_base.resize((int(logo_base.width * scale), int(logo_base.height * scale)), Image.Resampling.LANCZOS)
        if logo_alpha < 255:
            alpha = logo.getchannel("A").point(lambda value: value * logo_alpha // 255)
            logo.putalpha(alpha)
        layer.alpha_composite(logo, ((WIDTH - logo.width) // 2, cy - logo.height // 2 - 55))

        name_alpha = int(255 * ease((t - 4.1) / 0.7) * outro)
        centered_text(draw, 720, args.brand_name, name_font, (*secondary, name_alpha))
        if args.slogan:
            slogan_alpha = int(225 * ease((t - 5.0) / 0.7) * outro)
            centered_text(draw, 820, args.slogan, slogan_font, (255, 255, 255, slogan_alpha))

        canvas = Image.alpha_composite(canvas.convert("RGBA"), layer).convert("RGB")
        process.stdin.write(canvas.tobytes())

    process.stdin.close()
    return_code = process.wait()
    if return_code != 0:
        raise SystemExit(f"FFmpeg failed with exit code {return_code}")
    print(args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
