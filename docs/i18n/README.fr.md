# Mystilink Metaphysics Schema

> Languages: [English](../../README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md)

## Aperçu

Contrats JSON Schema pour services et intégrations de métaphysique : profils de naissance, base calendaire, thèmes système et enveloppes de messages. Ce dépôt définit uniquement les formes ; il ne calcule pas de thèmes et ne produit pas de lectures.

## Type de livraison

Ce dépôt est un **paquet de contrat schéma / documentation**. Il n’implémente **pas** la matrice de langages C / C++ / C# / Java / JavaScript / Python des bibliothèques calculateurs. Des validateurs optionnels peuvent être ajoutés plus tard sans changer cette classification jusqu’à la publication intentionnelle d’un SDK multilingue.

## Contenu

| Chemin | Rôle |
|------|------|
| `schemas/v0/common/` | Types partagés (instant, ganzhi, date lunaire, zodiaque, géo, …) |
| `schemas/v0/birth.schema.json` | Profil de naissance unifié |
| `schemas/v0/calendar-basis.schema.json` | Instantané lunaire/ganzhi optionnel |
| `schemas/v0/envelope.schema.json` | Enveloppe de message service / API |
| `schemas/v0/error.schema.json` | Objet d’erreur structuré |
| `schemas/v0/systems/` | Brouillons de thèmes (bazi, ziwei, horoscope, tarot, liuyao) |
| `examples/` | Documents d’exemple valides (données personnelles fictives) |
| `docs/` | Aperçu, versionnement, migration, index des champs, composition, correspondance BaZi 0.2 |

## Démarrage rapide

1. Pointez producteurs/consommateurs vers les fichiers sous `schemas/v0/`.
2. Copiez un exemple depuis `examples/` et remplacez les champs fictifs si besoin.
3. Validez avec n’importe quel outil JSON Schema Draft 2020-12, par exemple :

```bash
# après : python3 -m pip install jsonschema referencing
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

## Chaînes de version d’instance

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

Voir [docs/versioning.md](../versioning.md).

## Relation avec d’autres dépôts

- `mystilink-lunar-calendar` — produit la base calendaire / faits ganzhi
- `*-calculator` — produisent des objets `chart` système
- Services / API en aval — échangent `BirthProfile` et `Envelope`

Correspondance des champs hérités : [docs/migration-from-legacy.md](../migration-from-legacy.md).  
Composition (autonome / BirthProfile / lunar optionnel) : [docs/composition.md](../composition.md).  
Champs BaZi calculateur 0.2 : [docs/bazi-0.2-mapping.md](../bazi-0.2-mapping.md).  
Champs Zi Wei / Horoscope 0.2 : [docs/ziwei-horoscope-0.2-mapping.md](../ziwei-horoscope-0.2-mapping.md).

## Limites

- Les schémas de thèmes sous `systems/` sont des brouillons ; les formes imbriquées palais/planètes sont volontairement souples
- Aucun moteur de calcul ou d’interprétation de thème n’est inclus
- Aucune liaison SDK de matrice de langages n’est livrée

## Licence

MIT. Voir [LICENSE](../../LICENSE).

## Retours

Signalez les défauts de contrat avec : chemin du fichier schéma, `schema_version`, et un échantillon JSON fictif minimal.
