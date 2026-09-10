#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import json
import math
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import edge_tts
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from plan_storyboard import build_storyboard, read_text  # noqa: E402
from style_presets import DEFAULT_STYLE, get_style, style_names  # noqa: E402

DEFAULT_VOICE = "ko-KR-SunHiNeural"
DEFAULT_CTA = "더 배우고 싶다면 자명스쿨 콘텐츠를 확인하세요."
WORKSPACE = Path("C:/Users/SAMSUNG/Documents/ChatGPT/화이트보드프로젝트")
SRT_RENDERER_ROOT = WORKSPACE / "srt-whiteboard-animation"
DEFAULT_FFMPEG = WORKSPACE / "tools/ffmpeg/ffmpeg-9.0.1-essentials_build/bin/ffmpeg.exe"
DEFAULT_FFPROBE = WORKSPACE / "tools/ffmpeg/ffmpeg-9.0.1-essentials_build/bin/ffprobe.exe"

ICON_TYPES = [
    "lightbulb",
    "chat",
    "target",
    "book",
    "rocket",
    "heart",
    "clock",
    "checklist",
    "computer",
    "pencil",
]


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def font(size: int, bold: bool = False):
    candidates = [
        "C:/Windows/Fonts/malgunbd.ttf" if bold else "C:/Windows/Fonts/malgun.ttf",
        "C:/Windows/Fonts/NotoSansKR-Bold.ttf" if bold else "C:/Windows/Fonts/NotoSansKR-Regular.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for candidate in candidates:
        if candidate and os.path.exists(candidate):
            try:
                return ImageFont.truetype(candidate, size=size)
            except OSError:
                pass
    return ImageFont.load_default()


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font_obj, max_width: int, max_lines: int) -> list[str]:
    words = text.split()
    if not words:
        return []
    lines: list[str] = []
    current = ""
    for word in words:
        test = (current + " " + word).strip()
        bbox = draw.textbbox((0, 0), test, font=font_obj)
        if bbox[2] - bbox[0] <= max_width or not current:
            current = test
        else:
            lines.append(current)
            current = word
        if len(lines) >= max_lines:
            break
    if current and len(lines) < max_lines:
        lines.append(current)
    return lines[:max_lines]


class ArtBoard:
    def __init__(self, width: int, height: int, style: dict):
        self.width = width
        self.height = height
        self.style = style
        self.bg = hex_to_rgb(style["background_color"])
        self.ink = hex_to_rgb(style["primary_line_color"])
        self.accent = hex_to_rgb(style["accent_color"])
        self.accent2 = hex_to_rgb(style["secondary_accent_color"])
        self.muted = hex_to_rgb(style["muted_line_color"])
        self.stroke = int(style["icon_stroke_style"]["width"])
        self.scale = float(style["font_size_scale"])
        self.img = Image.new("RGB", (width, height), self.bg)
        self.draw = ImageDraw.Draw(self.img)
        self.draw.rounded_rectangle(
            (int(width * 0.025), int(height * 0.025), int(width * 0.975), int(height * 0.975)),
            radius=max(18, int(min(width, height) * 0.025)),
            outline=self.muted,
            width=max(3, self.stroke - 2),
        )

    def line(self, pts, fill=None, width=None):
        self.draw.line(pts, fill=fill or self.ink, width=width or self.stroke, joint="curve")

    def rect(self, xy, outline=None, width=None, radius=18):
        self.draw.rounded_rectangle(xy, radius=radius, outline=outline or self.ink, width=width or self.stroke)

    def circle(self, xy, outline=None, width=None):
        self.draw.ellipse(xy, outline=outline or self.ink, width=width or self.stroke)

    def text(self, xy, value: str, size: int, fill=None, bold=False, max_width=None, max_lines=1):
        f = font(max(16, int(size * self.scale)), bold=bold)
        if max_width:
            lines = wrap_text(self.draw, value, f, max_width, max_lines)
            y = xy[1]
            for line in lines:
                self.draw.text((xy[0], y), line, font=f, fill=fill or self.ink)
                bbox = self.draw.textbbox((xy[0], y), line, font=f)
                y = bbox[3] + int(size * 0.28)
            return lines
        self.draw.text(xy, value, font=f, fill=fill or self.ink)
        return [value]


