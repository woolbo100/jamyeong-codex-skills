#!/usr/bin/env python3
import argparse
import asyncio
from pathlib import Path
import edge_tts

DEFAULT_VOICE = "ko-KR-SunHiNeural"


def read_text(args):
    if args.text:
        return args.text.strip()
    if args.input:
        return Path(args.input).read_text(encoding="utf-8-sig").strip()
    raise SystemExit("Provide --text or --input")


async def synthesize(text, voice, rate, volume, pitch, output):
    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate=rate,
        volume=volume,
        pitch=pitch,
    )
    await communicate.save(str(out))
    print(out.resolve())


def main():
    p = argparse.ArgumentParser(description="API-key-free TTS using edge-tts")
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--text", help="Text to synthesize")
    src.add_argument("--input", help="UTF-8 text file")
    p.add_argument("--output", default="output/narration.mp3")
    p.add_argument("--voice", default=DEFAULT_VOICE)
    p.add_argument("--rate", default="+0%")
    p.add_argument("--volume", default="+0%")
    p.add_argument("--pitch", default="+0Hz")
    args = p.parse_args()
    text = read_text(args)
    if not text:
        raise SystemExit("Input text is empty")
    asyncio.run(synthesize(text, args.voice, args.rate, args.volume, args.pitch, args.output))


if __name__ == "__main__":
    main()
