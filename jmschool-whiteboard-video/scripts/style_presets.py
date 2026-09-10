from __future__ import annotations

STYLE_PRESETS = {
    "clean_education": {
        "background_color": "#F7F3E8",
        "primary_line_color": "#202124",
        "accent_color": "#2F6FDB",
        "secondary_accent_color": "#E35B4F",
        "muted_line_color": "#8A8172",
        "font_size_scale": 1.0,
        "title_style": {"weight": "bold", "case": "natural"},
        "body_style": {"weight": "regular", "max_lines": 2},
        "icon_stroke_style": {"width": 7, "rounded": True},
    },
    "premium_business": {
        "background_color": "#F5F1E7",
        "primary_line_color": "#1E293B",
        "accent_color": "#0F766E",
        "secondary_accent_color": "#B7791F",
        "muted_line_color": "#64748B",
        "font_size_scale": 0.94,
        "title_style": {"weight": "bold", "case": "natural"},
        "body_style": {"weight": "regular", "max_lines": 2},
        "icon_stroke_style": {"width": 6, "rounded": True},
    },
    "warm_story": {
        "background_color": "#FFF4DD",
        "primary_line_color": "#2D2420",
        "accent_color": "#D97706",
        "secondary_accent_color": "#C2410C",
        "muted_line_color": "#9A7B54",
        "font_size_scale": 1.02,
        "title_style": {"weight": "bold", "case": "natural"},
        "body_style": {"weight": "regular", "max_lines": 2},
        "icon_stroke_style": {"width": 7, "rounded": True},
    },
    "simple_kids": {
        "background_color": "#FFFBEA",
        "primary_line_color": "#1F2937",
        "accent_color": "#2563EB",
        "secondary_accent_color": "#F97316",
        "muted_line_color": "#6B7280",
        "font_size_scale": 1.08,
        "title_style": {"weight": "bold", "case": "natural"},
        "body_style": {"weight": "regular", "max_lines": 2},
        "icon_stroke_style": {"width": 8, "rounded": True},
    },
}

DEFAULT_STYLE = "clean_education"


def get_style(name: str | None) -> dict:
    key = name or DEFAULT_STYLE
    if key not in STYLE_PRESETS:
        available = ", ".join(sorted(STYLE_PRESETS))
        raise ValueError(f"Unknown style '{key}'. Available styles: {available}")
    return STYLE_PRESETS[key]


def style_names() -> list[str]:
    return sorted(STYLE_PRESETS)
