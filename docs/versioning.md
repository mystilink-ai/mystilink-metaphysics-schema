# Versioning

## Directory major

- `schemas/v0/` — current draft line
- Future breaking line: `schemas/v1/`

## Instance `schema_version`

Format: `mystilink.<name>/<major.minor>`

- **minor**: additive optional fields, clarifications
- **major**: required-field changes, renames, semantic breaks

Producers SHOULD reject unknown major versions and MAY ignore unknown optional fields on the same major.

## Compatibility policy

1. Do not remove or rename required fields within a minor.
2. Prefer additive optional properties.
3. Document migrations in [migration-from-legacy.md](migration-from-legacy.md).
4. Calculator CLI may emit legacy keys in parallel during a deprecation window; new contracts remain authoritative.
