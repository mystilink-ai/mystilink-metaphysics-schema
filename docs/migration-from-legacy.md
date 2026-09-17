# Migration from legacy shapes

This map helps adapt existing Mystilink skill/calculator JSON to v0 contracts. Examples use fictional data only.

## Birth profile

| Legacy (bazi-skill) | v0 BirthProfile |
|---------------------|-----------------|
| `birth_date` + `birth_time` + `birth_place_timezone` | `birth.datetime` (ISO-8601 with offset) + `birth.timezone` |
| `birth_place` | `place.label` |
| `birth_place_latitude` / `birth_place_longitude` | `place.lat` / `place.lon` |
| `gender` | `gender` (`male` \| `female` \| `unspecified`) |

| Legacy (ziwei / horoscope skill) | v0 |
|----------------------------------|-----|
| `datetime`: `YYYY-MM-DD HH:MM` | `birth.datetime` ISO with offset |
| `timezone` | `birth.timezone` |
| `lat` / `lon` | `place.lat` / `place.lon` |
| `longitude` only | `birth.longitude` and/or `place.lon` |

## Pillars

| Legacy (bazi-calculator ≤0.1) | v0 Ganzhi / calculator 0.2 |
|-------------------------------|----------------------------|
| `stem`, `branch`, `ganzhi` | `stem`, `branch`, `text` (+ required `stem_index`, `branch_index`); `ganzhi` kept as alias of `text` |
| `pillars` | same slots under `chart.pillars` or `calendar_basis.ganzhi` |

See [bazi-0.2-mapping.md](bazi-0.2-mapping.md) for the full calculator 0.2 table. Composition without hard package coupling: [composition.md](composition.md).

## Envelope

Wrap calculator output:

1. Build `subject` as BirthProfile
2. Optionally attach `calendar_basis` from `mystilink-lunar`
3. Put system facts in `chart` with the matching `systems/*.schema.json`
4. Keep interpretation references in `interpretation.wiki_ids`, not inside chart facts
