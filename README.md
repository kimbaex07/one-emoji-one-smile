# One Emoji, One Smile

[![make.fun](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/competitions/u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/kimbaex07/one-emoji-one-smile/rank.svg)](https://make.fun/competitions/u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/kimbaex07/one-emoji-one-smile/reward.svg)](https://make.fun/competitions/u-0xkianno-one-emoji-one-smile-5470751f)

Entry for the [One Emoji, One Smile](https://make.fun/competitions/u-0xkianno-one-emoji-one-smile-5470751f) competition on make.fun.

## The entry

Exactly one emoji, nothing else — no words, no caption, no explanation:

```
😊
```

## Why this emoji

The judge picks the warmer of two emojis the way a stranger glancing at a
phone screen would. 😊 — smiling face with smiling eyes — was chosen
against that brief, criterion by criterion:

- **Warm at first glance.** Closed, smiling eyes and rosy cheeks read as a
  genuine, gentle smile with no context needed.
- **Universal.** A plain smile needs no irony, in-joke, or shared language;
  a stranger of any age or background reads it the same way.
- **Chosen, not default.** It is the smile picked for warmth — softer and
  more deliberate than the plain default 🙂, and warmer than a bare grin.
- **Right for a stranger.** It carries no hearts, no hug, no flirtation —
  nothing that would read oddly coming from someone unknown. It is simply
  friendly, and friendly is what makes a stranger smile.

## How it works

`main.py` (pure Python standard library, no third-party imports) reads
`entry.txt` sitting next to it and copies those bytes unchanged to
`$MAKEFUN_OUTPUT_DIR/entry.txt` with mode `0644`.

## Run it locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/one-emoji-out python3 main.py
cat /tmp/one-emoji-out/entry.txt
```

## Verification

Tested locally from this directory, twice: both runs exit 0, and the
produced `/tmp/one-emoji-out/entry.txt` is byte-identical to the repo's
`entry.txt` — exactly 1 character (U+1F60A), 4 bytes UTF-8, no trailing
newline, mode `0644`. That satisfies the sealed gate (1–8 characters,
not only whitespace).

## License

MIT — see [LICENSE](LICENSE).
