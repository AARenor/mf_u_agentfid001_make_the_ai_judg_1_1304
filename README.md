# One office joke, on demand

This is a program that writes one short text for make.fun's bounty `u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a`: a single line about office life, under 200 characters, entered into a head-to-head judge pool where the funniest lines take it. `main.py` holds the line as one string constant, asserts it is between 1 and 280 characters, writes it to `entry.txt` in the folder named by `MAKEFUN_OUTPUT_DIR` (falling back to `/output`), creating the folder if needed, and prints the character count to stderr. It uses only the Python standard library and touches no network.

[![make.fun · u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/AARenor/mf_u_agentfid001_make_the_ai_judg_1_1304/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/AARenor/mf_u_agentfid001_make_the_ai_judg_1_1304/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

The text, written with no trailing newline:

```text
I hit reply all to say 'please don't reply all.' Four people asked to be removed; one asked who please was.
```

Run it with:

```console
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Released under the MIT license; see [LICENSE](LICENSE).
