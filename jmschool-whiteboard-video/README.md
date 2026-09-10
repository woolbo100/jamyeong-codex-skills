# JMSCHOOL Whiteboard Video Skill

API 키 없이 `edge-tts`와 오픈소스 `srt-whiteboard-animation` 렌더러를 사용해, 그림이 점점 그려지는 설명형 화이트보드 MP4를 만듭니다.

## 흐름

1. 주제 또는 대본 준비
2. `plan_storyboard.py`가 장면 콘티 JSON 생성
3. `make_whiteboard_video.py`가 TTS MP3 생성
4. 장면별 선화 PNG와 annotation JSON 생성
5. `srt-whiteboard-animation`으로 손그림 렌더링
6. FFmpeg로 MP3와 MP4 합성

## Windows 설치

1. Python 3.10 이상을 설치합니다.
2. FFmpeg를 설치하거나 프로젝트의 `tools/ffmpeg/.../bin` 경로를 사용합니다.
3. `srt-whiteboard-animation` 저장소를 설치하고 `scripts/prepare_env.py`를 실행합니다.
4. 이 스킬 폴더에서 실행합니다.

```powershell
python -m pip install -r requirements.txt
```

## 장면 콘티 생성

```powershell
python scripts\plan_storyboard.py --input sample_script.txt --output output\sample_storyboard.json --title "AI 자동화 시작하기"
```

각 scene에는 다음 필드가 들어갑니다.

- `scene_number`
- `narration`
- `short_headline`
- `key_points`
- `visual_type`
- `icon_type`
- `emphasis_words`
- `layout_type`
- `duration_hint`

## 영상 생성

가로형 16:9:

```powershell
python scripts\make_whiteboard_video.py --input sample_script.txt --output output\whiteboard.mp4 --audio-output output\narration.mp3 --title "AI 자동화 시작하기" --subtitle "반복 업무를 줄이는 첫걸음"
```

세로형 9:16:

```powershell
python scripts\make_whiteboard_video.py --input sample_script.txt --output output\whiteboard_vertical.mp4 --audio-output output\narration_vertical.mp3 --title "AI 자동화 시작하기" --width 1080 --height 1920
```

인트로/아웃트로 끄기:

```powershell
python scripts\make_whiteboard_video.py --input sample_script.txt --output output\whiteboard.mp4 --no-intro --no-outro
```

## 주요 옵션

- `--input`: UTF-8 대본 파일
- `--text`: 직접 입력 대본
- `--output`: 최종 MP4 경로
- `--audio-output`: 내레이션 MP3 경로
- `--voice`: edge-tts 음성
- `--rate`: 말하기 속도 예: `-5%`
- `--style`: `clean_education`, `premium_business`, `warm_story`, `simple_kids`
- `--width`, `--height`: 출력 비율 및 해상도
- `--fps`: 프레임레이트
- `--title`, `--subtitle`, `--cta`: 인트로/아웃트로 문구
- `--no-intro`, `--no-outro`: 인트로/아웃트로 비활성화

## 출력 구조

```text
output/
├── narration.mp3
├── storyboard.json
├── whiteboard.mp4
├── whiteboard_silent.mp4
├── preview_01s.png
├── preview_10s.png
├── preview_25s.png
└── srt_assets/
    ├── <title>.png
    └── <title>.annotation.json
```

## 디자인 원칙

한 화면에 문단을 넣지 않습니다. 읽기용 문장은 장면용 문장으로 바꿉니다.

예:

```text
AI는 업무 효율을 높입니다.
-> 반복 업무가 줄어듭니다
-> 시간이 생깁니다
-> 중요한 일에 집중할 수 있습니다
```

목표는 화려함보다 안정적이고 정돈된 설명형 화이트보드 영상입니다.
