# Sound library — upload instructions

Drop the finished MP3 files into **this folder**, named exactly as in `SCRIPT.md`:

    A1.1-C01-T01.mp3   A1.1-C04-T02.mp3   …

GitHub web upload: open this folder on github.com → **Add file → Upload files** → drag them in →
**Commit changes**. The page at `/audio/` plays them immediately.

Or from a computer:

    cd anki-hosting/audio
    cp ~/recordings/dist/*.mp3 .
    git add -A && git commit -m "audio: chapters 1-5" && git push
