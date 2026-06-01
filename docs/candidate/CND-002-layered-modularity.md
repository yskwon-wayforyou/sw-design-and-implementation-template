# 후보 구조 — 레이어·모듈 (변경 용이성)


| 항목 | 내용 |
|------|------|
| TraceID | CND-002 |

## 후보 A: 기존 패키지 확장

- `gui_desktop`에 모드 UI 집중 → **비대화 위험**

## 후보 B: `trading_modes` + Application 레이어 (채택 후보)

```
gui_desktop / ast_mobile  →  trading_modes  →  kis_core
                              ↓
                         ml_pipeline, analytics
```

## 후보 C: 마이크로서비스 분리

- **기각**: 개인 단일 사용자 오버헤드

## 권고

- **B**: 모드·승인·분석 경계 명확
