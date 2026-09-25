# Mystilink 현학 스키마

> Languages: [English](../../README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md)

## 개요

현학 서비스와 통합을 위한 JSON Schema 계약: 출생 프로필, 역법 기반, 체계 차트, 메시지 엔벨로프. 이 저장소는 형태만 정의하며 배반이나 해석을 수행하지 않습니다.

## 엔드포인트

- Agent: https://www.mystilink.com
- 이론 Wiki: https://wiki.mystilink.com (API `/api/v1`)

## 제공 유형

이 저장소는 **스키마 / 문서 계약 패키지**입니다. 계산기 저장소의 C / C++ / C# / Java / JavaScript / Python 언어 매트릭스는 **적용하지 않습니다**. 선택적 검증기를 나중에 추가해도, 다국어 SDK를 의도적으로 공개하기 전까지는 이 분류를 유지합니다.

## 내용

| 경로 | 역할 |
|------|------|
| `schemas/v0/common/` | 공유 타입(순간, 간지, 음력, 띠, 지리 등) |
| `schemas/v0/birth.schema.json` | 통합 출생 프로필 |
| `schemas/v0/calendar-basis.schema.json` | 선택적 음력/간지 스냅샷 |
| `schemas/v0/envelope.schema.json` | 서비스 / API 메시지 엔벨로프 |
| `schemas/v0/error.schema.json` | 구조화 오류 |
| `schemas/v0/systems/` | 체계 차트 스키마(팔자 / 자미 / 서양 네이탈·일간·월간 안정화; 타로/육효는 느슨함) |
| `examples/` | 유효 샘플(가상의 개인 데이터) |
| `docs/` | 개요, 버전, 이전, 필드 색인, 조합, 팔자 대응, [alignment matrix](../alignment-matrix.md) |
| `tests/` | 예제 Draft 2020-12 검증 (`pip install -e '.[dev]' && pytest`) |

## 빠른 시작

1. 생산자/소비자는 `schemas/v0/` 아래 스키마 파일을 참조합니다.
2. `examples/`에서 예제를 복사하고 필요 시 가상 필드를 바꿉니다.
3. 임의의 JSON Schema Draft 2020-12 도구로 검증합니다. 예:

```bash
# 먼저: python3 -m pip install jsonschema referencing
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

## 인스턴스 버전 문자열

| 문서 | `schema_version` |
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

[docs/versioning.md](../versioning.md) 참고.

## 다른 저장소와의 관계

- `mystilink-lunar-calendar` — 역법 기반 / 간지 사실 생성
- `*-calculator` — 체계 `chart` 생성
- 다운스트림 서비스 / API — `BirthProfile`과 `Envelope` 교환

구 필드 대응: [docs/migration-from-legacy.md](../migration-from-legacy.md).  
조합(단독 / BirthProfile / 선택 lunar): [docs/composition.md](../composition.md).  
팔자 계산기 0.2 필드: [docs/bazi-0.2-mapping.md](../bazi-0.2-mapping.md).  
자미 / 서양 차트 0.2 필드: [docs/ziwei-horoscope-0.2-mapping.md](../ziwei-horoscope-0.2-mapping.md).

## 제한

- 팔자 / 자미 / 서양(네이탈, 일간, 월간) 차트 스키마는 현재 계산기 출력에 맞춰 안정화됨
- 타로 / 육효 체계 스키마는 루트에서 여전히 느슨함(`chart` 루트는 `additionalProperties: true`)
- Envelope `chart`는 아직 개방형 객체(체계별 `oneOf` 미적용)
- 차트 계산·해석 엔진은 포함하지 않음
- 언어 매트릭스 SDK 바인딩은 제공하지 않음

## 라이선스

MIT. [LICENSE](../../LICENSE) 참고.

## 피드백

계약 결함 보고 시: 스키마 파일 경로, `schema_version`, 최소 가상 JSON 샘플을 첨부하세요.
