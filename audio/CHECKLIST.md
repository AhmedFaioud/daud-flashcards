# Recording checklist — Volume 0 sound library

You only need **41 files** for this volume. `SCRIPT.md` lists every one, with the book page it
belongs to and the exact items to say.

---

## Before you start (once)

- [ ] Small room, soft furnishings, no fan, no fridge, no clock ticking
- [ ] Phone on aeroplane mode; window closed
- [ ] Mic a hand's width away, slightly off-axis (not straight at the mouth — stops plosives)
- [ ] One test take; listen back **on headphones**, not the phone speaker
- [ ] Decide your pace: **slow and even** beats fast and clear — the learner is repeating after you

## The protocol, applied to every file

1. **300 ms of stillness** before the first item and after the last
2. Say the item → **pause 2 seconds** → say it again → 2 s → next item
3. Never stack three items without a pause — the pauses are the lesson
4. If you fluff an item: stop, breathe, **restart the whole file**. Don't splice — the rhythm matters

## Order of work

Record in the book's order, chapter by chapter. Each chapter is 1–6 files and 5–10 minutes.

- [ ] **Chapter 1** — 6 files (T01, T03–T07)
- [ ] **Chapter 2** — 4 files (T03, T05–T07)
- [ ] **Chapter 3** — 3 files (T05–T07)
- [ ] **Chapter 4** — 4 files (T02, T03, T05, T07)
- [ ] **Chapter 5** — 3 files (T04, T06, T07)
- [ ] **Chapter 6** — 4 files (T01, T03, T06, T07)
- [ ] **Chapter 7** — 3 files (T01, T03, T07)
- [ ] **Chapter 8** — 3 files (T03, T05, T07)
- [ ] **Chapter 9** — 3 files (T02, T05, T07)
- [ ] **Chapter 10** — 2 files (T03, T07)
- [ ] **Chapter 11** — 2 files (T05, T07)
- [ ] **Chapter 12** — 2 files (T03, T07)
- [ ] **Chapter 13** — 1 file (T07)
- [ ] **Chapter 14** — 1 file (T05)

Three sittings of about 40 minutes each will finish it: chapters 1–5, then 6–10, then 11–14.

## Naming — exactly this

```
A1.1-C01-T01.wav      A1.1 = Volume 0 · C01 = chapter · T01 = track
```

Put the raw takes in `audio/raw/`. Any of `.wav .m4a .mp3 .ogg .flac` is fine.

## After each sitting

```bash
cd /root/arabic-teaching-curriculum/audio
python3 make_audio.py      # trims, normalises, pads, converts to MP3
python3 validate.py        # tells you what is missing or out of spec
```

`make_audio.py` never touches your originals. It writes finished files to `audio/dist/`.

## The five mistakes that waste a session

| Mistake | Why it hurts |
|---|---|
| Recording too close | plosives on ب and م that cannot be fixed later |
| No pauses | the learner has nothing to repeat into |
| One pass instead of two | the book's whole method assumes hear → repeat → hear again |
| Different distance per track | volume jumps between chapters |
| Recording all 41 in one sitting | your voice tires; the last chapters sound flat |

## When it's done

`validate.py` should print **“library complete and within spec ✓”**. Send me `audio/dist/` and I
will publish it next to the deck, with one QR per chapter so a student can hear chapter 4 without
hunting through the whole library.
