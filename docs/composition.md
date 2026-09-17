# Composition patterns

Contracts are shapes only. Calculators and calendar libraries stay independently installable.

## Standalone BaZi

```bash
mystilink-bazi calculate --date 1990-05-15 --hour 14 --minute 30
```

No `mystilink-lunar` or schema package is required. Output still carries Ganzhi indices/`text` aligned with `mystilink.bazi.chart/0.1` (plus legacy fields).

## BirthProfile input

```bash
mystilink-bazi calculate --birth-json birth.json
```

`birth.json` should match `mystilink.birth/0.1` (see `examples/birth.minimal.json`). Field convention only — calculators do not import this repository.

## Optional calendar composition (orchestration)

```text
mystilink-lunar convert ... --json > basis.json
# later: mystilink-bazi calculate --calendar-basis basis.json   # reserved; not required in bazi 0.2.0
```

Until a calculator exposes `--calendar-basis` / `[lunar]` extras, compose processes externally: run lunar first, then pass civil time via BirthProfile or CLI flags.

## Compatibility promises

| Pattern | Required installs |
|---------|-------------------|
| BaZi CLI alone | `mystilink-bazi-calculator` |
| BirthProfile file | same; no schema pip package |
| Lunar + BaZi orchestration | both CLIs; no hard pip link between packages |
