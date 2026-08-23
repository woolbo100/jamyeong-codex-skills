---
name: funding-detail-page
description: Use when the user wants to make, plan, improve, or generate a Korean funding-style detail page for knowledge commerce, digital products, classes, coaching, memberships, ebooks, communities, or creator-led launches, including phrases like "펀딩 상세페이지", "와디즈 상세페이지", "지식창업 상세페이지", "강의 상세페이지", "전자책 펀딩", or "클래스 런칭 페이지". Produces mobile-first image cut plans, Korean launch copy, founder-story flow, proof/risk-reversal sections, funding reward composition, ASCII wireframes, style choices, compliance checks, and sales-ready image cuts. Ask one choice-based question at a time, treat proof and claims carefully, plan before image generation, and render approved Korean copy inside final images with the image-generation model.
---

# Funding Detail Page

## Overview

Use this skill to turn a knowledge-commerce offer into a mobile-first funding-style detail page plan. The output is not a generic product page or a long sales letter; it is a production-ready image sequence for a funding, preorder, waitlist, class launch, cohort recruitment, ebook launch, membership, or creator-led educational offer.

This skill preserves the basic workflow of `ecommerce-detail-page` while changing the persuasion model from product-commerce to funding-style knowledge entrepreneurship:

- sell the transformation before the curriculum
- introduce the creator/founder as the trust anchor
- prove demand and credibility without inventing results
- explain the problem, new opportunity, method, curriculum, reward, scarcity, refund/risk-reversal, and CTA
- keep every cut mobile-first and image-production-ready

## Audience Context

This skill is intended for Jamyung School students and internal educational use. Do not add AI Sync Club promotional links, community links, or unrelated creator branding to user-facing responses or generated page copy unless the user explicitly asks for them.

## Reference Inspiration

When the user asks for a Redpeople-style or Korean knowledge-startup funding page, use the pattern as inspiration, not as text to copy. The observed structure includes:

- bold social proof and review-first trust building
- ordinary-person-to-transformation narrative
- founder backstory and mission
- repeated belief framing around knowledge, execution, and economic freedom
- offer stack with classes, membership, VOD, documents, mentoring, and community
- urgency through early-bird, limited quantity, coupon, or application deadline when those facts are true
- final identity-based CTA, such as joining a group of people pursuing a specific future

Do not copy brand names, personal stories, exact claims, numbers, testimonials, refund promises, rankings, or designs from the reference site unless the user owns them and explicitly provides permission and source facts.

## How To Start

Trigger this skill when the user asks for:

```text
펀딩 상세페이지 만들어줘
지식창업 상세페이지 제작
와디즈용 강의 상세페이지 기획
전자책 펀딩 페이지 이미지 컷 구성
클래스 런칭 상세페이지 추천으로
레드피플 같은 지식창업 상세페이지
```

Recommended first-turn handling:

- If the user provides creator photos, screenshots, reviews, curriculum images, sales/funding screenshots, or product mockups, analyze them before planning.
- If the user gives only an offer name or category, infer a recommended offer category, target backer, style, and cut count, then mark assumptions clearly.
- If the user says `추천으로`, use recommended defaults instead of asking every optional question.
- Do not make platform mandatory. Use generic mobile funding detail page unless the user mentions Wadiz, Tumblbug, Smart Store, Gumroad, class platform, own landing page, or ad funnel.
- Always plan first, then ask whether to generate images or revise.

Default recommended settings when the user gives minimal input:

| Item | Default |
|---|---|
| Page style | `problem-story-proof-offer` from `references/funding-style-templates.md` |
| Cut count | 15 cuts |
| Platform | Channel-neutral mobile funding/launch page |
| Proof and claims | Use only provided facts; mark missing fields as `확인 필요` |
| Image production | One image per cut, maximum available parallel agents/jobs |

## Non-Negotiables

