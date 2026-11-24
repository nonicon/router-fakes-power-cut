# The Router That Fakes a Power Cut

[![make.fun](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/nonicon/router-fakes-power-cut/rank.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/nonicon/router-fakes-power-cut/reward.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

An entry for the [make.fun bounty "One Sentence Absurd Invention Pitch"](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a): one sentence pitching a ridiculous invention that fixes a tiny everyday annoyance, judged pairwise by a house judge on funniness, cleverness and originality.

## The pitch

> A Wi-Fi router that fakes a power cut whenever more than five devices connect, so your family finally talks to each other at dinner.

## How it works

`main.py` writes that single sentence to `/output/entry.txt` — the artifact the house judge reads. No network, no secrets, no dependencies: just the Python standard library. A `validate()` gate checks the entry is 1–220 characters, non-blank, a single line and exactly one sentence before writing, and the written file is read back to confirm it matches the entry.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
