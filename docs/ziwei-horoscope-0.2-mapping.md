# Zi Wei / Horoscope calculator 0.2 field mapping

Maps calculator **0.2.0** JSON to v0 contracts. No runtime dependency on this repository.

## Shared BirthProfile input

| CLI | BirthProfile |
|-----|--------------|
| `--birth-json` | whole document `mystilink.birth/0.1` |
| `--datetime` + `--timezone` | civil fallback (not a BirthProfile) |
| ziwei `--gender` | `gender` (`male` \| `female`) |
| horoscope `--lat` / `--lon` | `place.lat` / `place.lon` (or `birth.longitude`) |

## Zi Wei chart

| Calculator 0.2 | `mystilink.ziwei.chart/0.1` |
|----------------|----------------------------|
| `schema_version` | required const |
| `gender` | required |
| `ming_gong_branch` | required |
| `palaces` | required |
| other fields | calculator extensions (`additionalProperties` allowed) |

## Horoscope natal

| Calculator 0.2 | `mystilink.horoscope.natal/0.1` |
|----------------|--------------------------------|
| `schema_version` | required const |
| `planets` | alias of legacy `points` |
| `points` | legacy; keep for ≥1 minor |
| `house_system`, `zodiac_mode` | map to `house_system` / `zodiac_system` loosely |

Daily / monthly emit `mystilink.horoscope.daily/0.1` and `mystilink.horoscope.monthly/0.1` (calculator extensions; not yet separate schema files).
