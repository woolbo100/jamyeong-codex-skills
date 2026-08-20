---
name: homepage-brief-to-site
description: Guide users through a homepage planning worksheet, convert answers into a design brief, then build a polished homepage using design-taste-frontend.
---

# Homepage Brief To Site

Use this skill when the user wants to create, redesign, or brief a homepage and needs a guided intake before implementation.

## Core Workflow

1. Start with the worksheet before proposing a design or writing code. Read [references/worksheet.md](references/worksheet.md), then ask the user to fill it out. If the user already supplied enough information, silently map it into the worksheet and ask only for the most important missing items.
2. Convert the completed worksheet into a concise homepage brief:
   - project type and business goal
   - target audience and primary conversion
   - required sections and content assets
   - brand constraints and reference sites
   - design concept, tone, and interaction level
   - technical stack, deployment expectations, and success checks
3. For implementation, also use `design-taste-frontend`. State the one-line design read and dial values required by that skill before coding.
4. Build the homepage as the first screen of the product or site, not a generic landing-page explanation about what could be built.
5. Verify the result in desktop and mobile viewports. Check visual fit, responsive behavior, contrast, image rendering, and copy quality before final delivery.

## Intake Rules

- Keep the worksheet friendly and practical. Users should be able to answer in natural language, bullets, or partial notes.
- Do not force every field to be filled. Mark unknowns as assumptions when they are low risk.
- Ask follow-up questions only when missing information changes the site structure, brand direction, or conversion path.
- For personal homepages, portfolios, experts, clinics, local businesses, stores, and service brands, tailor the worksheet wording to that user's domain.
- If the user writes in Korean, present the worksheet in Korean and preserve Korean homepage copy direction unless they ask for another language.

## Design And Build Rules

- Use the worksheet to avoid generic content. Do not invent fake testimonials, metrics, client logos, credentials, pricing, or claims.
- If real images, logos, product photos, or profile photos are missing, use the best available image workflow and clearly note any placeholder placements.
- Prefer existing project conventions when working inside a codebase. For a new project, choose a simple, maintainable stack that can be locally run and verified.
- Treat SEO basics as part of the homepage brief: page title, meta description, social preview, headings, and meaningful section order.
- When redesigning an existing homepage, audit existing IA, copy, SEO-sensitive routes, brand assets, and conversion elements before changing structure.

## Output Expectations

When the user is still in planning mode, return the worksheet or the synthesized brief. When they ask to build, implement the page, run available checks, start a local server when appropriate, and report the URL or deliverable path.
