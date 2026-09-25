# Alignment matrix

Tracks input / output contract coverage across Mystilink packages. Update when schemas or CLIs change.

## Legend

| Status | Meaning |
|--------|---------|
| ok | Documented + examples/tests green |
| partial | Schema or CLI exists; gaps remain |
| missing | Not defined yet |

## Contracts (`mystilink-metaphysics-schema`)

| Document | `schema_version` | Schema file | Examples | Notes |
|----------|------------------|-------------|---------|-------|
| BirthProfile | `mystilink.birth/0.1` | `birth.schema.json` | ok | |
| Calendar basis | `mystilink.calendar_basis/0.1` | `calendar-basis.schema.json` | partial | Covered inside envelopes; no bare example yet |
| Envelope | `mystilink.envelope/0.1` | `envelope.schema.json` | ok (bazi, tarot) | `chart` still open object; not `oneOf` systems |
| Error | (none) | `error.schema.json` | ok | |
| BaZi chart | `mystilink.bazi.chart/0.1` | `systems/bazi.chart.schema.json` | ok | Stabilized; `day_master` required |
| Zi Wei chart | `mystilink.ziwei.chart/0.1` | `systems/ziwei.chart.schema.json` | ok | Stabilized; 12 typed palaces; string or Ganzhi pillars |
| Horoscope natal | `mystilink.horoscope.natal/0.1` | `systems/horoscope.natal.schema.json` | ok | `planets` + `zodiac_system`; legacy aliases kept |
| Horoscope daily | `mystilink.horoscope.daily/0.1` | `systems/horoscope.daily.schema.json` | ok | |
| Horoscope monthly | `mystilink.horoscope.monthly/0.1` | `systems/horoscope.monthly.schema.json` | ok | |
| Tarot chart | `mystilink.tarot.chart/0.1` | `systems/tarot.chart.schema.json` | partial | Envelope example only |
| Liu Yao chart | `mystilink.liuyao.chart/0.1` | `systems/liuyao.chart.schema.json` | missing | |

## Calculators → contracts

| Repo | Primary CLI | BirthProfile in | Bare chart validates | `--envelope` | Notes |
|------|-------------|-----------------|----------------------|--------------|-------|
| `mystilink-lunar-calendar` | `lunar convert` | via envelope subject | partial | convert only | Injects `calendar_basis/0.1` under envelope |
| `mystilink-bazi-calculator` | `bazi calculate` | `--birth-json` | ok (with `day_master`) | calculate only | dayun/liunian not enveloped yet |
| `mystilink-ziwei-calculator` | `ziwei chart` | `--birth-json` | ok | chart | Golden test vs shared schema |
| `mystilink-horoscope-calculator` | `horoscope natal` | `--birth-json` | ok (natal/daily/monthly) | natal/daily/monthly | Emits `zodiac_system` + `zodiac_mode` |
| `mystilink-tarot-calculator` | `tarot draw` | n/a | ok | draw | |
| `mystilink-liuyao-calculator` | `liuyao cast` | n/a | ok | cast | |

## MCP (`mystilink-mcp`)

| Tool | CLI | Envelope default | BirthProfile |
|------|-----|------------------|--------------|
| `lunar_convert` | `lunar convert` | true | no |
| `bazi_calculate` | `bazi calculate` | true | `birth_json` string |
| `bazi_dayun` | `bazi dayun` | n/a (CLI has no envelope) | no |
| `bazi_liunian` | `bazi liunian` | n/a | no |
| `ziwei_chart` | `ziwei chart` | true | `birth_json` |
| `horoscope_natal` | `horoscope natal` | true | `birth_json` |
| `horoscope_daily` | missing | — | — |
| `horoscope_monthly` | missing | — | — |
| `tarot_draw` | `tarot draw` | true | n/a |
| `liuyao_cast` | `liuyao cast` | true | n/a |

## Skills

| Skill | Execution | BirthProfile in SKILL.md | Notes |
|-------|-----------|--------------------------|-------|
| `mystilink-bazi` | embedded scripts | legacy flat | Target: call `bazi` CLI |
| `mystilink-ziwei` | embedded | partial | Target: call `ziwei` CLI |
| `mystilink-horoscope` | embedded | partial | natal only |
| `mystilink-tarot` | embedded | n/a | |
| `mystilink-liuyao` | embedded | n/a | throws docs vs CLI mismatch |
| `mystilink-router` | no chart | n/a | |

## Next alignment slices

1. MCP `horoscope_daily` / `horoscope_monthly` tools
2. Tarot / Liu Yao bare chart examples; optional root `additionalProperties` tighten
3. Skills thin-wrap published CLIs; SKILL.md BirthProfile default
4. Prefer Zi Wei `four_pillars` as Ganzhi objects (calculator migration)
