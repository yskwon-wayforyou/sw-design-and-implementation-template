# QS-001 — 장중 시세 실시간성


| 항목 | 내용 |
|------|------|
| TraceID | QS-001 |

## 자극

장중 09:00~15:30, Investor가 종목 A 시세 탭을 연다.

## 환경

- Tier A KIS REST; WS 선택 설정 ON/OFF

## 응답

- REST: 3s 이내 갱신 또는 수동 새로고침
- WS: 1s 이내 push 반영
- UI: `as_of` UTC, Tier 배지

## 허용 기대

- 95% 갱신이 위 주기 이내 (정상망)
- 전용 HTS 틱 수준 **미보장** (면책)

## 측정

- 통합 테스트: mock clock + respx
- UAT: 상태바 타임스탬프 샘플링
