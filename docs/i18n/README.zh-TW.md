# Mystilink 術數資料結構標準

> Languages: [English](../../README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md)

## 概述

面向玄學服務與整合場景的 JSON Schema 契約：出生檔案、曆法基座、體系盤面與訊息信封。本倉庫只定義資料結構，不進行排盤或解讀計算。

## 交付類型

本倉庫為 **schema / 文件契約套件**。**不適用**計算器倉庫的 C / C++ / C# / Java / JavaScript / Python 語言矩陣。日後若增加可選校驗器，在正式發布多語言 SDK 之前仍按契約倉說明；發布 SDK 時再按矩陣交付。

## 內容

| 路徑 | 作用 |
|------|------|
| `schemas/v0/common/` | 共用類型（瞬間、干支、農曆、生肖、地理等） |
| `schemas/v0/birth.schema.json` | 統一出生檔案 |
| `schemas/v0/calendar-basis.schema.json` | 可選農曆/干支快照 |
| `schemas/v0/envelope.schema.json` | 服務 / API 訊息信封 |
| `schemas/v0/error.schema.json` | 結構化錯誤 |
| `schemas/v0/systems/` | 體系盤面草案（八字、紫微、西洋本命、塔羅、六爻） |
| `examples/` | 合法範例（虛構個人資料） |
| `docs/` | 概述、版本、遷移、欄位索引、組合用法、八字 0.2 對照 |

## 快速開始

1. 生產者/消費者引用 `schemas/v0/` 下的 schema 檔案。
2. 從 `examples/` 複製範例並按需替換虛構欄位。
3. 使用任意 JSON Schema Draft 2020-12 校驗器驗證，例如：

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

## 實例版本欄位

| 文件 | `schema_version` |
|------|------------------|
| Birth | `mystilink.birth/0.1` |
| Calendar basis | `mystilink.calendar_basis/0.1` |
| Envelope | `mystilink.envelope/0.1` |
| BaZi chart | `mystilink.bazi.chart/0.1` |
| Zi Wei chart | `mystilink.ziwei.chart/0.1` |
| Horoscope natal | `mystilink.horoscope.natal/0.1` |
| Tarot chart | `mystilink.tarot.chart/0.1` |
| Liu Yao chart | `mystilink.liuyao.chart/0.1` |

詳見 [docs/versioning.md](../versioning.md)。

## 與其他倉庫的關係

- `mystilink-lunar-calendar` — 產出曆法基座 / 干支事實
- `*-calculator` — 產出體系 `chart`
- 下游服務 / API — 交換 `BirthProfile` 與 `Envelope`

舊欄位對照：[docs/migration-from-legacy.md](../migration-from-legacy.md)。  
組合用法（單獨 / BirthProfile / 可選 lunar）：[docs/composition.md](../composition.md)。  
八字計算器 0.2 欄位：[docs/bazi-0.2-mapping.md](../bazi-0.2-mapping.md)。  
紫微 / 西洋盤 0.2 欄位：[docs/ziwei-horoscope-0.2-mapping.md](../ziwei-horoscope-0.2-mapping.md)。

## 限制

- `systems/` 下盤面 schema 為草案；宮位/行星等巢狀項有意保持寬鬆
- 不包含排盤或解讀引擎
- 未交付語言矩陣 SDK 綁定

## 授權

MIT。見 [LICENSE](../../LICENSE)。

## 問題回饋

請附帶：schema 檔案路徑、`schema_version`、最小虛構 JSON 樣例。
