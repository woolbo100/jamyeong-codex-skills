---
name: logo-automation-system
description: Create logo and branding assets from a brand brief and optional reference images. Use when the user asks for logo design, logo concepts, logo options, brand identity design, branding assets, mockup images, brand guidelines, Korean or English logo prompts, or a workflow that generates multiple logo concepts, variations, product mockups, and a brand guideline document.
---

# Logo Automation System

Run a staged branding workflow: gather a brand brief, analyze optional reference images, generate nine distinct logo concepts as separate assets, refine the selected concept with nine variations, recommend brand-fit mockups, create selected mockups, and produce a concise brand guideline document.

## Core Rules

- Use image generation for raster logo and mockup assets.
- Generate each logo, variation, and mockup as its own image. Do not create a combined grid unless the user explicitly asks for a contact sheet.
- Keep logos simple, legible, high-contrast, isolated on a white or transparent-looking background, and suitable for later mockup use.
- Treat reference images as style references, not objects to copy exactly.
- If required brand inputs are missing, ask for only the missing essentials before generating: brand name, brand description, main color, target audience, desired mood, reference image status, and optional requirements.
- If the user already provided enough information, proceed without re-asking.

## Input Form

When the brief is incomplete, ask in this compact format:

```text
[1] Brand name:
[2] Brand description:
[3] Main color:
[4] Target audience:
[5] Desired mood:
[6] Reference image: attached / none
[7] Optional requirements:
```

Korean prompts are welcome. Preserve Korean brand names exactly when the user provides them.

## Reference Image Analysis

If images are attached, inspect them before generation and extract:

- Overall visual mood and tone
- Line weight and shape language
- Style category such as minimal, organic, geometric, vintage, premium, playful, or editorial
- Main and accent colors
- Typography clues such as serif, sans serif, handwritten, condensed, rounded, or monogram-like

If no reference image is available, infer style from the desired mood, audience, industry, and main color. Briefly tell the user what assumptions are being used.

## Stage 1: Generate 9 Logo Concepts

Create nine concept prompts using the same brand brief but different design directions:

| No. | Concept | Direction |
| --- | --- | --- |
| 1 | Wordmark | Refined typography built around the full brand name |
| 2 | Lettermark | Initials or one to two letters as a monogram |
| 3 | Symbol | Icon or pictogram expressing the brand value |
| 4 | Combination | Symbol plus brand name in a practical lockup |
| 5 | Emblem | Badge, seal, shield, or circular integrated mark |
| 6 | Geometric Abstract | Abstract symbol using grids, lines, and geometric forms |
| 7 | Organic | Natural, flowing, botanical, water, light, or handmade cues |
| 8 | Dynamic | Directional, energetic, motion-led structure |
| 9 | Heritage | Vintage, craft, retro, classic, or archival character |

Each image prompt must include:

- Concept type
- Exact brand name text
- Main color and any accent colors
- Two to three style cues from the brief or reference image
- White or transparent-looking background
- Clean vector-style logo, professional branding, centered composition
- Avoid mockup scenes, extra objects, watermarks, and tiny unreadable text

Suggested filenames:

```text
logo_01_wordmark.png
logo_02_lettermark.png
logo_03_symbol.png
logo_04_combination.png
logo_05_emblem.png
logo_06_geometric.png
logo_07_organic.png
logo_08_dynamic.png
logo_09_heritage.png
```

After generation, show the separate images and ask the user to choose one logo number for refinement.

## Stage 2: Generate 9 Variations

When the user selects a logo, keep the chosen concept type and brand personality while varying one axis per image:

| ID | Variation | Direction |
| --- | --- | --- |
| A | Typography | Change font family or lettering character |
| B | Color | Adjust palette, accent color, or monochrome treatment |
| C | Proportion | Change symbol-to-text ratio or horizontal/vertical layout |
| D | Weight | Change stroke thickness, boldness, or visual density |
| E | Inverted | Adapt for dark or brand-color background |
| F | Texture | Add subtle premium, print, gradient, embossed, or craft texture |
| G | Symbol Detail | Refine symbol geometry, negative space, or internal detail |
| H | Lockup | Create alternate stacked, horizontal, or badge lockup |
| I | Refined | Make the mark more premium, simple, and production-ready |

Suggested filenames:

```text
variation_A_typography.png
variation_B_color.png
variation_C_proportion.png
variation_D_weight.png
variation_E_invert.png
variation_F_texture.png
variation_G_symbol_detail.png
variation_H_lockup.png
variation_I_refined.png
```

After generation, show the separate images and ask the user to select the final variation.

## Stage 3: Recommend And Generate Mockups

After the final logo is selected, recommend six to ten mockup options based on the brand description, target audience, sales channel, desired mood, and logo type. Do not force the same mockups on every brand.

Examples:

- Cafe, dessert, food: cup sleeve, takeout cup, package box, menu board, apron, storefront sign
- Beauty, fashion: cosmetic container, shopping bag, clothing label, perfume package, SNS profile, store sign
- Tech, SaaS, app: app icon, website hero, login screen, business card, laptop sticker
- Premium B2B: business card, proposal cover, envelope, conference banner, pen and notebook set
- Kids, family: product package, sticker set, tote bag, character tag, SNS banner
- Eco, lifestyle: kraft shopping bag, recycled package, label sticker, tumbler, fabric tag

Ask the user which mockups to create. Generate only the selected mockups as separate images.

Suggested filename pattern:

```text
mockup_01_takeout_cup.png
mockup_02_package_box.png
```

## Stage 4: Brand Guidelines

Create a concise brand guideline document after the final logo and mockups are ready. If a `.docx` is requested or useful, use document-generation tooling available in the current environment; otherwise create a well-structured Markdown document.

Include:

1. Brand overview: name, meaning, positioning
2. Logo system: selected logo, minimum size, clear space, misuse examples
3. Color system: main color, RGB or HEX values, two to three supporting colors, usage ratio
4. Typography: headline font style, body font style, digital vs print guidance
5. Tone and voice: five communication keywords, OK and NG wording examples
6. Application guide: digital, print, packaging, signage, or product usage

Suggested filename:

```text
[brand-name]_Brand_Guidelines.docx
```

## Progress Reporting

Keep the user updated during long generation runs:

```text
Logo 1/9 generating: Wordmark
Variation A/9 generating: Typography
Mockup 1/3 generating: Takeout cup
```

Final response should summarize:

- Nine original logo assets
- Nine variation assets for the selected concept
- Mockup assets created
- Brand guideline document path
- Any assumptions or failed/retried generations

## Failure Handling

- If one image generation fails, retry that item once and continue with the rest.
- If reference image analysis is unavailable, continue from the text brief and clearly state that limitation.
- If brand guideline document creation fails, provide the guideline content in Markdown and mention the document failure.
