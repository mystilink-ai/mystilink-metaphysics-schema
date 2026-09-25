# BaZi calculator 0.2 field mapping

Maps `mystilink-bazi-calculator` **0.2.x** JSON to v0 contracts. No runtime dependency on this repository.

## Pillar / Ganzhi

| Calculator 0.2 field | Contract | Notes |
|----------------------|----------|-------|
| `pillars.*.stem_index` | `Ganzhi.stem_index` | 0–9 |
| `pillars.*.branch_index` | `Ganzhi.branch_index` | 0–11 |
| `pillars.*.stem` / `branch` | same | |
| `pillars.*.text` | `Ganzhi.text` | preferred for display |
| `pillars.*.ganzhi` | optional legacy alias of `text` | allowed on `ganzhi.schema.json` |
| `pillars.*.stem_element` / `branch_element` / `zodiac` | optional extensions | allowed on `ganzhi.schema.json` |

## Chart document

| Calculator 0.2.x | `mystilink.bazi.chart/0.1` |
|------------------|----------------------------|
| `schema_version` | required const |
| `pillars` | required |
| `day_master` | required (equals day pillar) |
| `bazi_schema_version` | optional legacy (`1.0`) |
| `calendar_engine` | optional `builtin` \| `lunar` \| `external_basis` |
| `calendar_basis` | optional nested snapshot |
| `birth_date`, `hour_interval`, `effective_*`, `true_solar_time_*` | optional calculator convenience |
| `birth` | optional `{datetime,timezone}` |
| `bazi_ganzhi`, `summary_zh`, `bazi_grid_cells`, `bazi_details` | optional convenience |
| `dayun` / `liunian` | optional; item shapes still loose |

Strict validation of a full calculator dump against `systems/bazi.chart.schema.json` should succeed for current `bazi calculate` output (see `examples/bazi.chart.json` and calculator `tests/test_schema_alignment.py`).

## Birth input

| Calculator CLI | BirthProfile |
|----------------|--------------|
| `--birth-json` | whole document `mystilink.birth/0.1` |
| `--date` + `--hour` + `--minute` | civil fallback (not a BirthProfile) |
| `--timezone` / `--longitude` | map to `birth.timezone` / `birth.longitude` or `place.lon` |

## Skill profiles

| File | Shape |
|------|-------|
| `mystilink-bazi-skill/examples/profile.v0.json` | BirthProfile |
| `mystilink-bazi-skill/examples/profile.json` | legacy skill fields (see [migration-from-legacy.md](migration-from-legacy.md)) |
