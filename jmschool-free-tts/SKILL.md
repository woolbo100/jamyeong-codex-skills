---
name: jmschool-free-tts
description: Generate Korean or other-language TTS narration as MP3 without API keys using edge-tts. Use when the user asks Codex to make narration, voiceover, TTS audio, or an MP3 from a script and wants a free/no-API-key workflow.
---

# JMSCHOOL Free TTS

Use this skill to turn text or a text file into narration audio without asking the user for an API key.

## Workflow

1. Confirm Python is available.
2. If `edge-tts` is not installed, run `python -m pip install -r requirements.txt` from this skill directory.
3. Use `scripts/tts.py` to generate the audio.
4. Default to Korean female voice `ko-KR-SunHiNeural` unless the user asks for another voice.
5. Save output as MP3 in the user's requested project/output folder. If none is specified, use `output/narration.mp3` in the current project.
6. Report the exact output path when finished.

## Commands

Direct text:

```bash
python scripts/tts.py --text "안녕하세요. 자명스쿨입니다." --output narration.mp3
```

Text file:

```bash
python scripts/tts.py --input script.txt --output narration.mp3
```

Male Korean voice:

```bash
python scripts/tts.py --input script.txt --voice ko-KR-InJoonNeural --output narration.mp3
```

Slower speech:

```bash
python scripts/tts.py --input script.txt --rate=-5% --output narration.mp3
```

## Constraints

- Do not request or create a TTS API key.
- This workflow needs internet access because `edge-tts` uses Microsoft's online speech service.
- If the requested voice fails, list available voices with `edge-tts --list-voices` and select a matching Korean voice.
- Do not hardcode secrets or credentials.
