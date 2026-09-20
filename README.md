# Mystilink Metaphysics Schema

> Languages: [English](README.md) | [简体中文](README.zh-CN.md)

## Overview

JSON Schema contracts for metaphysics services and integrations: birth profiles, calendar basis, system charts, and message envelopes. This repository defines shapes only; it does not compute charts or produce readings.

## Delivery type

This repository is a **schema / documentation contract package**. It does **not** implement the C / C++ / C# / Java / JavaScript / Python language matrix used by calculator libraries. Optional validators may be added later without changing that classification until a multi-language SDK is intentionally published.

## Contents

| Path | Role |
|------|------|
| `schemas/v0/common/` | Shared types (instant, ganzhi, lunar date, zodiac, geo, …) |
| `schemas/v0/birth.schema.json` | Unified birth profile |
| `schemas/v0/calendar-basis.schema.json` | Optional lunar/ganzhi snapshot |
| `schemas/v0/envelope.schema.json` | Service / API message envelope |
| `schemas/v0/error.schema.json` | Structured error object |
| `schemas/v0/systems/` | Draft chart schemas (bazi, ziwei, horoscope, tarot, liuyao) |
| `examples/` | Valid sample documents (fictional personal data) |
| `docs/` | Overview, versioning, migration, field index, composition, BaZi 0.2 mapping |

## Quick start

1. Point producers/consumers at the schema files under `schemas/v0/`.
2. Copy an example from `examples/` and replace fictional fields as needed.
3. Validate with any JSON Schema Draft 2020-12 tool, for example:

```bash
# after: python3 -m pip install jsonschema referencing
python3 - <<'PY'
from pathlib import Path
import json
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012
from jsonschema import Draft202012Validator

root = Path("schemas/v0")
registry = Registry()
for path in root.rglob("*.schema.json"):
    data = json.loads(path.read_text())
    registry = registry.with_resource(data["$id"], Resource.from_contents(data, default_specification=DRAFT202012))

schema = json.loads((root / "birth.schema.json").read_text())
instance = json.loads(Path("examples/birth.full.json").read_text())
Draft202012Validator(schema, registry=registry).validate(instance)
print("ok")
PY
```

## Instance version strings

| Document | `schema_version` |
|----------|------------------|
| Birth | `mystilink.birth/0.1` |
| Calendar basis | `mystilink.calendar_basis/0.1` |
| Envelope | `mystilink.envelope/0.1` |
| BaZi chart | `mystilink.bazi.chart/0.1` |
| Zi Wei chart | `mystilink.ziwei.chart/0.1` |
| Horoscope natal | `mystilink.horoscope.natal/0.1` |
| Tarot chart | `mystilink.tarot.chart/0.1` |
| Liu Yao chart | `mystilink.liuyao.chart/0.1` |

See [docs/versioning.md](docs/versioning.md).

## Relationship to other repos

- `mystilink-lunar-calendar` — produces calendar basis / ganzhi facts
- `*-calculator` — produce system `chart` objects
- Downstream services / APIs — exchange `BirthProfile` and `Envelope`

Legacy field mapping: [docs/migration-from-legacy.md](docs/migration-from-legacy.md).  
Composition (standalone / BirthProfile / optional lunar): [docs/composition.md](docs/composition.md).  
BaZi calculator 0.2 fields: [docs/bazi-0.2-mapping.md](docs/bazi-0.2-mapping.md).  
Zi Wei / Horoscope 0.2 fields: [docs/ziwei-horoscope-0.2-mapping.md](docs/ziwei-horoscope-0.2-mapping.md).

## Limits

- System chart schemas under `systems/` are drafts; nested palace/planet item shapes are intentionally loose
- No chart computation or interpretation engine is included
- Language-matrix SDK bindings are not shipped

## License

MIT. See [LICENSE](LICENSE).

## Feedback

Report contract defects with: schema file path, `schema_version`, and a minimal fictional JSON sample.
