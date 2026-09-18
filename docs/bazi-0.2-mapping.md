# BaZi calculator 0.2 field mapping

Maps `mystilink-bazi-calculator` **0.2.0** JSON to v0 contracts. No runtime dependency on this repository.

## Pillar / Ganzhi

| Calculator 0.2 field | Contract | Notes |
|----------------------|----------|-------|
| `pillars.*.stem_index` | `Ganzhi.stem_index` | 0–9 |
| `pillars.*.branch_index` | `Ganzhi.branch_index` | 0–11 |
| `pillars.*.stem` / `branch` | same | |
| `pillars.*.text` | `Ganzhi.text` | preferred for display |
| `pillars.*.ganzhi` | legacy alias of `text` | keep for ≥1 minor |
| `pillars.*.stem_element` etc. | extension | not in core Ganzhi schema |

## Chart document

| Calculator 0.2.x | `mystilink.bazi.chart/0.1` |
|------------------|----------------------------|
| `schema_version` | required const when wrapping as chart |
| `pillars` | required |
| `bazi_schema_version` | calculator-only legacy (`1.0`) |
| `calendar_engine` | `builtin` \| `lunar` \| `external_basis` (0.2.1+) |
| `calendar_basis` | optional nested snapshot (lunar / external_basis) |
| `birth_date`, `bazi_ganzhi`, grids | calculator convenience; omit or keep outside strict chart validation |

Strict validation of a calculator dump against `systems/bazi.chart.schema.json` may fail on extra properties (`additionalProperties: false`). Prefer extracting `{ schema_version, pillars }` (and optional `day_master`) when validating as a chart, or wrap via Envelope.

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
