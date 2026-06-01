# 품질 시나리오 목록

| 항목 | 내용 |
|------|------|
| TraceID | QSC-001 |
| 버전 | 0.3 |

평가(중요도·선정·근거): [QEV-001-evaluations.md](QEV-001-evaluations.md)

---

## QJ 카탈로그

| TraceID | 제목 | 품질 속성 | 시나리오 요약 | 허용 기대 |
|---------|------|-----------|---------------|-----------|
| QS-001 | 장중 시세 실시간 갱신 | 실시간성 | 장중 종목 시세 갱신 | Tier A: 폴링 ≤3s 또는 WS ≤1s (LAN) |
| QS-002 | paper/live URL·키 혼선 차단 | 안전 | paper+실전 URL 혼선 | 기동 100% 거부 |
| QS-003 | live 주문 확인 UI | 안전 | live 주문 | 100% 확인 UI |
| QS-004 | AI 무승인 주문 차단 | 안전 | AI 무승인 주문 | 기본 0건 |
| QS-005 | KIS 401 토큰 갱신 | 신뢰성 | KIS 401 | 갱신 성공률 >99% (정상망) |
| QS-006 | paper/live 시각 구분 | 사용성 | paper/live 구분 | 1초 내 배너 인지 |
| QS-007 | 주문 제출 UI 응답 | 성능 | 주문 제출 UI | 클릭→전송 <500ms |
| QS-008 | ML 학습 재현성 | 유지보수 | ML 재현 | 동일 data_hash → val_loss ±ε |
| QS-009 | 로그 시크릿 누출 방지 | 보안 | 로그 누출 | 시크릿 패턴 0건 |
| QS-010 | Android 기능 패리티 | 이식성 | Android 패리티 | P1 체크리스트 90% |
| QS-011 | RNN 침묵 실패 감지 | AI 품질 | RNN 침묵 실패 | HOLD 남용 시 알림 |
| QS-012 | SyncHub 오프라인 degraded | 가용성 | SyncHub 오프라인 | Android 읽기 전용+메시지 |
| QS-013 | WS 폴백·stale 시세 차단 | 가용성·안전 | WS 단절·stale | 3s REST 폴백; stale live 주문 0 |
| QS-014 | DB 내구성·백업 | 신뢰성 | DB·크래시 | WAL·백업 RPO 24h |
| QS-015 | 주문 멱등성 | 신뢰성 | 주문 재시도 | 멱등 ID·이중 체결 0 |
| QS-016 | KIS Circuit Breaker | 신뢰성 | KIS 5xx 폭주 | Circuit breaker |
| QS-017 | Hub 세션·무토큰 거부 | 보안 | Hub 무토큰 API | 401·rate limit |
| QS-018 | 금전 감사 append-only | 보안 | 금전 감사 | append-only 100% |
| QS-019 | 릴리스 lock·SBOM | 보안 | 릴리스 | lock·SBOM·CVE 0 |
| QS-020 | ML 데이터 무결성 | AI·보안 | 학습 데이터 | data_hash 게이트 |

상세: `quality/QS-*.md` · 상용: [QLT-002](../QLT-002-commercial-quality-baseline.md)