def draw_icon(board: ArtBoard, icon: str, box: tuple[int, int, int, int]):
    d = board.draw
    x1, y1, x2, y2 = box
    w, h = x2 - x1, y2 - y1
    cx, cy = x1 + w // 2, y1 + h // 2
    s = board.stroke

    if icon == "lightbulb":
        d.arc((cx - w * 0.22, cy - h * 0.32, cx + w * 0.22, cy + h * 0.12), 0, 360, fill=board.ink, width=s)
        board.line([(cx - w * 0.08, cy + h * 0.10), (cx - w * 0.03, cy + h * 0.28)], width=s)
        board.line([(cx + w * 0.08, cy + h * 0.10), (cx + w * 0.03, cy + h * 0.28)], width=s)
        board.line([(cx - w * 0.12, cy + h * 0.32), (cx + w * 0.12, cy + h * 0.32)], fill=board.accent2, width=s)
        for dx, dy in [(-0.35, -0.28), (0, -0.42), (0.35, -0.28)]:
            board.line([(cx + w * dx, cy + h * dy), (cx + w * dx * 0.75, cy + h * dy * 0.75)], fill=board.accent, width=max(3, s - 2))
    elif icon == "chat":
        board.rect((x1 + w * 0.12, y1 + h * 0.20, x2 - w * 0.12, y2 - h * 0.26), radius=24)
        board.line([(x1 + w * 0.30, y2 - h * 0.26), (x1 + w * 0.20, y2 - h * 0.08)], width=s)
        board.line([(x1 + w * 0.25, y1 + h * 0.40), (x2 - w * 0.25, y1 + h * 0.40)], fill=board.accent, width=max(3, s - 2))
        board.line([(x1 + w * 0.25, y1 + h * 0.55), (x2 - w * 0.35, y1 + h * 0.55)], fill=board.accent, width=max(3, s - 2))
    elif icon == "target":
        for r, col in [(0.36, board.ink), (0.24, board.accent), (0.10, board.accent2)]:
            board.circle((cx - w * r, cy - h * r, cx + w * r, cy + h * r), outline=col)
        board.line([(x1 + w * 0.12, cy), (x2 - w * 0.12, cy)], fill=board.muted, width=max(3, s - 2))
        board.line([(cx, y1 + h * 0.12), (cx, y2 - h * 0.12)], fill=board.muted, width=max(3, s - 2))
    elif icon == "book":
        board.rect((x1 + w * 0.14, y1 + h * 0.22, cx, y2 - h * 0.18), radius=20)
        board.rect((cx, y1 + h * 0.22, x2 - w * 0.14, y2 - h * 0.18), radius=20)
        board.line([(cx, y1 + h * 0.23), (cx, y2 - h * 0.18)], fill=board.accent, width=max(3, s - 2))
        for i in range(3):
            yy = y1 + h * (0.36 + i * 0.13)
            board.line([(x1 + w * 0.22, yy), (cx - w * 0.08, yy)], fill=board.muted, width=max(3, s - 3))
            board.line([(cx + w * 0.08, yy), (x2 - w * 0.22, yy)], fill=board.muted, width=max(3, s - 3))
    elif icon == "rocket":
        d.arc((cx - w * 0.13, cy - h * 0.35, cx + w * 0.13, cy + h * 0.08), 180, 360, fill=board.ink, width=s)
        board.line([(cx - w * 0.13, cy), (cx, cy + h * 0.28), (cx + w * 0.13, cy)], width=s)
        board.line([(cx - w * 0.08, cy + h * 0.30), (cx - w * 0.16, cy + h * 0.44)], fill=board.accent, width=s)
        board.line([(cx + w * 0.08, cy + h * 0.30), (cx + w * 0.16, cy + h * 0.44)], fill=board.accent, width=s)
        board.line([(cx, cy + h * 0.32), (cx, cy + h * 0.52)], fill=board.accent2, width=s)
    elif icon == "heart":
        d.arc((cx - w * 0.34, cy - h * 0.26, cx, cy + h * 0.18), 190, 20, fill=board.accent2, width=s)
        d.arc((cx, cy - h * 0.26, cx + w * 0.34, cy + h * 0.18), 160, 350, fill=board.accent2, width=s)
        board.line([(cx - w * 0.33, cy), (cx, cy + h * 0.38), (cx + w * 0.33, cy)], fill=board.accent2, width=s)
    elif icon == "clock":
        board.circle((cx - w * 0.32, cy - h * 0.32, cx + w * 0.32, cy + h * 0.32))
        board.line([(cx, cy), (cx, cy - h * 0.20)], fill=board.accent, width=s)
        board.line([(cx, cy), (cx + w * 0.18, cy + h * 0.10)], fill=board.accent2, width=s)
    elif icon == "checklist":
        board.rect((x1 + w * 0.18, y1 + h * 0.12, x2 - w * 0.14, y2 - h * 0.12), radius=18)
        for i in range(3):
            yy = y1 + h * (0.30 + i * 0.20)
            board.line([(x1 + w * 0.27, yy), (x1 + w * 0.31, yy + h * 0.04), (x1 + w * 0.38, yy - h * 0.05)], fill=board.accent, width=max(4, s - 1))
            board.line([(x1 + w * 0.45, yy), (x2 - w * 0.25, yy)], fill=board.muted, width=max(3, s - 3))
    elif icon == "computer":
        board.rect((x1 + w * 0.14, y1 + h * 0.18, x2 - w * 0.14, y2 - h * 0.28), radius=12)
        board.line([(cx, y2 - h * 0.28), (cx, y2 - h * 0.14)], fill=board.accent, width=s)
        board.line([(cx - w * 0.20, y2 - h * 0.14), (cx + w * 0.20, y2 - h * 0.14)], width=s)
        for dx, dy in [(-0.18, -0.05), (0.0, -0.16), (0.18, -0.05), (0.0, 0.08)]:
            board.circle((cx + w * dx - 12, cy + h * dy - 12, cx + w * dx + 12, cy + h * dy + 12), outline=board.accent2, width=max(3, s - 2))
    else:
        board.line([(cx - w * 0.22, cy + h * 0.30), (cx + w * 0.18, cy - h * 0.30)], width=s)
        board.line([(cx + w * 0.18, cy - h * 0.30), (cx + w * 0.30, cy - h * 0.18)], fill=board.accent2, width=s)
        board.line([(cx - w * 0.28, cy + h * 0.36), (cx - w * 0.14, cy + h * 0.28)], fill=board.accent, width=s)


