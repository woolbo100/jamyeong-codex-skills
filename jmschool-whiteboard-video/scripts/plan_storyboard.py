#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

LAYOUTS = [
    "title_left_icon_right",
    "big_quote_center",
    "top_title_bottom_steps",
    "problem_vs_solution",
    "checklist_layout",
]

ICONS = {
    "idea": "lightbulb",
    "question": "chat",
    "goal": "target",
    "learning": "book",
    "growth": "rocket",
    "heart": "heart",
    "time": "clock",
    "list": "checklist",
    "ai": "computer",
    "write": "pencil",
}


def read_text(text: str | None, input_path: str | None) -> str:
    if text:
        return text.strip()
    if input_path:
        return Path(input_path).read_text(encoding="utf-8-sig").strip()
    raise SystemExit("Provide --text or --input")


def split_sentences(text: str) -> list[str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    parts: list[str] = []
    for line in lines or [text]:
        chunks = re.split(r"(?<=[.!?。！？])\s+|(?<=[.!?])|(?<=다\.)|(?<=요\.)|(?<=죠\.)|(?<=니다\.)", line)
        for chunk in chunks:
            cleaned = chunk.strip(" \t\r\n.。")
            if cleaned:
                parts.append(cleaned)
    return parts or [text.strip()]


def choose_scene_count(sentences: list[str], requested: int | None) -> int:
    if requested:
        return max(1, min(12, requested))
    if len(sentences) <= 4:
        return len(sentences)
    return max(5, min(8, len(sentences)))


def merge_to_scene_units(sentences: list[str], count: int) -> list[str]:
    if len(sentences) <= count:
        return sentences
    units: list[str] = []
    for i in range(count):
        start = round(i * len(sentences) / count)
        end = round((i + 1) * len(sentences) / count)
        units.append(" ".join(sentences[start:end]).strip())
    return [u for u in units if u]


def compact(text: str, max_chars: int) -> str:
    text = re.sub(r"\s+", " ", text).strip(" .")
    replacements = [
        ("할 수 있습니다", "할 수 있습니다"),
        ("중요하게 생각합니다", "중요합니다"),
        ("집중합니다", "집중합니다"),
        ("시작됩니다", "시작됩니다"),
    ]
    for a, b in replacements:
        text = text.replace(a, b)
    if len(text) <= max_chars:
        return text
    clauses = re.split(r"[,，]| 그리고 | 그래서 | 하지만 | 또한 | 즉 ", text)
    clauses = [c.strip(" .") for c in clauses if c.strip(" .")]
    for clause in clauses:
        if 4 <= len(clause) <= max_chars:
            return clause
    return text[: max_chars - 1].rstrip() + "…"


def to_display_lines(narration: str) -> tuple[str, list[str]]:
    normalized = re.sub(r"\s+", " ", narration).strip()
    visual_rules = [
        (["반복", "업무", "줄"], ("반복 업무가 줄어듭니다", ["시간이 생깁니다", "중요한 일에 집중합니다"])),
        (["자동화", "나눕"], ("일을 나눕니다", ["사람이 할 일", "AI가 도울 일"])),
        (["글쓰기", "요약"], ("먼저 맡겨봅니다", ["글쓰기", "요약과 정리"])),
        (["시간", "중요"], ("중요한 일에 집중합니다", ["판단할 시간", "대화할 시간"])),
        (["작게", "시작"], ("작게 시작합니다", ["결과를 확인합니다", "흐름을 만듭니다"])),
        (["질문", "기록"], ("질문하고 기록합니다", ["생각이 선명해집니다"])),
        (["배움", "수업"], ("배움이 실천이 됩니다", ["알고 끝내지 않습니다"])),
        (["방향", "기준"], ("내 기준이 생깁니다", ["흔들릴 때 돌아옵니다"])),
        (["마음", "현실"], ("마음과 현실을 정리합니다", ["지금 문제를 봅니다"])),
        (["AI", "도구"], ("도구가 연결됩니다", ["일상이 가벼워집니다"])),
    ]
    for keywords, result in visual_rules:
        if all(keyword in normalized for keyword in keywords):
            return result

    clauses = [c.strip(" .") for c in re.split(r"[,，]| 그리고 | 그래서 | 또한 | 즉 | 하지만 |\\s+-\\s+", normalized) if c.strip(" .")]
    if not clauses:
        clauses = [normalized]

    headline = compact(clauses[0], 18)
    points = []
    for clause in clauses[1:]:
        point = compact(clause, 24)
        if point and point != headline:
            points.append(point)
        if len(points) == 2:
            break

    if not points:
        words = normalized.split()
        if len(words) >= 5:
            points = [compact(" ".join(words[2:]), 24)]
        else:
            points = [compact(normalized, 24)]
    return headline, points[:2]


def choose_icon(text: str) -> str:
    t = text.lower()
    rules = [
        (["ai", "자동화", "도구", "컴퓨터", "기술"], "computer"),
        (["질문", "대화", "소통", "말"], "chat"),
        (["기록", "쓰기", "메모", "정리"], "pencil"),
        (["배움", "수업", "지식", "공부", "강의"], "book"),
        (["목표", "방향", "기준", "나침반"], "target"),
        (["성장", "실천", "시작", "도전"], "rocket"),
        (["마음", "관계", "공감"], "heart"),
        (["시간", "하루", "반복"], "clock"),
        (["체크", "단계", "목록", "방법"], "checklist"),
    ]
    for keywords, icon in rules:
        if any(k in t for k in keywords):
            return icon
    return "lightbulb"


def visual_type_for(icon: str) -> str:
    if icon in {"chat", "heart"}:
        return "relationship"
    if icon in {"target", "rocket", "clock"}:
        return "process"
    if icon in {"book", "pencil", "checklist"}:
        return "learning"
    if icon == "computer":
        return "technology"
    return "concept"


def emphasis_words(headline: str, points: list[str]) -> list[str]:
    text = " ".join([headline] + points)
    words = re.findall(r"[가-힣A-Za-z0-9]{2,}", text)
    filtered = [w for w in words if w not in {"그리고", "하지만", "그래서", "합니다", "있습니다"}]
    return filtered[:3]


def build_storyboard(text: str, title: str, scene_count: int | None = None) -> dict:
    sentences = split_sentences(text)
    count = choose_scene_count(sentences, scene_count)
    units = merge_to_scene_units(sentences, count)
    scenes = []
    for idx, narration in enumerate(units, start=1):
        headline, points = to_display_lines(narration)
        icon = choose_icon(narration + " " + headline)
        scenes.append({
            "scene_number": idx,
            "narration": narration,
            "short_headline": headline,
            "key_points": points,
            "visual_type": visual_type_for(icon),
            "icon_type": icon,
            "emphasis_words": emphasis_words(headline, points),
            "layout_type": LAYOUTS[(idx - 1) % len(LAYOUTS)],
            "duration_hint": "auto",
        })
    return {
        "title": title,
        "scene_count": len(scenes),
        "planning_rules": {
            "screen_text": "headline plus 1-2 short supporting lines",
            "display_sentence_rule": "Convert reading sentences into short visual phrases.",
            "default_scene_range": "5-8",
        },
        "scenes": scenes,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Plan a scene storyboard JSON for a whiteboard explainer.")
    parser.add_argument("--input")
    parser.add_argument("--text")
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", default="화이트보드 설명 영상")
    parser.add_argument("--scene-count", type=int)
    args = parser.parse_args()

    text = read_text(args.text, args.input)
    storyboard = build_storyboard(text, args.title, args.scene_count)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(storyboard, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"STORYBOARD={out.resolve()}")


if __name__ == "__main__":
    main()
