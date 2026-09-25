# Mystilink Metaphysics Schema

> Languages: [English](../../README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md)

## Resumen

Contratos JSON Schema para servicios e integraciones de metafísica: perfiles de nacimiento, base calendárica, cartas de sistema y sobres de mensaje. Este repositorio solo define formas; no calcula cartas ni produce lecturas.

## Puntos de acceso

- Agent: https://www.mystilink.com
- Wiki teórica: https://wiki.mystilink.com (API `/api/v1`)

## Tipo de entrega

Este repositorio es un **paquete de contrato de esquema / documentación**. **No** implementa la matriz de lenguajes C / C++ / C# / Java / JavaScript / Python de las bibliotecas calculadoras. Pueden añadirse validadores opcionales más adelante sin cambiar esa clasificación hasta que se publique intencionadamente un SDK multilingüe.

## Contenido

| Ruta | Rol |
|------|------|
| `schemas/v0/common/` | Tipos compartidos (instante, ganzhi, fecha lunar, zodiaco, geo, …) |
| `schemas/v0/birth.schema.json` | Perfil de nacimiento unificado |
| `schemas/v0/calendar-basis.schema.json` | Instantánea lunar/ganzhi opcional |
| `schemas/v0/envelope.schema.json` | Sobre de mensaje de servicio / API |
| `schemas/v0/error.schema.json` | Objeto de error estructurado |
| `schemas/v0/systems/` | Esquemas de carta de sistema (BaZi / Zi Wei / Horoscope natal·diario·mensual estabilizados; tarot/liuyao más flexibles) |
| `examples/` | Documentos de ejemplo válidos (datos personales ficticios) |
| `docs/` | Resumen, versionado, migración, índice de campos, composición, correspondencia BaZi, [matriz de alineación](../alignment-matrix.md) |
| `tests/` | Validación de ejemplos Draft 2020-12 (`pip install -e '.[dev]' && pytest`) |

## Inicio rápido

1. Apunte productores/consumidores a los archivos bajo `schemas/v0/`.
2. Copie un ejemplo de `examples/` y reemplace campos ficticios según necesite.
3. Valide con cualquier herramienta JSON Schema Draft 2020-12, por ejemplo:

```bash
# después: python3 -m pip install jsonschema referencing
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

## Cadenas de versión de instancia

| Documento | `schema_version` |
|----------|------------------|
| Birth | `mystilink.birth/0.1` |
| Calendar basis | `mystilink.calendar_basis/0.1` |
| Envelope | `mystilink.envelope/0.1` |
| BaZi chart | `mystilink.bazi.chart/0.1` |
| Zi Wei chart | `mystilink.ziwei.chart/0.1` |
| Horoscope natal | `mystilink.horoscope.natal/0.1` |
| Horoscope daily | `mystilink.horoscope.daily/0.1` |
| Horoscope monthly | `mystilink.horoscope.monthly/0.1` |
| Tarot chart | `mystilink.tarot.chart/0.1` |
| Liu Yao chart | `mystilink.liuyao.chart/0.1` |

Vea [docs/versioning.md](../versioning.md).

## Relación con otros repositorios

- `mystilink-lunar-calendar` — produce base calendárica / hechos ganzhi
- `*-calculator` — producen objetos `chart` de sistema
- Servicios / API posteriores — intercambian `BirthProfile` y `Envelope`

Correspondencia de campos heredados: [docs/migration-from-legacy.md](../migration-from-legacy.md).  
Composición (autónomo / BirthProfile / lunar opcional): [docs/composition.md](../composition.md).  
Campos BaZi calculadora 0.2: [docs/bazi-0.2-mapping.md](../bazi-0.2-mapping.md).  
Campos Zi Wei / Horoscope 0.2: [docs/ziwei-horoscope-0.2-mapping.md](../ziwei-horoscope-0.2-mapping.md).

## Límites

- Los esquemas de carta BaZi / Zi Wei / Horoscope (natal, diario, mensual) están estabilizados para las salidas actuales de los calculadores
- Los esquemas de sistema tarot / liuyao siguen siendo más flexibles en la raíz (`additionalProperties: true` en la raíz `chart`)
- El `chart` del sobre sigue siendo un objeto abierto (aún sin `oneOf` por sistema)
- No se incluye motor de cálculo ni de interpretación de cartas
- No se entregan enlaces SDK de la matriz de lenguajes

## Licencia

MIT. Vea [LICENSE](../../LICENSE).

## Comentarios

Reporte defectos de contrato con: ruta del archivo de esquema, `schema_version` y una muestra JSON ficticia mínima.
