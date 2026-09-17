# Mystilink 术数数据结构标准

> Languages: [English](README.md) | [简体中文](README.zh-CN.md)

## 概述

面向玄学服务与集成场景的 JSON Schema 契约：出生档案、历法基座、体系盘面与消息信封。本仓库只定义数据结构，不进行排盘或解读计算。

## 交付类型

本仓库为 **schema / 文档契约包**。**不适用**计算器仓库的 C / C++ / C# / Java / JavaScript / Python 语言矩阵。日后若增加可选校验器，在正式发布多语言 SDK 之前仍按契约仓说明；发布 SDK 时再按矩阵交付。

## 内容

| 路径 | 作用 |
|------|------|
| `schemas/v0/common/` | 共用类型（瞬间、干支、农历、生肖、地理等） |
| `schemas/v0/birth.schema.json` | 统一出生档案 |
| `schemas/v0/calendar-basis.schema.json` | 可选农历/干支快照 |
| `schemas/v0/envelope.schema.json` | 服务 / API 消息信封 |
| `schemas/v0/error.schema.json` | 结构化错误 |
| `schemas/v0/systems/` | 体系盘面草案（八字、紫微、西洋本命） |
| `examples/` | 合法示例（虚构个人数据） |
| `docs/` | 概述、版本、迁移、字段索引、组合用法、八字 0.2 对照 |

## 快速开始

1. 生产者/消费者引用 `schemas/v0/` 下的 schema 文件。
2. 从 `examples/` 复制示例并按需替换虚构字段。
3. 使用任意 JSON Schema Draft 2020-12 校验器验证，例如：

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

## 实例版本字段

| 文档 | `schema_version` |
|------|------------------|
| Birth | `mystilink.birth/0.1` |
| Calendar basis | `mystilink.calendar_basis/0.1` |
| Envelope | `mystilink.envelope/0.1` |
| BaZi chart | `mystilink.bazi.chart/0.1` |

详见 [docs/versioning.md](docs/versioning.md)。

## 与其他仓库的关系

- `mystilink-lunar-calendar` — 产出历法基座 / 干支事实
- `*-calculator` — 产出体系 `chart`
- 下游服务 / API — 交换 `BirthProfile` 与 `Envelope`

旧字段对照：[docs/migration-from-legacy.md](docs/migration-from-legacy.md)。  
组合用法（单独 / BirthProfile / 可选 lunar）：[docs/composition.md](docs/composition.md)。  
八字计算器 0.2 字段：[docs/bazi-0.2-mapping.md](docs/bazi-0.2-mapping.md)。

## 限制

- `systems/` 下盘面 schema 为草案；宫位/行星等嵌套项有意保持宽松
- 不包含排盘或解读引擎
- 未交付语言矩阵 SDK 绑定

## 许可

MIT。见 [LICENSE](LICENSE)。

## 问题反馈

请附带：schema 文件路径、`schema_version`、最小虚构 JSON 样例。
