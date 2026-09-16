# Overview

JSON Schema contracts for metaphysics services and integrations.

## Layers

1. **BirthProfile** — person + timezone-aware birth instant
2. **CalendarBasis** — optional lunar/ganzhi/solar-term snapshot
3. **Envelope** — system tag + subject + chart (+ optional interpretation hooks)
4. **systems/** — per-theory chart drafts (`bazi`, `ziwei`, `horoscope`, …)

Chart computation stays in calculator repos. This repository only defines shapes.

## Schema ids

Instances should carry a `schema_version` string:

| Document | `schema_version` |
|----------|------------------|
| Birth | `mystilink.birth/0.1` |
| Calendar basis | `mystilink.calendar_basis/0.1` |
| Envelope | `mystilink.envelope/0.1` |
| BaZi chart | `mystilink.bazi.chart/0.1` |
| Zi Wei chart | `mystilink.ziwei.chart/0.1` |
| Horoscope natal | `mystilink.horoscope.natal/0.1` |

Files live under `schemas/v0/`. See [versioning.md](versioning.md).
