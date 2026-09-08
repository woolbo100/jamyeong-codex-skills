# Remotion 구현 가이드

Remotion 프로젝트를 만들거나 수정할 때 이 기준을 사용한다.

## 기술 기본값

- 프레임워크: Remotion, React, TypeScript
- FPS: `30`
- 기본 길이: `15s`
- 외부 의존성을 추가하기 전에 Remotion 기본 기능과 헬퍼 함수를 우선한다.
- 외부 의존성은 최소화한다.
- 수정 가능한 영상 콘텐츠는 컴포넌트 곳곳이 아니라 데이터 파일에 둔다.

## 해상도 기본값

- `9:16`: `1080x1920`
- `16:9`: `1920x1080`
- `1:1`: `1080x1080`

초 단위 길이는 프레임으로 계산한다.

```ts
const fps = 30;
const durationInFrames = seconds * fps;
```

## 권장 프로젝트 구조

```text
project-root/
  src/
    Root.tsx
    compositions/
      MainVideo.tsx
    components/
      AnimatedCard.tsx
      AnimatedText.tsx
      BackgroundScene.tsx
      CTAButton.tsx
      DividerLine.tsx
      LogoLockup.tsx
      SceneFrame.tsx
    data/
      content.ts
    styles/
      tokens.ts
    utils/
      motion.ts
      timing.ts
  public/
    images/
    audio/
  package.json
  remotion.config.ts
  tsconfig.json
  README.md
```

기존 프로젝트가 있으면 그 구조를 우선하고, 새 프로젝트일 때만 이 구조를 기본으로 삼는다.

## 구현 규칙

- `content.ts`에 제목, 부제, CTA, 장면 카피, 브랜드명, 타이밍을 둔다.
- `tokens.ts`에 색상, 타이포그래피, 간격, radius, shadow를 둔다.
- `motion.ts`에 재사용 가능한 interpolation 헬퍼를 둔다.
- `timing.ts`에 장면별 프레임 범위를 둔다.
- 장면 컴포넌트는 단순하고 읽기 쉽게 유지한다.
- 반복 값은 장면 안에 하드코딩하지 않는다.
- 초보자가 애니메이션 코드를 깊게 이해하지 않아도 텍스트를 바꿀 수 있게 만든다.

## 애니메이션 기준

텍스트 등장:

- opacity와 `translateY`를 함께 사용한다.
- 주요 제목은 대략 `8-18`프레임에 걸쳐 등장시킨다.
- 보조 텍스트는 `4-10`프레임 간격으로 스태거한다.

카드와 패널:

- `20-40px` 정도의 미세한 이동감을 사용한다.
- 깊이감이 필요할 때만 약한 scale을 더한다.
- shadow는 절제한다.

라인과 디바이더:

- width expansion 또는 masked reveal을 사용한다.
- 라인은 얇게 유지한다.

CTA:

- 마지막 `1-2s`에 안정적으로 등장시킨다.
- 요청이 없으면 pulsing, shaking, 반복 주목 효과를 피한다.

배경:

- 영상이 정적으로 느껴지지 않도록 아주 은은한 움직임을 둔다.
- 텍스트 가독성을 위해 대비를 충분히 유지한다.

## 렌더 명령

일반적인 명령:

```bash
npm install
npm run dev
npm run render
```

기존 프로젝트가 사용하는 패키지 매니저가 있으면 그것을 따른다. 새 프로젝트라면 사용자가 달리 요청하지 않는 한 npm을 사용한다.

## 검증

가능하면 로컬 preview 또는 render를 실행한다. 렌더링 비용이 크거나 실행할 수 없으면 최소한 타입 체크나 빌드 명령을 실행하고 무엇을 검증했는지 명확히 보고한다.
