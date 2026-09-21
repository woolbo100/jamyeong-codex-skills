# book.json 스키마

```json
{
  "meta": {"title":"책 제목","subtitle":"부제","author":"저자명","brand":"브랜드","publisher":"출판사","publication_date":"2026-08-19","isbn":"","contact":"","copyright":"Copyright © 2026 저자명. All rights reserved.","disclaimer":""},
  "design": {"page":"A5","accent":"#7C5AA6","text":"#2C2630","muted":"#F2ECF6","font":"Malgun Gothic","cover_image":"images/cover.png","copyright_background":"images/copyright.png"},
  "front_matter": [{"type":"heading","text":"프롤로그"},{"type":"paragraph","text":"본문"},{"type":"quote","text":"강조 문장"}],
  "chapters": [{"number":1,"title":"장 제목","subtitle":"장 부제","image":"images/ch01.png","blocks":[{"type":"heading","level":2,"text":"소제목"},{"type":"paragraph","text":"본문"},{"type":"quote","text":"핵심 문장"},{"type":"callout","title":"실천","text":"오늘 해볼 일"},{"type":"checklist","title":"점검","items":["항목 1","항목 2"]},{"type":"page_break"}]}],
  "back_matter": [{"type":"heading","text":"에필로그"},{"type":"paragraph","text":"본문"}]
}
```

지원 블록은 `paragraph`, `heading`, `quote`, `callout`, `checklist`, `bullets`, `page_break`다. 이미지 경로는 JSON 파일 기준 상대경로 또는 절대경로다. 존재하지 않는 선택 이미지는 건너뛰며 본문은 계속 생성한다.