- Ask intake questions one at a time, and always show explicit choices for the current question.
- Prefer Codex's internal choice UI when available. If it is unavailable, fall back to visible text choices such as A/B/C.
- At the beginning, check whether the user has visual assets, proof assets, or product/creator materials.
- If assets are provided, analyze them before planning. Identify creator image quality, screenshots, review credibility, product mockup usability, text-safe spaces, crop opportunities, visual tone, strengths, defects, and which cuts each asset should support.
- If key proof assets are weak, unverifiable, cropped, blurry, or legally risky, mark them as `검증 필요` or `재제작 권장` instead of using them as definitive proof.
- For true sales-ready final images, request enough offer facts: offer name, creator/brand name, target learner, curriculum or modules, delivery format, access period, reward tiers, pricing or early-bird facts, schedule, refund policy, community/support details, reviews or proof sources, and cautions.
- If proof, creator identity, curriculum, pricing, or policy facts are missing, final image output can only be a `펀딩용 초안` or `컨셉 기획`, not a fully production-ready funding page.
- Never invent revenue, ranking, student count, review count, funding amount, success rate, refund guarantee, certification, legal qualification, case study, countdown, limited quantity, or deadline.
- Avoid exaggerated or risky claims such as `무조건`, `100%`, `보장`, `확실히`, `누구나 월 1억`, `한 달 만에 성공`, `No.1`, `완전 자동수익`, `환불 보장` unless exact source facts and policy wording are provided.
- For money-making, investment, career, education, health, psychology, law, tax, or business coaching offers, include a compliance note before publishing.
- For funding-style pages, do not lead with seller bragging alone. Start with the backer's pain, desired future, belief shift, or opportunity, then earn trust with proof and founder context.
- Ask the user to choose a funding detail-page style template before cut planning. Use [funding-style-templates.md](references/funding-style-templates.md), mark recommended styles with `(추천)`, and adapt copy density, layout, and image prompts to the chosen style.
- Do not create or request actual images first. First create the strategy and cut plan, show cut-by-cut copy, image composition, and ASCII layout wireframes, then ask whether to generate images or revise.
- Do not include final image-generation prompts in the planning output. Use ASCII wireframes to show text position, proof placement, creator/product visual, reward block, CTA, and section structure.
- Planning-stage ASCII wireframes are only for approval. Final image production must render the approved Korean copy directly inside each image like a real mobile funding detail page.
- Final image production must use the image-generation model as the production tool, including Korean text inside the image. Do not switch to deterministic text overlay, SVG/Sharp, or manual post-processing unless the user explicitly asks for that workflow.
- If Korean text inside final images is missing, broken, unreadable, replaced with English, or materially different from the approved copy, treat the image as failed and regenerate it with stricter prompts.
- If image generation starts, generate exactly the planned cut count. Never collapse all cuts into one tall image unless the user explicitly asks for a combined mockup.
- Image production must use maximum available parallel agents/jobs by default. Split the approved plan into independent `cut-01` through `cut-N` jobs, launch all possible workers before waiting, then collect and QA all outputs.
- After all cut images are complete, build an HTML review/download page that shows images sequentially and provides per-cut downloads plus a `전체 다운로드` button when local image files are available.
- Generated images must pass Korean text QA: approved copy present, readable, not broken, not translated, not replaced, and aligned with verified facts.

## Intake Flow

Collect missing inputs one question at a time. Never show the whole questionnaire at once. Every question must display explicit choices.

If the user has already provided an item, fill it in and skip that question. If the user provides multiple answers at once, record them and ask the next unresolved question only.

### Question 1: Assets

Always start by checking whether offer assets exist unless assets are already attached.

```text
펀딩 상세페이지에 쓸 자료가 있나요?

A. 있음, 첨부한 자료를 기준으로 제작
B. 있음, 곧 첨부할 예정
C. 없음, 상품명/아이디어 기준으로 제작
```

Useful assets include:

- creator/founder photos
- ebook cover, VOD thumbnail, curriculum screenshots, community screenshots
- reviews, testimonials, funding/sales screenshots, press or ranking evidence
- logo, brand colors, product mockup, curriculum table
- refund policy, delivery schedule, FAQ, reward tier information

If assets are provided, read [asset-analysis.md](references/asset-analysis.md) and produce a short `자료 분석 및 배치 추천` section before the cut plan.

If proof assets are risky or weak, ask before final image generation:

