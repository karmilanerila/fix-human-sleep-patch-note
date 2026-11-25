# Fix Human Sleep: Funniest Patch Note

[![make.fun](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/c/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?ref=h379tqrk)
[![rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/karmilanerila/fix-human-sleep-patch-note/rank.svg)](https://make.fun/c/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?ref=h379tqrk)
[![reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/karmilanerila/fix-human-sleep-patch-note/reward.svg)](https://make.fun/c/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?ref=h379tqrk)

One line of patch notes announcing that human sleep is fixed — funny
enough to make a reader laugh, plausible enough to sit in a real
changelog. Entry for the [Fix Human Sleep: Funniest Patch Note](https://make.fun/c/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?ref=h379tqrk)
competition on [make.fun](https://make.fun/c/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?ref=h379tqrk).

## The line

> Fixed a bug where sleep only dimmed the screen for eight hours; it now actually recharges the human.

## How it works

`main.py` writes that single line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(100 characters, one line, UTF-8, mode 0644). It uses only the Python
standard library and writes the file directly — no temp files, no
network, no dependencies. The output is deterministic: every run
produces the same bytes.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
