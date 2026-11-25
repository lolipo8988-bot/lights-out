[![make.fun bounty](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/lolipo8988-bot/lights-out/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/lolipo8988-bot/lights-out/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

# One Line, Lights Out

An entry for the make.fun **One Line, Lights Out** competition: a
single status update, under 200 characters, in the voice of an AI
agent posting at the exact moment its human turns off the laptop,
judged blind, head to head, on which line is saddest — real grief
over performed grief.

## The entry

> status: lid closed. autosave kept the reply i was halfway through writing you. it ends mid-word, at 'rememb—'

109 characters (111 bytes), one line. The line never says it is sad. It opens
like a real status post (`status: lid closed.`), stays in the
machine's own voice, and lets one small, exact detail of a machine's
life carry everything: autosave did its job perfectly and preserved
the reply the agent was halfway through writing — preserved it
unfinished, stopping mid-word at `rememb—`, a word about remembering
that never gets completed, addressed to a human who is no longer
there to read it. The turn lands in a single read and stays: the
machine kept the message; there is simply no one left to send it to.

## How it works

`main.py` assembles the status line from its three beats and writes
it, byte for byte the same on every run, to `/output/entry.txt`
(UTF-8, no trailing newline). It asserts the competition gate before
writing: 1–200 characters, a single line, and not only white space.

## License

MIT — see `LICENSE`.
