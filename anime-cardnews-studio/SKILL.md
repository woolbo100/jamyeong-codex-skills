---
name: anime-cardnews-studio
description: Turn an uploaded person photo into a consistent cute chibi or SD animated character and plan and generate an Instagram carousel with selectable background colors, optimized card order, concise Korean copy, and card-by-card images. Use for portrait-based card news or social carousel creation; do not use for simple one-off portrait edits without a carousel.
---

# Anime Cardnews Studio

Create a coherent Instagram carousel in which the same recognizable animated character appears across cards. Treat planning, copy, character consistency, and visual generation as one workflow.

## Gather only material inputs

Proceed immediately when enough information is present. Otherwise ask in one compact message for only the missing items:

- person photo (required for portrait-based character work)
- topic or source content
- background color: a named color, hex code, palette, or `recommend`
- optional: audience, goal, card count, ratio, character style, brand colors, CTA

If the user gives no card count, recommend 6–8 cards based on content density. Default to Instagram portrait 4:5 (1080×1350). Use 1:1 only when requested. If the user says `recommend` for color, offer three suitable palette options with hex codes and continue after their selection when that choice would materially change the design.

Never infer sensitive personal traits from the photo. Preserve recognizable, non-sensitive features such as face shape, hairstyle, glasses, and clothing cues without exaggerating age, body, ethnicity, or disability.

## Plan before generating

Identify the carousel goal as educational, story, promotional, checklist, or mixed. Read [references/carousel-structures.md](references/carousel-structures.md) and choose the closest structure. Adapt the number of cards to the message rather than padding it.

Present a compact production table before image generation. Separate the large headline from the smaller body copy so every card has enough substance to stand alone:

| Card | Role | Headline | Small body copy | Character action/expression | Visual cue |
| --- | --- | --- | --- | --- | --- |

Copy rules:

- One main idea per card.
- Cover: one strong promise, tension, or curiosity hook; usually 8–18 Korean characters.
- Interior headline: usually no more than two short lines.
- Small body copy: include 1–3 short lines on each interior card whenever the user asks for card news, not only titles. Keep it readable at mobile size; shorten the idea rather than shrinking type below a legible size.
- Move only overflow, examples, or nuance into the caption. Do not omit body copy unless the card is intentionally title-only, such as a cover or divider.
- Final card: one clear CTA appropriate to the goal.
- Keep Korean natural and specific. Avoid empty hype, repetitive headings, and unverified numerical claims.

If the user asked to make the carousel, the plan is an intermediate checkpoint, not the final deliverable. Continue to image generation without asking for confirmation unless a required choice is unresolved.

## Lock the character and art direction

Inspect the uploaded photo before editing. Build an internal character lock containing:

- face silhouette and key facial cues
- hairstyle and hair color
- signature accessory or clothing cue
- character treatment (default: polished adult chibi/SD illustration, about 2.5–3 heads tall)
- line weight, shading, eye treatment, and expression range

Use the source photo as an identity reference, not as a composition to copy. Keep the same character design, palette, and rendering style on every card. Vary pose, expression, props, and framing to support each card’s message.

### Default chibi direction

Unless the user selects another style, use a cute but credible adult chibi character:

- slightly oversized head, compact body, soft rounded shapes, and lively facial expressions
- preserve the adult subject’s recognizable hairstyle, face cues, glasses, accessories, and signature outfit
- bright, friendly eyes without making them disproportionately huge
- clean 2D linework, gentle cel shading, polished editorial finish, and simple expressive gestures
- attractive enough for a professional personal brand, instructor, expert, or business account

Avoid toddler-like proportions, baby clothes, excessive doll features, hypersexualization, overly childish poses, or a generic face that loses the person’s identity. If the user requests a stronger chibi look, move toward 2–2.5 heads tall; if they request a more professional look, use 3–3.5 heads tall while retaining the cute facial treatment.

Create a palette lock from the selected background color:

- primary background
- lighter and darker companion shades
- high-contrast text color
- one accent color

Create a layout lock before generating the first card and repeat it in every card prompt:

- shared canvas ratio and safe margins
- repeated border, grid, panel, or background motif
- fixed headline zone and small-body text zone
- fixed typography direction for headline, body, badges, and card numbers
- consistent character rendering, clothing cues, scale range, and outline treatment
- consistent palette roles, such as background, headline, body text, accent, and icon glow

Maintain legible contrast. Do not place important text or facial features near crop edges. Keep a consistent text-safe area and repeatable hierarchy across the set. Variation should come from pose, expression, props, and card-specific icons rather than changing the whole design system.

## Generate the carousel

Use the image generation/editing capability with the uploaded photo included as a reference. Generate each card as a separate image, in order. Include the full shared art-direction lock and the card-specific content in every generation request; do not rely on the model remembering visual details between calls.

Preferred generation strategy:

1. Generate a clean character-led background/composition with intentional text space for both a headline and small body copy.
2. Include Korean headline and short body copy in the image only when the generator can reproduce both reliably.
3. If body text is misspelled, malformed, too small, or unreadable, regenerate once with shorter body copy and stronger text panels; if still unreliable, generate the art with reserved text areas and clearly provide the exact overlay copy and placement specification.

For every card prompt specify:

- exact dimensions and aspect ratio
- locked character description and reference image
- chibi proportion target and the instruction to keep an adult identity
- locked palette with hex codes
- locked layout system, including headline zone, body text zone, border style, background motif, and typography hierarchy
- card purpose and emotional beat
- pose, expression, framing, props, and background elements
- exact headline and exact small body copy, or reserved text areas for both
- consistent typography direction and margins
- exclusions: no watermark, no extra fingers/limbs, no duplicate person, no random letters, no unintended logo

Cover cards should prioritize stopping power and clarity, but may include a short subtitle when helpful. Interior cards should prioritize reading rhythm: headline first, then a concise body block that explains the card's point. The final card should feel conclusive and leave room for the CTA.

## Quality check and delivery

Check the full set, not only individual cards:

- same person is recognizable as the same animated character
- hook and sequence make sense without the caption
- no duplicated message or missing logical step
- background color and accents remain consistent
- layout system, border treatment, typography hierarchy, and card numbering feel like one designed set
- each interior card includes readable small body copy, not only a title
- readable mobile-size hierarchy and contrast
- Korean spelling, card numbering, and CTA are correct
- no unsafe crop, distorted anatomy, watermark, or accidental text

Regenerate only failed cards while retaining the lock. Deliver images in card order and include:

- the final card table
- suggested Instagram caption
- 5–10 relevant hashtags, avoiding spammy repetition
- optional alt text for accessibility

Do not claim that images were generated if only prompts or a plan were produced.
