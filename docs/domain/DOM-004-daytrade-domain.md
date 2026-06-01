# UC-004 도메인 분석 — 단타 패턴


| 항목 | 내용 |
|------|------|
| TraceID | DOM-004 |

## IntradayPatternAnalyzer

**입력**: `IntradaySeries` — `{ts, price, volume}[]` 당일

**처리**:

1. 결측 보간(제한적)
2. Savitzky-Golay 또는 EMA 스무딩
3. 국소 min/max 후보
4. 거래량 z-score 필터
5. `buy_window` = [t_lo - δ, t_lo + δ], `sell_window` = [t_hi - δ, t_hi + δ]

**출력**: `DayTradeSuggestion` VO

##와 Manual 모드 경계

- Analyzer는 **주문 API 호출 없음**
- `SuggestionPresenter`만 UI·EventStore

## 학습 연계

- 사용자가 제안 수락 후 실제 체결 시 Tier3에 `label=accepted_pattern`