def add_badge(board: ArtBoard, x: int, y: int, number: int):
    r = max(18, int(min(board.width, board.height) * 0.028))
    board.circle((x, y, x + 2 * r, y + 2 * r), outline=board.accent2, width=max(4, board.stroke - 1))
    board.text((x + int(r * 0.62), y + int(r * 0.30)), str(number), int(r * 0.9), fill=board.accent2, bold=True)


def layout_boxes(width: int, height: int, index: int, total: int, layout: str) -> dict:
    margin_x = int(width * 0.08)
    margin_y = int(height * 0.10)
    footer = int(height * 0.09)
    if height > width:
        margin_x = int(width * 0.09)
        headline = (margin_x, margin_y, int(width * 0.82), int(height * 0.12))
        body = (margin_x, int(height * 0.22), int(width * 0.82), int(height * 0.16))
        icon = (int(width * 0.22), int(height * 0.43), int(width * 0.56), int(height * 0.28))
    elif layout == "title_left_icon_right":
        headline = (margin_x, int(height * 0.22), int(width * 0.43), int(height * 0.16))
        body = (margin_x, int(height * 0.43), int(width * 0.42), int(height * 0.18))
        icon = (int(width * 0.61), int(height * 0.25), int(width * 0.27), int(height * 0.35))
    elif layout == "big_quote_center":
        headline = (int(width * 0.18), int(height * 0.25), int(width * 0.64), int(height * 0.16))
        body = (int(width * 0.22), int(height * 0.49), int(width * 0.56), int(height * 0.15))
        icon = (int(width * 0.40), int(height * 0.66), int(width * 0.20), int(height * 0.18))
    elif layout == "top_title_bottom_steps":
        headline = (margin_x, margin_y, int(width * 0.84), int(height * 0.12))
        body = (margin_x, int(height * 0.23), int(width * 0.84), int(height * 0.14))
        icon = (int(width * 0.32), int(height * 0.45), int(width * 0.36), int(height * 0.28))
    elif layout == "problem_vs_solution":
        headline = (margin_x, margin_y, int(width * 0.84), int(height * 0.12))
        body = (int(width * 0.14), int(height * 0.32), int(width * 0.72), int(height * 0.16))
        icon = (int(width * 0.35), int(height * 0.54), int(width * 0.30), int(height * 0.25))
    else:
        headline = (margin_x, margin_y, int(width * 0.84), int(height * 0.12))
        body = (int(width * 0.20), int(height * 0.30), int(width * 0.58), int(height * 0.20))
        icon = (int(width * 0.35), int(height * 0.55), int(width * 0.30), int(height * 0.24))
    return {"headline": headline, "body": body, "icon": icon, "footer": footer}


