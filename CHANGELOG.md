# Changelog

## 0.1.4 — Zi Wei / Horoscope chart alignment

- `systems/ziwei.chart.schema.json`: `additionalProperties: false`; typed 12 palaces; documented calculator fields; `four_pillars` accepts Ganzhi or legacy strings
- `systems/horoscope.natal.schema.json`: tightened points/aspects/asc/mc; `planets` + legacy `points`; `zodiac_system` + legacy `zodiac_mode`; `house_cusps`
- New: `horoscope.daily.schema.json`, `horoscope.monthly.schema.json`
- Examples: `ziwei.chart.json`, `horoscope.natal.json`, `horoscope.daily.json`, `horoscope.monthly.json`
- Docs: mapping + alignment matrix updated
- Instance version strings unchanged (`*.chart|natal|daily|monthly/0.1`)

## 0.1.3 — BaZi chart alignment

- `ganzhi.schema.json`: optional `ganzhi`, `stem_element`, `branch_element`, `zodiac`
- `systems/bazi.chart.schema.json`: require `day_master`; document calculator convenience fields; keep `additionalProperties: false`
- Example `examples/bazi.chart.json`; pytest suite validates all examples (`pip install -e '.[dev]' && pytest`)
- Docs: [alignment-matrix.md](docs/alignment-matrix.md); BaZi mapping updated
- Instance `schema_version` strings unchanged (`mystilink.bazi.chart/0.1`)

## 0.1.2 — Envelope subject optional; tarot/liuyao charts

- `envelope.schema.json`: `subject` no longer required (still recommended for birth-based systems)
- Draft system charts: `tarot.chart`, `liuyao.chart`
- Docs: composition `--envelope` examples; overview / field-index updated
- No change to existing `mystilink.*/0.1` const strings

## 0.1.1 — Composition and BaZi 0.2 mapping

- Docs: [composition.md](docs/composition.md) — standalone vs BirthProfile vs optional lunar (in-process + `--calendar-basis`)
- Docs: [bazi-0.2-mapping.md](docs/bazi-0.2-mapping.md) — field map for `mystilink-bazi-calculator` 0.2.x
- Docs: [ziwei-horoscope-0.2-mapping.md](docs/ziwei-horoscope-0.2-mapping.md) — BirthProfile + schema_version for ziwei/horoscope 0.2.0
- Migration notes updated for calculator Ganzhi indices/`text`
- No change to `mystilink.*/0.1` instance version strings or schema const values

## 0.1.0 — Contract foundation

- `schemas/v0/common/*`: SolarInstant, Ganzhi, pillars, lunar date, zodiac, geo, rules, solar term
- `birth`, `calendar-basis`, `envelope`, `error`
- Draft system charts: bazi, ziwei, horoscope natal
- Examples under `examples/`
- Docs: overview, versioning, migration-from-legacy, field-index
