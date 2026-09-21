const fs = require("fs");
const path = require("path");

const outDir = path.resolve(__dirname, "..", "assets");
fs.mkdirSync(outDir, { recursive: true });

const C = {
  purple: "#36204F",
  plum: "#5A347A",
  lavender: "#B99BE7",
  ivory: "#F7F1E8",
  paper: "#FFFDF8",
  charcoal: "#242128",
  warmGray: "#8B8178",
  line: "#D8CDE8",
  gold: "#C8A96B",
};

function write(name, svg) {
  fs.writeFileSync(path.join(outDir, name), svg.trim() + "\n", "utf8");
}

function svgShell(w, h, body) {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" role="img" aria-label="Jamyung School brand asset">
  <defs>
    <style>
      .kr { font-family: "Noto Serif KR", "Noto Sans KR", "Malgun Gothic", serif; }
      .sans { font-family: "Noto Sans KR", "Malgun Gothic", Arial, sans-serif; }
      .brand { fill: ${C.purple}; }
      .plum { fill: ${C.plum}; }
      .ink { fill: ${C.charcoal}; }
      .muted { fill: ${C.warmGray}; }
      .gold { fill: ${C.gold}; }
      .small { font-size: 24px; letter-spacing: 0; }
    </style>
    <linearGradient id="softPurple" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="${C.purple}"/>
      <stop offset="100%" stop-color="${C.plum}"/>
    </linearGradient>
    <pattern id="quietGrid" width="42" height="42" patternUnits="userSpaceOnUse">
      <path d="M42 0H0v42" fill="none" stroke="${C.line}" stroke-width="1" opacity=".42"/>
    </pattern>
  </defs>
  ${body}
</svg>`;
}

function mark(x, y, s = 1, bg = C.purple, fg = C.ivory) {
  return `<g transform="translate(${x} ${y}) scale(${s})">
    <rect x="0" y="0" width="96" height="96" rx="18" fill="${bg}"/>
    <path d="M28 68V25h12v30c0 10 6 15 15 15 13 0 22-10 22-27V25h12v43H77v-9c-6 8-14 12-25 12-14 0-24-9-24-23Z" fill="${fg}"/>
    <path d="M25 23h45" stroke="${C.gold}" stroke-width="6" stroke-linecap="round"/>
  </g>`;
}

write("00-logo-master.svg", svgShell(1600, 1000, `
  <rect width="1600" height="1000" fill="${C.paper}"/>
  <text x="90" y="105" class="kr brand" font-size="54" font-weight="850">자명스쿨 로고 마스터</text>
  <text x="92" y="154" class="sans muted" font-size="25">이 파일의 로고를 먼저 확정한 뒤 명함, SNS, 포스터, 카드뉴스에 넣어 사용합니다.</text>

  <rect x="90" y="220" width="650" height="250" rx="28" fill="${C.ivory}" stroke="${C.line}" stroke-width="2"/>
  ${mark(145, 285, 1.3)}
  <text x="305" y="345" class="kr brand" font-size="68" font-weight="850">자명스쿨</text>
  <text x="309" y="394" class="sans muted" font-size="24">AI · 콘텐츠 · 1인 비즈니스 교육</text>

  <rect x="860" y="220" width="650" height="250" rx="28" fill="${C.purple}"/>
  ${mark(915, 285, 1.3, C.ivory, C.purple)}
  <text x="1075" y="345" class="kr" fill="${C.ivory}" font-size="68" font-weight="850">자명스쿨</text>
  <text x="1079" y="394" class="sans" fill="${C.line}" font-size="24">AI · 콘텐츠 · 1인 비즈니스 교육</text>

  <rect x="90" y="560" width="420" height="300" rx="28" fill="${C.ivory}" stroke="${C.line}" stroke-width="2"/>
  ${mark(225, 620, 1.55)}
  <text x="300" y="815" text-anchor="middle" class="sans muted" font-size="23">밝은 배경용 심볼</text>

  <rect x="590" y="560" width="420" height="300" rx="28" fill="${C.purple}"/>
  ${mark(725, 620, 1.55, C.ivory, C.purple)}
  <text x="800" y="815" text-anchor="middle" class="sans" fill="${C.line}" font-size="23">어두운 배경용 심볼</text>

  <rect x="1090" y="560" width="420" height="300" rx="28" fill="${C.paper}" stroke="${C.line}" stroke-width="2"/>
  <text x="1300" y="700" text-anchor="middle" class="kr brand" font-size="78" font-weight="850">자명스쿨</text>
  <text x="1300" y="760" text-anchor="middle" class="sans muted" font-size="24">워드마크 단독형</text>
`));

write("01-logo-horizontal.svg", svgShell(1200, 420, `
  <rect width="1200" height="420" fill="${C.paper}"/>
  <rect x="44" y="44" width="1112" height="332" rx="28" fill="${C.ivory}" stroke="${C.line}" stroke-width="2"/>
  ${mark(115, 124, 1.8)}
  <text x="340" y="205" class="kr brand" font-size="86" font-weight="800">자명스쿨</text>
  <text x="346" y="260" class="sans muted" font-size="28" font-weight="500">AI · 콘텐츠 · 1인 비즈니스 교육</text>
  <path d="M345 292H790" stroke="${C.gold}" stroke-width="5" stroke-linecap="round"/>
  <text x="346" y="334" class="sans ink" font-size="24">경험을 콘텐츠로, 콘텐츠를 새로운 일로</text>
`));

write("01A-logo-horizontal-transparent.svg", svgShell(1200, 360, `
  ${mark(82, 82, 1.8)}
  <text x="307" y="163" class="kr brand" font-size="86" font-weight="800">자명스쿨</text>
  <text x="313" y="218" class="sans muted" font-size="28" font-weight="500">AI · 콘텐츠 · 1인 비즈니스 교육</text>
  <path d="M312 250H757" stroke="${C.gold}" stroke-width="5" stroke-linecap="round"/>
  <text x="313" y="292" class="sans ink" font-size="24">경험을 콘텐츠로, 콘텐츠를 새로운 일로</text>
`));

write("01B-logo-horizontal-white.svg", svgShell(1200, 360, `
  ${mark(82, 82, 1.8, C.ivory, C.purple)}
  <text x="307" y="163" class="kr" fill="${C.ivory}" font-size="86" font-weight="800">자명스쿨</text>
  <text x="313" y="218" class="sans" fill="${C.line}" font-size="28" font-weight="500">AI · 콘텐츠 · 1인 비즈니스 교육</text>
  <path d="M312 250H757" stroke="${C.gold}" stroke-width="5" stroke-linecap="round"/>
  <text x="313" y="292" class="sans" fill="${C.paper}" font-size="24">경험을 콘텐츠로, 콘텐츠를 새로운 일로</text>
`));

write("02A-logo-symbol-transparent.svg", svgShell(1080, 1080, `
  ${mark(252, 160, 6)}
  <text x="540" y="820" text-anchor="middle" class="kr brand" font-size="108" font-weight="800">자명스쿨</text>
`));

write("02-logo-symbol-profile.svg", svgShell(1080, 1080, `
  <rect width="1080" height="1080" fill="url(#softPurple)"/>
  <circle cx="540" cy="540" r="392" fill="${C.ivory}" opacity=".95"/>
  ${mark(400, 286, 2.9)}
  <text x="540" y="760" text-anchor="middle" class="kr brand" font-size="92" font-weight="800">자명스쿨</text>
  <text x="540" y="822" text-anchor="middle" class="sans muted" font-size="34">AI 콘텐츠 교육</text>
`));

write("03-business-card-front.svg", svgShell(1012, 638, `
  <rect width="1012" height="638" fill="${C.ivory}"/>
  <rect x="32" y="32" width="948" height="574" rx="26" fill="${C.paper}" stroke="${C.line}" stroke-width="2"/>
  <rect x="32" y="32" width="302" height="574" rx="26" fill="${C.purple}"/>
  <path d="M32 180C118 145 206 175 334 116V606H32Z" fill="${C.plum}" opacity=".62"/>
  ${mark(104, 204, 1.32, C.ivory, C.purple)}
  <text x="510" y="222" class="kr brand" font-size="64" font-weight="800">자명스쿨</text>
  <text x="514" y="274" class="sans muted" font-size="25">AI · 콘텐츠 · 1인 비즈니스 교육</text>
  <text x="514" y="388" class="kr ink" font-size="40" font-weight="700">[대표자명]</text>
  <text x="514" y="430" class="sans muted" font-size="23">Founder / Instructor</text>
  <path d="M514 470H794" stroke="${C.gold}" stroke-width="4" stroke-linecap="round"/>
  <text x="514" y="520" class="sans ink" font-size="25">경험을 콘텐츠로, 콘텐츠를 새로운 일로</text>
`));

write("04-business-card-back.svg", svgShell(1012, 638, `
  <rect width="1012" height="638" fill="${C.purple}"/>
  <rect x="56" y="56" width="900" height="526" rx="24" fill="${C.ivory}"/>
  <text x="118" y="165" class="kr brand" font-size="46" font-weight="800">자명스쿨</text>
  <text x="118" y="214" class="sans muted" font-size="24">AI 활용 · 콘텐츠 제작 · 1인 비즈니스 설계</text>
  <text x="118" y="322" class="sans ink" font-size="28">E. [이메일 입력 필요]</text>
  <text x="118" y="370" class="sans ink" font-size="28">T. [연락처 입력 필요]</text>
  <text x="118" y="418" class="sans ink" font-size="28">W. [홈페이지/신청 링크 입력 필요]</text>
  <rect x="740" y="288" width="138" height="138" fill="${C.paper}" stroke="${C.purple}" stroke-width="6"/>
  <path d="M762 310h34v34h-34zM822 310h34v34h-34zM762 370h34v34h-34zM822 370h12v12h22v22h-34z" fill="${C.purple}"/>
  <text x="809" y="466" text-anchor="middle" class="sans muted" font-size="18">QR</text>
`));

write("05-sns-banner.svg", svgShell(1500, 500, `
  <rect width="1500" height="500" fill="${C.ivory}"/>
  <rect width="1500" height="500" fill="url(#quietGrid)"/>
  <rect x="0" y="0" width="525" height="500" fill="${C.purple}"/>
  <path d="M525 0C456 104 423 234 525 500H348C258 352 245 143 333 0Z" fill="${C.plum}" opacity=".7"/>
  ${mark(112, 132, 1.45, C.ivory, C.purple)}
  <text x="620" y="164" class="kr brand" font-size="62" font-weight="800">AI를 배우는 이유가</text>
  <text x="620" y="244" class="kr brand" font-size="62" font-weight="800">다시 일하는 힘이 되도록</text>
  <text x="623" y="322" class="sans ink" font-size="30">40~60대를 위한 AI · 콘텐츠 · 1인 비즈니스 교육</text>
  <text x="623" y="382" class="sans muted" font-size="24">자명스쿨  |  [대표 강의명 입력 필요]</text>
`));

write("06-poster.svg", svgShell(1080, 1350, `
  <rect width="1080" height="1350" fill="${C.ivory}"/>
  <rect x="58" y="58" width="964" height="1234" rx="34" fill="${C.paper}" stroke="${C.line}" stroke-width="2"/>
  <rect x="58" y="58" width="964" height="328" rx="34" fill="${C.purple}"/>
  <path d="M58 314C256 218 473 353 1022 160V386H58Z" fill="${C.plum}" opacity=".72"/>
  <text x="112" y="170" class="sans" fill="${C.ivory}" font-size="31" font-weight="700">JAMYUNG SCHOOL</text>
  <text x="112" y="258" class="kr" fill="${C.ivory}" font-size="72" font-weight="850">AI로 여는</text>
  <text x="112" y="336" class="kr" fill="${C.ivory}" font-size="72" font-weight="850">나의 두 번째 일</text>
  <text x="112" y="494" class="kr brand" font-size="46" font-weight="800">40~60대를 위한 실전 AI 콘텐츠 클래스</text>
  <text x="112" y="570" class="sans ink" font-size="31">챗GPT 활용, 콘텐츠 기획, 전자책/강의자료 제작,</text>
  <text x="112" y="614" class="sans ink" font-size="31">1인 비즈니스 구조 설계까지 한 흐름으로 배웁니다.</text>
  <rect x="112" y="700" width="856" height="260" rx="22" fill="${C.ivory}" stroke="${C.line}" stroke-width="2"/>
  <text x="160" y="770" class="sans brand" font-size="30" font-weight="800">이런 분께 맞습니다</text>
  <text x="160" y="830" class="sans ink" font-size="28">01  AI를 배우고 싶지만 어디서 시작할지 막막한 분</text>
  <text x="160" y="884" class="sans ink" font-size="28">02  경험을 콘텐츠와 강의로 바꾸고 싶은 분</text>
  <text x="160" y="938" class="sans ink" font-size="28">03  퇴직 후 새로운 수익 구조를 만들고 싶은 분</text>
  <text x="112" y="1060" class="sans ink" font-size="30">일정  [입력 필요]     장소  [입력 필요]</text>
  <text x="112" y="1112" class="sans ink" font-size="30">수강료  [확인 필요]   신청  [링크 입력 필요]</text>
  <rect x="112" y="1182" width="430" height="82" rx="12" fill="${C.purple}"/>
  <text x="327" y="1235" text-anchor="middle" class="sans" fill="${C.ivory}" font-size="31" font-weight="800">상담 / 신청하기</text>
  <text x="600" y="1233" class="kr brand" font-size="39" font-weight="800">자명스쿨</text>
`));

const cards = [
  ["07-carousel-01-hook.svg", "AI가 어려운 게 아니라", "내 일에 연결하는 길이 없었던 겁니다", "40~60대를 위한 실전 AI 콘텐츠 교육"],
  ["08-carousel-02-problem.svg", "배워도 남는 게 없었던 이유", "기능만 배우고 내 경험을 상품으로 바꾸는 구조를 배우지 못했기 때문입니다", "문제 인식"],
  ["09-carousel-03-insight.svg", "중장년의 강점은 따로 있습니다", "오래 쌓은 경험, 설명력, 신뢰감은 AI와 만나면 콘텐츠 자산이 됩니다", "통찰"],
  ["10-carousel-04-solution.svg", "자명스쿨은 이렇게 갑니다", "AI 활용 → 콘텐츠 기획 → 자료 제작 → 1인 비즈니스 흐름까지", "해결 제안"],
  ["11-carousel-05-cta.svg", "다시 시작하는 일을", "혼자 헤매지 않도록 함께 설계합니다", "[대표 강의명 입력 필요] / [신청 링크 입력 필요]"],
];

cards.forEach(([file, title, copy, tag], i) => {
  const side = i % 2 === 0 ? "left" : "right";
  const block = side === "left"
    ? `<rect x="0" y="0" width="265" height="1350" fill="${C.purple}"/><path d="M265 0C180 324 192 846 265 1350H0V0Z" fill="${C.plum}" opacity=".7"/>`
    : `<rect x="815" y="0" width="265" height="1350" fill="${C.purple}"/><path d="M815 0C900 324 888 846 815 1350h265V0Z" fill="${C.plum}" opacity=".7"/>`;
  write(file, svgShell(1080, 1350, `
    <rect width="1080" height="1350" fill="${C.ivory}"/>
    ${block}
    <rect x="102" y="102" width="876" height="1146" rx="30" fill="${C.paper}" stroke="${C.line}" stroke-width="2"/>
    <text x="158" y="202" class="sans gold" font-size="25" font-weight="800">0${i + 1}  ${tag}</text>
    <text x="158" y="430" class="kr brand" font-size="70" font-weight="850">${title}</text>
    <foreignObject x="158" y="500" width="764" height="260">
      <div xmlns="http://www.w3.org/1999/xhtml" style="font-family:'Noto Sans KR','Malgun Gothic',sans-serif;font-size:38px;line-height:1.45;color:${C.charcoal};font-weight:600;word-break:keep-all;">
        ${copy}
      </div>
    </foreignObject>
    <path d="M158 878H620" stroke="${C.gold}" stroke-width="5" stroke-linecap="round"/>
    <text x="158" y="1030" class="kr brand" font-size="45" font-weight="800">자명스쿨</text>
    <text x="158" y="1086" class="sans muted" font-size="26">AI · 콘텐츠 · 1인 비즈니스 교육</text>
  `));
});

write("12-visual-style-board.svg", svgShell(1440, 1080, `
  <rect width="1440" height="1080" fill="${C.ivory}"/>
  <text x="90" y="120" class="kr brand" font-size="66" font-weight="850">Purple Archive</text>
  <text x="92" y="174" class="sans muted" font-size="28">Jamyung School visual direction</text>
  <rect x="90" y="250" width="260" height="260" rx="24" fill="${C.purple}"/>
  <rect x="390" y="250" width="260" height="260" rx="24" fill="${C.plum}"/>
  <rect x="690" y="250" width="260" height="260" rx="24" fill="${C.ivory}" stroke="${C.line}" stroke-width="2"/>
  <rect x="990" y="250" width="260" height="260" rx="24" fill="${C.charcoal}"/>
  <text x="90" y="575" class="sans ink" font-size="26">Deep Purple #36204F</text>
  <text x="390" y="575" class="sans ink" font-size="26">Plum #5A347A</text>
  <text x="690" y="575" class="sans ink" font-size="26">Warm Ivory #F7F1E8</text>
  <text x="990" y="575" class="sans ink" font-size="26">Charcoal #242128</text>
  <rect x="90" y="690" width="1260" height="250" rx="28" fill="${C.paper}" stroke="${C.line}" stroke-width="2"/>
  <text x="150" y="790" class="kr brand" font-size="52" font-weight="850">경험을 콘텐츠로, 콘텐츠를 새로운 일로</text>
  <text x="150" y="858" class="sans ink" font-size="32">AI를 젊은 사람의 기술이 아니라 중장년의 두 번째 일 도구로 번역합니다.</text>
`));

console.log(`Generated ${fs.readdirSync(outDir).filter((f) => f.endsWith(".svg")).length} SVG files in ${outDir}`);
