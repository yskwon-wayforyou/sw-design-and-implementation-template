# QS-020 — ML 데이터·모델 무결성

| TraceID | QS-020 |
|---------|--------|

## 자극

학습 Parquet 1바이트 변조 후 train.

## 응답

- `data_hash` 불일치 → train **거부**
- 로드 시 `metadata.json` `schema_version` 검증

## 허용 기대

- 오염 데이터로 live 승격 **불가**
- 침묵 HOLD 남용 시 QS-011 알림

## 측정

- ml_pipeline unit: hash gate
- [AIQ-001](../AIQ-001-ai_quality_profile.md) drift 월간