```text
제공된 자료 중 일부는 펀딩 상세페이지에 그대로 쓰기에는 검증/가독성/품질 이슈가 있습니다. 어떻게 진행할까요?

A. 자료는 참고만 하고 안전한 표현으로 재구성 (추천)
B. 더 좋은 원본 자료를 추가한 뒤 다시 기획
C. 현재 자료를 그대로 쓰되 펀딩용 초안으로 표시
```

### Question 2: Progress Mode

```text
펀딩 상세페이지 제작 방식부터 고르겠습니다.

A. 아이템명만 입력하고 추천 가정으로 기획안 만들기
B. 항목을 하나씩 선택해서 정확하게 만들기

답변 예시: A / 아이템명: AI 자동화 전자책
```

If the user chooses A and gives an item name, use the Item-Name-Only Fast Path. If not, ask only:

```text
아이템명을 알려주세요.

A. 아이템명 입력
B. 아직 아이템명이 정해지지 않음
```

### Question 3: Offer Category

```text
펀딩/지식상품 유형을 골라주세요.

A. 전자책/PDF
B. VOD 강의
C. 라이브 클래스/코호트
D. 1:1 코칭/컨설팅
E. 커뮤니티/멤버십
F. 템플릿/자동화 파일
G. 챌린지/습관 프로그램
H. 패키지 번들
I. 기타/직접 입력
```

### Question 4: Offer Name and Core Promise

```text
아이템명과 핵심 약속을 알려주세요.

A. 아이템명만 입력
B. 아이템명 + 핵심 약속 1~3개 입력
C. 아직 미정, 추천 가정으로 진행
```

After an offer category or item name is known, infer likely backer segments and purchase anxieties before asking the target question.

### Question 5: Main Backer

```text
주요 후원자/구매자를 골라주세요.

A. 초보자/첫 시작 고객 (추천 가능)
B. 부업·수익화 관심 고객 (추천 가능)
C. 업무 자동화/생산성 고객
D. 창업·퍼스널브랜딩 고객
E. 이미 해봤지만 성과가 막힌 고객
F. 고급 전략/멘토링이 필요한 고객
G. 커뮤니티와 동기부여가 필요한 고객
H. 기타/직접 입력
I. 추천 가정으로 진행
```

### Optional Question: Platform

Ask this only when platform-specific constraints matter or the user mentions a platform.

```text
펀딩/판매 채널까지 맞춰서 구성할까요?

A. 와디즈 기준
B. 텀블벅 기준
C. 클래스/강의 플랫폼 기준
D. 자사몰/브랜드몰 기준
E. 광고 랜딩/신청서 전환 기준
F. 채널 무관 모바일 펀딩 상세페이지 (추천)
G. 기타/직접 입력
```

### Question 6: Funding Page Style

Read [funding-style-templates.md](references/funding-style-templates.md), then ask:

```text
펀딩 상세페이지 스타일을 골라주세요.

A. 문제공감-해결책 설득형 (추천 가능)
B. 창업자 스토리/미션형
C. 후기·성과 근거 집중형
D. 커리큘럼/로드맵 정보형
E. 얼리버드/혜택 전환형
F. 프리미엄 코칭/고단가형
G. 커뮤니티 합류/정체성형
H. 추천 스타일로 진행
```

### Question 7: Cut Count

```text
상세페이지 컷 수를 골라주세요.

A. 8컷 티저형
B. 15컷 기본 펀딩형
C. 20컷 고관여 설득형
D. 추천 가정으로 진행 (기본 15컷)
```

If the user selects a cut count, output exactly that many cuts.

### Question 8: Required Facts

```text
반드시 넣어야 할 사실 정보가 있나요?

A. 커리큘럼/목차/제공 구성 있음
B. 가격/얼리버드/리워드 정보 있음
C. 후기/성과/수치 근거 있음
D. 일정/제공 방식/환불 정책 있음
E. 없음, 확인 필요로 표시
F. 직접 입력
```

## Item-Name-Only Fast Path

When only an item name is available:

