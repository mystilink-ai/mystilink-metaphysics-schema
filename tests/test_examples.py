# -*- coding: utf-8 -*-
"""Validate examples/ against schemas/v0 using Draft 2020-12."""
from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas" / "v0"
EXAMPLES = ROOT / "examples"


def _registry() -> Registry:
    registry = Registry()
    for path in SCHEMAS.rglob("*.schema.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        registry = registry.with_resource(
            data["$id"],
            Resource.from_contents(data, default_specification=DRAFT202012),
        )
    return registry


REGISTRY = _registry()


def _validator_for(schema_path: Path) -> Draft202012Validator:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, registry=REGISTRY)


CASES = [
    ("birth.minimal.json", SCHEMAS / "birth.schema.json"),
    ("birth.full.json", SCHEMAS / "birth.schema.json"),
    ("envelope.bazi.json", SCHEMAS / "envelope.schema.json"),
    ("envelope.tarot.json", SCHEMAS / "envelope.schema.json"),
    ("error.missing-timezone.json", SCHEMAS / "error.schema.json"),
    ("bazi.chart.json", SCHEMAS / "systems" / "bazi.chart.schema.json"),
    ("ziwei.chart.json", SCHEMAS / "systems" / "ziwei.chart.schema.json"),
    ("horoscope.natal.json", SCHEMAS / "systems" / "horoscope.natal.schema.json"),
    ("horoscope.daily.json", SCHEMAS / "systems" / "horoscope.daily.schema.json"),
    ("horoscope.monthly.json", SCHEMAS / "systems" / "horoscope.monthly.schema.json"),
]


@pytest.mark.parametrize("example_name,schema_path", CASES, ids=[c[0] for c in CASES])
def test_example_validates(example_name: str, schema_path: Path) -> None:
    instance = json.loads((EXAMPLES / example_name).read_text(encoding="utf-8"))
    _validator_for(schema_path).validate(instance)


def test_bazi_chart_requires_day_master() -> None:
    chart = json.loads((EXAMPLES / "bazi.chart.json").read_text(encoding="utf-8"))
    del chart["day_master"]
    with pytest.raises(Exception):
        _validator_for(SCHEMAS / "systems" / "bazi.chart.schema.json").validate(chart)


def test_envelope_bazi_chart_is_strict_chart() -> None:
    """Nested chart in envelope.bazi must also pass bazi.chart schema."""
    envelope = json.loads((EXAMPLES / "envelope.bazi.json").read_text(encoding="utf-8"))
    _validator_for(SCHEMAS / "systems" / "bazi.chart.schema.json").validate(envelope["chart"])
