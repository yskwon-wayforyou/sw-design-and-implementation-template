# 품질 시나리오 평가

| 항목 | 내용 |
|------|------|
| TraceID | QEV-001 |
| 버전 | 0.3 |
| 입력 | [QSC-001](QSC-001-scenarios.md) · 상세 시나리오 `quality/QS-*.md` |

**표 읽는 법**: `TraceID`는 추적용 코드, **`제목`**으로 검토 내용을 파악한다. **`평가 근거`**는 중요도·선정(Must/Should) 판단의 이유다.

---

## 시나리오별 평가

| TraceID | 제목 | 품질 속성 | 중요도 (1–5) | 구현 난이도 (1–5) | 비즈니스 영향 | 선정 | 평가 근거 |
|---------|------|-----------|:------------:|:-----------------:|---------------|------|-----------|
| QS-001 | 장중 시세 실시간 갱신 | 실시간성 | 5 | 3 | 높음 | **Must** | 매매 UX·Tier A 신뢰의 핵심; [CND-004](../candidate/CND-004-performance-realtime.md)에서 WS+REST 채택. HTS급 체감에 직결 |
| QS-002 | paper/live URL·키 혼선 차단 | 안전 | 5 | 2 | 치명 | **Must** | 오주문·약관 위반 방지; ASR-002·[UC-001](../usecase/UC-001-profile-connect.md). 설계·kis_core에 반영 용이 |
| QS-003 | live 주문 확인 UI | 안전 | 5 | 2 | 치명 | **Must** | 실계좌 오클릭 방지; ASR-003·RG-01. HTS 표준 관행 |
| QS-004 | AI 무승인 주문 차단 | 안전 | 5 | 4 | 치명 | **Must** | 고영향 AI; ADR-004 기본 Off·ApprovalGate. 오너 피드백 #2 |
| QS-005 | KIS 401 토큰 갱신 | 신뢰성 | 4 | 2 | 높음 | **Must** | 세션 끊김 시 업무 중단 방지; NFR-R-01. kis_core 기존 패턴 확장 |
| QS-006 | paper/live 시각 구분 | 사용성 | 4 | 2 | 중 | Should | 혼동 감소; NFR-U-01. UI 배너·[UI-004](../ui/UI-004-plain-language-and-labels.md) |
| QS-007 | 주문 제출 UI 응답 | 성능 | 4 | 2 | 중 | Should | 체감 품질; NFR-P-01. 로컬 RiskGuard 후 전송 |
| QS-008 | ML 학습 재현성 | 유지보수 | 3 | 3 | 중 | Should | NFR-04·UC-007; 동일 data_hash 재현. live 전 모델 검증 전제 |
| QS-009 | 로그 시크릿 누출 방지 | 보안 | 5 | 2 | 치명 | **Must** | ADR-006·ASR-011; 채팅·Git 유출 사고 방지. CI grep 가능 |
| QS-010 | Android 기능 패리티 | 이식성 | 4 | 4 | 중 | Should | UC-010·ADR-001; 승인·조회 동등. WebView 한계 명시 |
| QS-011 | RNN 침묵 실패 감지 | AI 품질 | 4 | 3 | 중 | Should | [AIQ-001](../AIQ-001-ai_quality_profile.md); HOLD 남용·저신뢰 미표시 방지 |
| QS-012 | SyncHub 오프라인 degraded | 가용성 | 3 | 3 | 낮 | Should | 맥북 꺼짐 시 Android 읽기 전용; QS-012·ADR-007 |
| QS-013 | WS 폴백·stale 시세 차단 | 가용성·안전 | 5 | 3 | 치명 | **Must** | [QLT-002](../QLT-002-commercial-quality-baseline.md)·ASR-019; stale live 주문 차단 |
| QS-014 | DB 내구성·백업 | 신뢰성 | 4 | 2 | 높음 | **Must** | ASR-020·[REL-001](../reliability/REL-001-slo-resilience-patterns.md); 이력·감사 손실 방지 |
| QS-015 | 주문 멱등성 | 신뢰성 | 5 | 3 | 치명 | **Must** | ASR-015·RG-08; 네트워크 재시도 이중 체결 방지 |
| QS-016 | KIS Circuit Breaker | 신뢰성 | 4 | 3 | 높음 | **Must** | ASR-016·[ARC-004](../architecture/ARC-004-resilience-security-crosscut.md); 5xx storm 차단 |
| QS-017 | Hub 세션·무토큰 거부 | 보안 | 5 | 3 | 치명 | **Must** | ASR-018·O-01; LAN 스푸핑·무단 주문 방지 |
| QS-018 | 금전 감사 append-only | 보안 | 5 | 2 | 치명 | **Must** | ASR-017·[SEC-001](../security/SEC-001-threat-model-and-controls.md); 사후 추적·분쟁 대응 |
| QS-019 | 릴리스 lock·SBOM | 보안 | 4 | 2 | 중 | Should | ASR-021; 공급망 CVE. 개인 앱이나 상용 기준선 |
| QS-020 | ML 데이터 무결성 | AI·보안 | 4 | 3 | 높음 | Should | ADR-009·오염 학습 방지; `data_hash` 게이트 |

---

## 선정 요약

| 구분 | TraceID | 평가 근거 (요약) |
|------|---------|------------------|
| **Must (live/AI)** | QS-001~004, 009, **013~018** | 금전·키·감사·오주문 직결; 미충족 시 live/AI 릴리스 보류 ([QLT-002](QLT-002-commercial-quality-baseline.md) §4) |
| **Should** | QS-005~008, 010~012, 019~020 | UX·ML·Android·공급망; 로드맵 C/D 허용 |

---

## 후보 구조와의 대응

| 평가 출처 | TraceID | 제목 |
|-----------|---------|------|
| 성능 후보 | CND-004 | 실시간 WS/REST → QS-001 |
| 보안 후보 | CND-005 | RiskGuard+ApprovalGate → QS-002~004, 009 |
| ML 후보 | CND-003 | LSTM BC → QS-008, 011, 020 |
| Android | CND-001 | SyncHub → QS-010, 012, 017 |
| 상용 기준 | ADR-009, ARC-004 | → QS-013~018 |

→ [QLT-001](../QLT-001-qualities.md) · [QLT-002](../QLT-002-commercial-quality-baseline.md) · [DEC-002](../decision/DEC-002-evaluations.md)