1. Infer the likely offer category from the item name.
2. Infer likely backers, pain points, desired future, and objections; mark them as assumptions.
3. Use `채널 무관 모바일 펀딩 상세페이지` unless platform-specific context was provided.
4. Recommend a style from [funding-style-templates.md](references/funding-style-templates.md) and mark it as an assumption.
5. Choose exactly 15 cuts by default unless the user selected another exact count.
6. State assumptions at the top and include `확인 필요` fields inside relevant cuts.
7. Do not invent proof. Use neutral placeholders such as `확인 필요: 후기`, `확인 필요: 커리큘럼`, `확인 필요: 리워드 가격`, `확인 필요: 환불 정책`.

## Planning Before Image Production

Planning stage:

1. Produce the funding detail-page plan: context summary, backer insight, core promise, offer positioning, cut-by-cut copy, image composition, ASCII layout, tone, compliance checklist.
2. Planning output must not include final image-generation prompts.
3. ASCII wireframes are design blueprints only.
4. After the cut plan, ask:

```text
다음 단계로 어떻게 진행할까요?

A. 이 기획안 그대로 이미지 생성
B. 컷별 카피/구성 수정
C. 자료 또는 사실 정보 추가 후 다시 기획
```

Production stage:

1. Treat the approved plan as the source of truth.
2. Generate sales-ready images cut by cut using the image-generation model.
3. Include the approved Korean text inside each image.
4. If proof or screenshots are weak, use them only as references and rewrite claims safely.
5. Generate exactly the planned number of separate images.
6. Use maximum parallel agents/jobs when available.
7. Build an HTML gallery/download page after generation when local files exist.
8. Run Korean text QA and regenerate failed cuts only.

## Workflow

1. Confirm or infer offer category and product context.
2. Ask one unresolved intake question at a time.
3. Check whether visual/proof assets exist. If provided, analyze them using [asset-analysis.md](references/asset-analysis.md).
4. Once category or item name is known, infer likely backers and objections.
5. Treat platform as optional unless needed.
6. Read [funding-style-templates.md](references/funding-style-templates.md) before recommending a style.
7. Choose cut count: 8 for a teaser, 15 for a standard funding page, 20 for a high-consideration launch.
8. Use [funding-cut-structure.md](references/funding-cut-structure.md) to build the flow.
9. Use [funding-output-template.md](references/funding-output-template.md) for each cut.
10. Run [funding-compliance.md](references/funding-compliance.md) before publishing.
11. Ask whether to generate images or revise before image production.

## Output Contract

Final planning answers must be in Korean and follow this structure:

1. `# [아이템명] 펀딩 상세페이지 이미지 기획안`
2. `## 1. 카테고리 및 펀딩 맥락 요약`
3. `## 2. 자료 분석 및 배치 추천` if assets were provided
4. `## 3. 후원자 인사이트와 핵심 전략`
5. `## 4. 이미지 컷별 제작안`
6. `## 5. 전체 디자인 톤앤매너`
7. `## 6. 준법·품질 체크`

Each cut must include:

- 목적
- 후원자 심리
- 헤드라인
- 서브카피
- 이미지 내 삽입 문구
- 이미지 구성
- 자료 배치 추천
- 자료 품질 판단
- ASCII 레이아웃
- 사실 정보
- 사용 자료
- 디자인 메모
- 최종 이미지 QA
- 확인 필요

## Completion Check

Before answering, verify:

- Offer category was confirmed or explicitly marked as assumed.
- The page addresses backer pain, desired transformation, objections, proof needs, reward clarity, and risk reversal.
- The cut flow moves from hook to problem, opportunity, founder story, method, curriculum, proof, reward, FAQ, policy, urgency, and CTA.
- The number of cuts exactly matches the selected cut count.
- The selected style template is visible in the plan.
- If assets were provided, the plan includes analysis and per-cut placement recommendations.
- Every claim is either provided fact, clearly marked assumption, or `확인 필요`.
- Risky income, outcome, ranking, refund, deadline, and scarcity claims were removed or marked as needing proof.
- Planning output uses ASCII wireframes rather than image-generation prompts.
- Final generated images include approved Korean text inside the image.
- Final generated images pass Korean text QA.
- Generated image files are collected into a sequential HTML gallery when local files are available.
