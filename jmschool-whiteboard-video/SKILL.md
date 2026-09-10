---
name: jmschool-whiteboard-video
description: Create clean narrated Korean explainer whiteboard videos with free edge-tts and the installed open-source srt-whiteboard-animation renderer. Use when the user gives a topic or script and wants MP3 plus MP4 with drawings progressively appearing on a whiteboard.
---

# JMSCHOOL Whiteboard Video

Use this skill to create a clean, professional explainer-style whiteboard animation without asking for a TTS API key. The default pipeline is: topic or script -> scene storyboard -> line-art whiteboard assets -> free `edge-tts` narration -> open-source `srt-whiteboard-animation` render -> final MP4.

## Defaults

- Preserve a provided script unless the user asks for rewriting.
- If only a topic is provided, draft a concise Korean script before running the tools.
- Convert reading sentences into display sentences: use a short headline plus one or two visual key points, not a paragraph on screen.
- Keep each scene focused on one message. Aim for 5-8 scenes by default.
- Default voice: `ko-KR-SunHiNeural`; default style: `clean_education`; default output: MP3 + MP4.
- Add a 2-3 second intro and a short outro unless the user disables them.
- Support both 16:9 and 9:16. For shorts/reels, use width 1080 and height 1920.

## Local Engines

Prefer the installed open-source renderer at:

`C:\Users\SAMSUNG\Documents\ChatGPT\화이트보드프로젝트\srt-whiteboard-animation`

Use its `scripts/render_stream_whiteboard.py` for the progressive drawing effect. Use HyperFrames only when the user explicitly asks for extra HTML/CSS motion packaging, title sequences, or a richer composition pass. Do not claim HyperFrames was used unless it actually was.

## Workflow

1. Prepare the script.
   - Existing script: use as-is.
   - Topic only: draft a clear Korean explainer script.

2. Plan the storyboard.
   ```powershell
   python scripts\plan_storyboard.py --input script.txt --output output\storyboard.json --title "영상 제목"
   ```
   Each scene includes `scene_number`, `narration`, `short_headline`, `key_points`, `visual_type`, `icon_type`, `emphasis_words`, `layout_type`, and `duration_hint`.

3. Make the video.
   ```powershell
   python scripts\make_whiteboard_video.py --input script.txt --output output\whiteboard.mp4 --audio-output output\narration.mp3 --title "영상 제목"
   ```

4. Verify the result.
   - Confirm MP3 and MP4 exist.
   - Check the MP4 has video and audio streams.
   - Extract beginning, middle, and ending preview frames. The beginning should be sparse, the middle partially drawn, and the ending complete.

## Visual Rules

- Build a concise screen: headline + 1-2 supporting lines + visual symbol.
- Avoid putting full paragraphs on screen.
- Use layout presets: `title_left_icon_right`, `big_quote_center`, `top_title_bottom_steps`, `problem_vs_solution`, `checklist_layout`.
- Use style presets: `clean_education`, `premium_business`, `warm_story`, `simple_kids`.
- Use simple visual elements: arrows, checkboxes, speech bubbles, boxes, underline strokes, number badges.
- Pick icons from: `lightbulb`, `chat`, `target`, `book`, `rocket`, `heart`, `clock`, `checklist`, `computer`, `pencil`.

## Useful Options

`scripts/make_whiteboard_video.py` supports:

`--input`, `--text`, `--output`, `--audio-output`, `--voice`, `--rate`, `--style`, `--width`, `--height`, `--fps`, `--title`, `--subtitle`, `--cta`, `--no-intro`, `--no-outro`.

## Privacy Note

`edge-tts` is free and needs no API key, but it sends narration text to Microsoft's online speech service. When the environment requires explicit approval for private/user-provided text, ask before generating narration.
