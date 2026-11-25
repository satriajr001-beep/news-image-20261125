# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/satriajr001-beep/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/satriajr001-beep/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

The World Today — one image summing up the world's news of Wednesday, 25 November 2026: Houthi strikes on a Saudi oil refinery and Riyadh's financial district, Asian stocks sliding as the AI rally fades, Pakistan's first astronaut docking at China's Tiangong station, the Solomon Islands choosing Australia over China, a graft probe into a Politburo member in China, rescuers searching for dozens of miners trapped in a West Java gold mine, insurgents in Mali and across the Sahel taking the war to the skies with cheap drones, and Real Madrid hitting PSV for five in the Champions League.

## Run it

```sh
python3 main.py
```

This writes the image to `/output/entry.png`. The image is bundled as `entry.png.b64` (base64 of the 1024×1024 PNG — the GitHub connector only pushes text, so the PNG travels as base64; the bytes written are identical). If an `entry.png` sits next to `main.py` it is copied directly instead. Deterministic, no network.

## The image

`entry.png` is a newspaper-style summary poster rendered with PIL (all text drawn by script, so every word is crisp). Sources: Reuters, CNN, WSJ.

---

<sub>Entered on [make.fun](https://make.fun/?ref=745kjsj6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
