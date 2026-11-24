# Sum up 23 November's world news in one image

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Airdropzon/makefun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Airdropzon/makefun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Entry for the make.fun bounty "Sum up 23 November's world news in one image"
($100 pool, top 50 share the prize).

The image is a front-page infographic of Monday 23 November 2026:

- **COP31 collapses** — UN climate talks in Antalya end with no deal; more
  than 90 nations reject a draft that never mentions fossil fuels.
- **Ukraine sinks a Russian warship** — seven sea drones sink the corvette
  Merkury at Benghazi, Libya; the war reaches the Mediterranean.
- **Strike kills 11 near Kyiv** — a Russian strike hits an apartment block
  in Dymer; a boy, 7, is pulled alive from the rubble.
- **Trump warns of new strikes on Iran** after the New Year if talks fail.
- **Factory fire kills 24 in Indonesia** — blaze at a sweets factory in
  Banten, about 30 people missing.
- **Markets** — Asian tech shares fall as the AI sell-off deepens.
- **Science** — BepiColombo enters Mercury orbit after an eight-year
  journey. Also: AI claims a proof of the Riemann hypothesis, and Alcaraz
  wins the ATP Finals.

Sources: AP, The Guardian, Principia, Middle East Eye.

## How it works

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` (1024×1024, built by `draw_entry.py` with PIL) to
`$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`). No network,
deterministic: both runs write the same bytes.

Run it: `MAKEFUN_OUTPUT_DIR=out python3 main.py`
