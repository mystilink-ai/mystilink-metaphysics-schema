# Composition patterns

Contracts are shapes only. Calculators and calendar libraries stay independently installable.

## Standalone BaZi

```bash
bazi calculate --date 1990-05-15 --hour 14 --minute 30
```

No `mystilink-lunar` or schema package is required. Output still carries Ganzhi indices/`text` aligned with `mystilink.bazi.chart/0.1` (plus legacy fields). `calendar_engine` is `builtin`.

## BirthProfile input

```bash
bazi calculate --birth-json birth.json
```

`birth.json` should match `mystilink.birth/0.1` (see `examples/birth.minimal.json`). Field convention only — calculators do not import this repository.

## Optional lunar engine (in-process)

```bash
python3 -m pip install 'mystilink-bazi-calculator[lunar]'   # Python 3.10+
bazi calculate --date 1990-05-15 --hour 12 \
  --timezone Asia/Shanghai --calendar-engine lunar
```

Uses `GanzhiRules.bazi_default()` inside `mystilink-lunar`. Output sets `calendar_engine` to `lunar` and may embed a `calendar_basis` snapshot.

## Optional calendar composition (orchestration, no import)

```bash
lunar convert --date 1990-05-15 --time 12:00 \
  --timezone Asia/Shanghai --profile bazi --json > basis.json
bazi calculate --calendar-basis basis.json
```

`--calendar-basis` does **not** import `mystilink-lunar`. Accepts `mystilink.calendar_basis/0.1` or lunar convert JSON that includes `ganzhi` four pillars. Output `calendar_engine` is `external_basis`.

## Optional envelope wrap

Calculators default to bare chart JSON. Pass `--envelope` to wrap as `mystilink.envelope/0.1`:

```bash
bazi calculate --date 1990-05-15 --hour 12 --timezone Asia/Shanghai --envelope
ziwei chart --datetime "1990-05-15 14:30" --timezone Asia/Shanghai --gender male --envelope
horoscope natal --datetime "1990-05-15 14:30" --timezone Asia/Shanghai --lat 31.2 --lon 121.5 --envelope
lunar convert --date 1990-05-15 --time 12:00 --timezone Asia/Shanghai --envelope
tarot draw --seed 123 --envelope
liuyao cast --seed 123 --envelope
```

`subject` is included when birth civil time is known; tarot/liuyao may omit it. On `--envelope` errors, stderr uses `{ "error": { "code", "message" } }` (`mystilink` error shape).

## Compatibility promises

| Pattern | Required installs |
|---------|-------------------|
| BaZi CLI alone | `mystilink-bazi-calculator` |
| BirthProfile file | same; no schema pip package |
| Lunar engine in-process | `mystilink-bazi-calculator[lunar]` |
| Lunar JSON → BaZi | both CLIs; no hard pip link between packages |
| Envelope wrap | same calculator; no schema pip package |
