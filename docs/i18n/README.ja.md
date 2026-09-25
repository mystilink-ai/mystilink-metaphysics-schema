# Mystilink 玄学スキーマ

> Languages: [English](../../README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md)

## 概要

玄学サービスと統合向けの JSON Schema 契約：出生プロフィール、暦基盤、体系盤面、メッセージエンベロープ。本リポジトリは形状のみを定義し、排盤や解読は行いません。

## エンドポイント

- Agent：https://www.mystilink.com
- 理論 Wiki：https://wiki.mystilink.com（API `/api/v1`）

## デリバリ種別

本リポジトリは **スキーマ / ドキュメント契約パッケージ**です。計算機リポジトリの C / C++ / C# / Java / JavaScript / Python 言語マトリクスは**適用しません**。任意の検証器を後から追加しても、多言語 SDK を意図的に公開するまではこの分類のままです。

## 内容

| パス | 役割 |
|------|------|
| `schemas/v0/common/` | 共有型（瞬間、干支、旧暦、十二支、地理など） |
| `schemas/v0/birth.schema.json` | 統一出生プロフィール |
| `schemas/v0/calendar-basis.schema.json` | 任意の旧暦/干支スナップショット |
| `schemas/v0/envelope.schema.json` | サービス / API メッセージエンベロープ |
| `schemas/v0/error.schema.json` | 構造化エラー |
| `schemas/v0/systems/` | 体系盤面スキーマ（八字 / 紫微 / 西洋ネイタル・日次・月次は安定；タロット/六爻は緩め） |
| `examples/` | 妥当なサンプル（架空の個人データ） |
| `docs/` | 概要、版管理、移行、フィールド索引、組み合わせ、八字対応、[alignment matrix](../alignment-matrix.md) |
| `tests/` | 例の Draft 2020-12 検証（`pip install -e '.[dev]' && pytest`） |

## クイックスタート

1. 生産者/消費者は `schemas/v0/` 配下のスキーマを参照します。
2. `examples/` から例をコピーし、架空フィールドを必要に応じて置き換えます。
3. 任意の JSON Schema Draft 2020-12 ツールで検証します。例：

```bash
# 先: python3 -m pip install jsonschema referencing
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

## インスタンス版文字列

| 文書 | `schema_version` |
|------|------------------|
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

[docs/versioning.md](../versioning.md) を参照。

## 他リポジトリとの関係

- `mystilink-lunar-calendar` — 暦基盤 / 干支事実を生成
- `*-calculator` — 体系 `chart` を生成
- 下流サービス / API — `BirthProfile` と `Envelope` を交換

旧フィールド対応：[docs/migration-from-legacy.md](../migration-from-legacy.md)。  
組み合わせ（単独 / BirthProfile / 任意 lunar）：[docs/composition.md](../composition.md)。  
八字計算機 0.2 フィールド：[docs/bazi-0.2-mapping.md](../bazi-0.2-mapping.md)。  
紫微 / 西洋盤 0.2 フィールド：[docs/ziwei-horoscope-0.2-mapping.md](../ziwei-horoscope-0.2-mapping.md)。

## 制限

- 八字 / 紫微 / 西洋（ネイタル、日次、月次）の盤面スキーマは現行計算機出力に合わせて安定化済み
- タロット / 六爻の体系スキーマはルートで依然として緩め（`chart` ルートは `additionalProperties: true`）
- Envelope の `chart` は未だオープンなオブジェクト（体系ごとの `oneOf` は未導入）
- 排盤・解釈エンジンは含まない
- 言語マトリクス SDK バインディングは同梱しない

## ライセンス

MIT。[LICENSE](../../LICENSE) を参照。

## フィードバック

契約の不具合報告時は：スキーマファイルパス、`schema_version`、最小の架空 JSON サンプルを添えてください。
