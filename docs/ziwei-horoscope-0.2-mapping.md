# Zi Wei / Horoscope calculator field mapping

Maps calculator **0.2.x** JSON to v0 contracts. No runtime dependency on this repository.

## Shared BirthProfile input

| CLI | BirthProfile |
|-----|--------------|
| `--birth-json` | whole document `mystilink.birth/0.1` |
| `--datetime` + `--timezone` | civil fallback (not a BirthProfile) |
| ziwei `--gender` | `gender` (`male` \| `female`) |
| horoscope `--lat` / `--lon` | `place.lat` / `place.lon` (or `birth.longitude`) |

## Zi Wei chart (`mystilink.ziwei.chart/0.1`)

| Calculator field | Contract |
|------------------|----------|
| `schema_version` | required const |
| `gender` | required |
| `ming_gong_branch` | required |
| `palaces` | required; 12 items with `palace_index`, `branch`, `name`; star lists are string arrays |
| `four_pillars` | optional; currently stem+branch **strings**; Ganzhi objects also accepted |
| `shen_gong_branch`, `midnight_zi_rule`, lunar/meta fields | documented optional extensions |
| `si_hua`, `liunian` | optional blocks when requested |

Strict validation of a full calculator dump against `systems/ziwei.chart.schema.json` should succeed (see `examples/ziwei.chart.json`).

## Horoscope natal (`mystilink.horoscope.natal/0.1`)

| Calculator field | Contract |
|------------------|----------|
| `schema_version` | required const |
| `planets` | required; preferred |
| `points` | legacy alias of `planets` (≥1 minor) |
| `zodiac_system` | preferred; calculator also emits `zodiac_mode` as legacy alias |
| `house_cusps` | 12 numbers (calculator path); `houses` array optional / unused |
| `asc` / `mc` / `aspects` | typed angle / aspect objects |
| `kind` | optional `natal` (CLI sets it) |

## Horoscope daily / monthly

| Document | `schema_version` | Schema file |
|----------|------------------|-------------|
| Daily transit | `mystilink.horoscope.daily/0.1` | `systems/horoscope.daily.schema.json` |
| Monthly transit | `mystilink.horoscope.monthly/0.1` | `systems/horoscope.monthly.schema.json` |

Examples: `examples/horoscope.daily.json`, `examples/horoscope.monthly.json`.
