# 비주얼 설계 시스템

## 이미지 세트

각 이미지 프롬프트에 책 제목, 핵심 감정, 독자, 프리셋, 공통 팔레트, 재질, 조명, 반복 상징을 적는다. 세트 전체에 동일한 아트디렉션 문장을 복사해 일관성을 유지한다.

### 표지

- 세로 2:3 또는 최종 판형 비율, 상단 25~35%에 제목 텍스트 영역
- 하단 12~18%에 저자명과 출판사 텍스트 영역
- 한 개의 강한 상징과 명확한 초점
- 작은 썸네일에서도 실루엣이 읽히는 단순한 구성
- 표지 프롬프트에는 책 제목, 저자명, 출판사명을 실제 텍스트로 넣도록 명시한다. 정확한 한글 렌더링이 중요하므로 생성 후 반드시 오탈자와 글자 깨짐을 확인하고, 실패하면 무문자 표지 이미지 위에 Word/Canva에서 텍스트를 얹는 방식으로 보정한다.

### 판권 배경

- 같은 팔레트의 매우 낮은 대비, 넓은 중앙 여백
- 정보 가독성을 해치는 얼굴·강한 패턴·고대비 요소 금지
- 불투명도 8~18%로 사용 가능한 종이 질감 또는 모서리 장식

### 장 오프너

- 각 장의 핵심 감정을 서로 다른 상징으로 표현
- 세트 전체의 렌즈, 질감, 광원, 인물 스타일은 고정
- 제목을 얹을 안전 영역 30% 이상

## 프리셋

### warm-editorial

아이보리, 웜그레이, 테라코타 포인트, 자연광, 고급 종이 질감, 절제된 에디토리얼 사진/일러스트.

### baekdohwa-luxury

딥 버건디, 블랙, 샴페인 골드, 진주·자개·한지 질감, 영화적인 명암, 성숙하고 신비로운 여성성. 선정적 표현보다 권위와 자기주도성을 강조한다.

### lumora-healing

라벤더, 더스티 로즈, 크림, 은은한 금빛, 새벽 안개와 부드러운 빛 입자, 심리 치유와 내면 성장을 상징하는 서정적 이미지.

## 공통 프롬프트 골격

```text
Use case: Korean ebook [cover/copyright background/chapter opener]
Book concept: [한 문장 약속]
Scene and symbol: [핵심 장면/상징]
Art direction: [프리셋 + 공통 팔레트/재질/조명]
Composition: portrait, [텍스트/본문]을 위한 clean negative space [위치], restrained details
Audience and mood: [독자], [감정]
Consistency key: [세트 전체에 반복할 상징·렌즈·광원]
Constraints: no text, no letters, no typography, no logo, no watermark, no frame, no clutter
```

표지에는 위 골격의 `Constraints` 대신 다음 텍스트 지시를 사용한다:

```text
Cover text: exact Korean title at top: "[제목]"; author and publisher at bottom: "[저자명] · [출판사명]"; clean readable typography, no extra letters, no watermark, no fake logo
```

실제 인물 레퍼런스가 있으면 사용 전 이미지를 확인하고, 변경하지 말아야 할 정체성 요소를 프롬프트에 명시한다.