def draw_scene(board: ArtBoard, scene: dict, idx: int, total: int):
    boxes = layout_boxes(board.width, board.height, idx, total, scene["layout_type"])
    hx, hy, hw, _ = boxes["headline"]
    bx, by, bw, _ = boxes["body"]
    ix, iy, iw, ih = boxes["icon"]
    title_size = 58 if board.width > board.height else 66
    body_size = 34 if board.width > board.height else 42
    add_badge(board, hx, max(18, hy - 48), idx)
    board.text((hx + 65, hy), scene["short_headline"], title_size, bold=True, max_width=hw - 70, max_lines=1)
    board.line([(hx + 65, hy + int(title_size * 1.35)), (hx + min(hw, int(title_size * 8)), hy + int(title_size * 1.35))], fill=board.accent2, width=max(4, board.stroke - 2))
    if scene["layout_type"] == "problem_vs_solution":
        board.rect((bx - 20, by - 20, bx + bw // 2 - 14, by + 130), outline=board.muted, radius=20)
        board.rect((bx + bw // 2 + 14, by - 20, bx + bw + 20, by + 130), outline=board.accent, radius=20)
        points = scene.get("key_points", [])
        left = points[0] if points else scene["short_headline"]
        right = points[1] if len(points) > 1 else "핵심에 집중합니다"
        board.text((bx + 10, by + 18), left, body_size, max_width=bw // 2 - 50, max_lines=1)
        board.text((bx + bw // 2 + 45, by + 18), right, body_size, fill=board.accent, max_width=bw // 2 - 55, max_lines=1)
        board.line([(bx + bw // 2 - 4, by + 45), (bx + bw // 2 + 30, by + 45)], fill=board.accent2, width=board.stroke)
    elif scene["layout_type"] == "checklist_layout":
        for i, point in enumerate(scene.get("key_points", [])[:2] or [scene["short_headline"]]):
            yy = by + i * int(body_size * 1.55)
            board.rect((bx, yy + 8, bx + 32, yy + 40), outline=board.accent, width=max(4, board.stroke - 2), radius=6)
            board.line([(bx + 7, yy + 25), (bx + 16, yy + 35), (bx + 31, yy + 12)], fill=board.accent, width=max(4, board.stroke - 2))
            board.text((bx + 55, yy), point, body_size, max_width=bw - 65, max_lines=1)
    else:
        points = scene.get("key_points", [])[:2]
        for i, point in enumerate(points):
            yy = by + i * int(body_size * 1.42)
            board.text((bx, yy), point, body_size, fill=board.muted if i else board.ink, max_width=bw, max_lines=1)
        if scene["layout_type"] == "top_title_bottom_steps":
            step_y = by + int(body_size * 2.4)
            for n in range(3):
                sx = bx + n * int(bw / 3)
                board.rect((sx, step_y, sx + int(bw / 4), step_y + 56), outline=board.muted, width=max(4, board.stroke - 2), radius=10)
                board.line([(sx + int(bw / 4), step_y + 28), (sx + int(bw / 4) + 48, step_y + 28)], fill=board.accent, width=max(4, board.stroke - 2))
    draw_icon(board, scene.get("icon_type", "lightbulb"), (ix, iy, ix + iw, iy + ih))


def normalize_storyboard(storyboard: dict, title: str, subtitle: str, cta: str, intro: bool, outro: bool) -> list[dict]:
    scenes = []
    n = 1
    if intro:
        scenes.append({
            "scene_number": n,
            "narration": f"{title}. {subtitle}" if subtitle else title,
            "short_headline": title[:18],
            "key_points": [subtitle[:24] if subtitle else "핵심만 쉽게 정리합니다"],
            "visual_type": "intro",
            "icon_type": "lightbulb",
            "emphasis_words": [title],
            "layout_type": "big_quote_center",
            "duration_hint": 2800,
        })
        n += 1
    for scene in storyboard["scenes"]:
        item = dict(scene)
        item["scene_number"] = n
        scenes.append(item)
        n += 1
    if outro:
        scenes.append({
            "scene_number": n,
            "narration": cta,
            "short_headline": "핵심을 실천으로",
            "key_points": [cta[:28]],
            "visual_type": "outro",
            "icon_type": "checklist",
            "emphasis_words": ["실천", "자명스쿨"],
            "layout_type": "checklist_layout",
            "duration_hint": 3500,
        })
    return scenes


def make_assets(storyboard: dict, out_dir: Path, title: str, subtitle: str, cta: str, style_name: str, width: int, height: int, audio_duration_ms: int, intro: bool, outro: bool) -> tuple[Path, Path, list[dict]]:
    style = get_style(style_name)
    scenes = normalize_storyboard(storyboard, title, subtitle, cta, intro, outro)
    board = ArtBoard(width, height, style)
    total = len(scenes)
    elements = []
    gap = 320
    available = max(1000, audio_duration_ms - gap * 2)
    slot = available / max(1, total)
    for idx, scene in enumerate(scenes, start=1):
        draw_scene(board, scene, idx, total)
        boxes = layout_boxes(width, height, idx, total, scene["layout_type"])
        region = union_region(boxes, width, height)
        start = int(gap + (idx - 1) * slot)
        duration = max(1100, int(slot * 0.72))
        elements.append({
            "id": f"scene-{idx:02d}",
            "label": scene["short_headline"],
            "sequence": idx,
            "narrativeRole": scene["visual_type"],
            "subtitle": scene["narration"],
            "type": "scene",
            "region": region,
            "reveal": {
                "direction": "top_to_bottom",
                "startMs": start,
                "durationMs": duration,
                "maskPaddingPx": 26,
                "protectedRegions": [],
            },
            "handPath": {
                "start": [region["x"] + region["width"] // 2, region["y"]],
                "end": [region["x"] + region["width"] // 2, region["y"] + region["height"]],
                "easing": "easeInOut",
            },
        })
    safe = safe_name(title)
    png = out_dir / "srt_assets" / f"{safe}.png"
    ann = out_dir / "srt_assets" / f"{safe}.annotation.json"
    png.parent.mkdir(parents=True, exist_ok=True)
    board.img.save(png)
    annotation = {
        "sceneId": "scene-01",
        "canvas": {"width": width, "height": height},
        "storyBasis": storyboard.get("title", title),
        "sceneDurationMs": audio_duration_ms,
        "elements": elements,
    }
    ann.write_text(json.dumps(annotation, ensure_ascii=False, indent=2), encoding="utf-8")
    return png, ann, scenes


def union_region(boxes: dict, width: int, height: int) -> dict:
    coords = []
    for key in ("headline", "body", "icon"):
        x, y, w, h = boxes[key]
        coords.append((x, y, x + w, y + h))
    x0 = max(0, min(c[0] for c in coords) - 60)
    y0 = max(0, min(c[1] for c in coords) - 75)
    x1 = min(width, max(c[2] for c in coords) + 70)
    y1 = min(height, max(c[3] for c in coords) + 80)
    return {"x": int(x0), "y": int(y0), "width": int(x1 - x0), "height": int(y1 - y0)}


def safe_name(value: str) -> str:
    out = re.sub(r"[^A-Za-z0-9가-힣_-]+", "-", value).strip("-")
    return out or "whiteboard"


async def synthesize(text: str, output: Path, voice: str, rate: str):
    output.parent.mkdir(parents=True, exist_ok=True)
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    await communicate.save(str(output))


def which_or_default(name: str, default: Path | None = None) -> str:
    found = shutil.which(name)
    if found:
        return found
    if default and default.exists():
        return str(default)
    return name


def run(cmd: list[str], cwd: Path | None = None):
    result = subprocess.run(cmd, cwd=str(cwd) if cwd else None, text=True)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def ffprobe_duration_ms(path: Path) -> int:
    ffprobe = which_or_default("ffprobe", DEFAULT_FFPROBE)
    result = subprocess.run(
        [ffprobe, "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return 60000
    try:
        return max(3000, int(float(result.stdout.strip()) * 1000))
    except ValueError:
        return 60000


def render_silent(png: Path, ann: Path, output: Path, width: int, height: int, fps: int):
    root = SRT_RENDERER_ROOT
    renderer = root / "scripts/render_stream_whiteboard.py"
    if not renderer.exists():
        raise SystemExit(f"Missing srt-whiteboard-animation renderer: {renderer}")
    py = root / ".venv/Scripts/python.exe"
    python = str(py) if py.exists() else sys.executable
    hand = root / "assets/drawing-hand.png"
    cmd = [
        python,
        str(renderer),
        str(png),
        str(ann),
        str(output),
        str(hand),
        "--ink-path",
        "grid",
        "--color-fill",
        "contour-wipe",
        "--pause",
        "light",
        "--fps",
        str(fps),
        "--cap-long-edge",
        str(max(width, height)),
        "--grid-edge",
        "8",
    ]
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    result = subprocess.run(cmd, cwd=str(root), env=env, text=True)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def mux(silent: Path, audio: Path, output: Path):
    ffmpeg = which_or_default("ffmpeg", DEFAULT_FFMPEG)
    run([ffmpeg, "-y", "-i", str(silent), "-i", str(audio), "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", str(output)])


def write_preview_frames(video: Path, out_dir: Path):
    ffmpeg = which_or_default("ffmpeg", DEFAULT_FFMPEG)
    for stamp, name in [("00:00:01", "preview_01s.png"), ("00:00:10", "preview_10s.png"), ("00:00:25", "preview_25s.png")]:
        subprocess.run([ffmpeg, "-y", "-ss", stamp, "-i", str(video), "-frames:v", "1", "-update", "1", str(out_dir / name)], text=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a clean narrated whiteboard explainer MP4.")
    parser.add_argument("--input")
    parser.add_argument("--text")
    parser.add_argument("--output", default="output/whiteboard.mp4")
    parser.add_argument("--audio-output", default="output/narration.mp3")
    parser.add_argument("--voice", default=DEFAULT_VOICE)
    parser.add_argument("--rate", default="+0%")
    parser.add_argument("--style", default=DEFAULT_STYLE, choices=style_names())
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--title", default="화이트보드 설명 영상")
    parser.add_argument("--subtitle", default="핵심만 쉽게 정리합니다")
    parser.add_argument("--cta", default=DEFAULT_CTA)
    parser.add_argument("--no-intro", action="store_true")
    parser.add_argument("--no-outro", action="store_true")
    args = parser.parse_args()

    text = read_text(args.text, args.input)
    output = Path(args.output)
    audio_output = Path(args.audio_output)
    out_dir = output.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    storyboard = build_storyboard(text, args.title)
    storyboard_path = out_dir / "storyboard.json"
    storyboard_path.write_text(json.dumps(storyboard, ensure_ascii=False, indent=2), encoding="utf-8")

    narration_text = []
    if not args.no_intro:
        narration_text.append(f"{args.title}. {args.subtitle}")
    narration_text.extend(scene["narration"] for scene in storyboard["scenes"])
    if not args.no_outro:
        narration_text.append(args.cta)
    asyncio.run(synthesize("\n".join(narration_text), audio_output, args.voice, args.rate))
    duration_ms = ffprobe_duration_ms(audio_output)

    png, ann, _ = make_assets(storyboard, out_dir, args.title, args.subtitle, args.cta, args.style, args.width, args.height, duration_ms, not args.no_intro, not args.no_outro)
    silent = out_dir / f"{output.stem}_silent.mp4"
    render_silent(png, ann, silent, args.width, args.height, args.fps)
    mux(silent, audio_output, output)
    write_preview_frames(output, out_dir)

    print(f"STORYBOARD={storyboard_path.resolve()}")
    print(f"LINEART={png.resolve()}")
    print(f"ANNOTATION={ann.resolve()}")
    print(f"MP3={audio_output.resolve()}")
    print(f"MP4={output.resolve()}")


if __name__ == "__main__":
    main()
