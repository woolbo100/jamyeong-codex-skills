# jamyeong-codex-skills

Version: v1.0.0

`ebook-studio` is a Codex skill for planning and producing Korean ebooks from a topic, outline, or draft. It helps with editorial structure, manuscript writing, editable Word output, cover direction, copyright-page background imagery, and chapter opener image planning.

## 주요 기능

- 주제 입력을 바탕으로 제목, 부제, 독자 정의, 한 문장 약속, 목차 설계
- 한국어 전자책 원고 작성과 장별 학습 목표 구성
- 사례, 자기점검, 실천 박스, 체크리스트가 포함된 본문 구조화
- 표지, 판권 배경, 장별 오프너 이미지를 위한 통일된 아트디렉션
- `book.json` 입력을 편집 가능한 `.docx` 파일로 변환하는 빌드 스크립트
- Word 스타일 기반 제목, 본문, 인용, 실천 박스, 자동 목차 안내 생성

## 저장소 구조

```text
ebook-studio/
|-- SKILL.md
|-- agents/
|-- assets/
|-- references/
|-- scripts/
`-- templates/
```

## 설치 방법

Codex 스킬 폴더에 이 저장소의 `ebook-studio` 폴더를 복사합니다.

```powershell
git clone https://github.com/woolbo100/jamyeong-codex-skills.git
Copy-Item -Recurse -Force .\ebook-studio\ebook-studio "$env:USERPROFILE\.codex\skills\ebook-studio"
```

macOS 또는 Linux에서는 다음처럼 복사할 수 있습니다.

```bash
git clone https://github.com/woolbo100/jamyeong-codex-skills.git
mkdir -p ~/.codex/skills
cp -R ebook-studio/ebook-studio ~/.codex/skills/ebook-studio
```

설치 후 새 Codex 작업에서 `$ebook-studio`로 호출할 수 있습니다.

## 사용 예시

```text
Use $ebook-studio to create a Korean lead-magnet ebook for beginner freelancers about pricing their services. Include a practical workbook style, 6 chapters, warm editorial visuals, and an editable Word file.
```

```text
$ebook-studio
관계에서 나를 잃지 않는 법을 주제로 7장짜리 한국어 전자책을 만들어줘. 표지는 제목을 상단에, 저자와 출판사를 하단에 넣어줘.
```

## DOCX 빌드

`ebook-studio/scripts/build_ebook.py`는 `python-docx`가 필요합니다.

```bash
python ebook-studio/scripts/build_ebook.py book.json output.docx
```

입력 스키마는 `ebook-studio/references/book-schema.md`를 참고하고, 시작 템플릿은 `ebook-studio/templates/book-template.json` 또는 `ebook-studio/assets/book-template.json`을 사용할 수 있습니다.

## 라이선스

MIT License. 자세한 내용은 [LICENSE](LICENSE)를 확인하세요.
