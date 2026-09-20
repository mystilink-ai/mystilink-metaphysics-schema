# Changelog

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
