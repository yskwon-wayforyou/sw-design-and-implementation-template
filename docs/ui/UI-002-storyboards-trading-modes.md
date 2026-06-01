# 화면 콘티 — 매매 모드 (Day · Long · AI · ML) PySide6

| TraceID | UI-002 |
|---------|------------|
| UC | UC-004, UC-005, UC-006, UC-007 |
| Qt6 정본 | [UI-QT6-layout-conventions.md](UI-QT6-layout-conventions.md) |
| 모드 정의 | [SYS-001-system.md](../SYS-001-system.md) §4 |

도식은 **Mermaid만** 사용합니다.

---

## 공통 — `ProposalCardWidget`

위젯 트리: [UI-QT6 §3.2](UI-QT6-layout-conventions.md).

```mermaid
flowchart LR
  DaySvc[DayTradeService] --> Cards[List of ProposalCardWidget]
  LongSvc[LongTermService] --> Cards
  AiSvc[AiAutoService] --> Cards
  Cards --> Dock[order_dock prefill]
```

---

## SCR-MODE-DAY — `DayWorkspaceWidget`

| UC | UC-004 |
|----|--------|
| 스택 인덱스 | `workspace_stack` = 1 |

### Qt6 배치

```mermaid
flowchart TB
  Day[DayWorkspaceWidget]
  Day --> Toolbar[QHBoxLayout day_toolbar]
  Toolbar --> Search[QLineEdit symbol_search]
  Toolbar --> WatchCombo[QComboBox watchlist_combo]
  Toolbar --> SensSlider[QSlider day_sensitivity]
  Toolbar --> AnalyzeBtn[QPushButton analyze_now_btn]
  Day --> MainSplit[QSplitter Horizontal]
  MainSplit --> ChartHost[ChartPanelWidget embedded]
  MainSplit --> Right[QVBoxLayout]
  Right --> ProposalScroll[QScrollArea]
  ProposalScroll --> ProposalStack[QVBoxLayout proposal_cards]
  Right --> Meta[QLabel last_analysis_label]
  Day --> Disclaimer[QLabel disclaimer_label]
```

| 위젯 | objectName | 동작 |
|------|------------|------|
| `QSlider` | `day_sensitivity` | 0=low,1=med,2=high → `DayTradeService.set_sensitivity` |
| `analyze_now_btn` | | 클릭 시 Worker `analyze(symbol)` |
| `ChartPanelWidget` | | `QCandlestickSeries` + `QAreaSeries` buy/sell band |
| `proposal_cards` | | `ProposalCardWidget` 동적 add |

### 사용자 흐름

```mermaid
sequenceDiagram
  participant U as User
  participant UI as DayWorkspaceWidget
  participant Svc as DayTradeService
  participant Chart as QChartView
  U->>UI: 종목_선택
  UI->>Svc: analyze symbol
  Svc-->>UI: DaySuggestion list
  UI->>Chart: set_overlay_windows
  UI->>UI: rebuild ProposalCardWidgets
  U->>UI: fill_order_btn
  UI->>UI: order_dock prefill
```

### 상태

```mermaid
stateDiagram-v2
  [*] --> NoSymbol
  NoSymbol --> Ready: symbol_selected
  Ready --> Analyzing: analyze_triggered
  Analyzing --> ShowingResults: success
  Analyzing --> InsufficientData: few_bars
  ShowingResults --> Ready: refresh_timer
  InsufficientData --> Ready: user_retry
```

---

## SCR-MODE-LONG — `LongWorkspaceWidget`

| UC | UC-005 |
|----|--------|
| 스택 인덱스 | 2 |

```mermaid
flowchart TB
  Long[LongWorkspaceWidget]
  Long --> Bar[QHBoxLayout]
  Bar --> RiskGroup[QButtonGroup QRadioButton x3]
  Bar --> UniverseCombo[QComboBox universe_combo]
  Bar --> ScoreBtn[QPushButton run_scoring_btn]
  Long --> TopCards[QScrollArea horizontal]
  TopCards --> CardRow[QHBoxLayout top_n_cards]
  Long --> BodySplit[QSplitter]
  BodySplit --> RankTable[QTableView ranking_table]
  BodySplit --> Detail[QVBoxLayout]
  Detail --> ScoreChart[QChartView bar_series]
  Detail --> Rationale[QLabel rationale_text]
  Detail --> DisclosureLink[QLabelLinkButton]
  Long --> WeeklyNotify[QCheckBox weekly_rebalance_notify]
  Long --> Footer[TierFooterWidget]
```

| 위젯 | 비고 |
|------|------|
| `ranking_table` | columns: rank, symbol, score, tags |
| `top_n_cards` | `QFrame` × N, 클릭 → table selection sync |
| `run_scoring_btn` | `QProgressDialog` during Worker |

```mermaid
flowchart LR
  ScoreBtn[run_scoring_clicked] --> Worker[LongTermService Worker]
  Worker --> Table[ranking_table model reset]
  Worker --> Cards[top_n_cards rebuild]
```

---

## SCR-MODE-AI — `AiWorkspaceWidget`

| UC | UC-006 |
|----|--------|
| 스택 인덱스 | 3 |

```mermaid
flowchart TB
  AI[AiWorkspaceWidget]
  AI --> Top[QHBoxLayout]
  Top --> ModelBadge[QLabel model_version_label]
  Top --> PolicyCombo[QComboBox policy_combo]
  Top --> PauseBtn[QPushButton pause_toggle checkable]
  AI --> Mid[QSplitter Horizontal]
  Mid --> Left[QVBoxLayout status_pane]
  Left --> StateLabel[QLabel current_action_label]
  Left --> NextTick[QLabel next_tick_label]
  Left --> LogTable[QTableView inference_log_table]
  Mid --> Right[QVBoxLayout approval_pane]
  Right --> QueueList[QListWidget approval_queue]
  Right --> DetailGroup[QGroupBox rationale_group]
  DetailGroup --> Confidence[QLabel]
  DetailGroup --> Features[QTableWidget top_features]
  AI --> AutoToggle[QCheckBox ai_auto_without_approval]
```

| 위젯 | 값 |
|------|-----|
| `policy_combo` | 「승인 필수」「무승인 자동」— `ai_auto_without_approval` |
| `approval_queue` | `ApprovalRequest` id, TTL `QTimer` 로 행 갱신 |
| `pause_toggle` | On 시 `AiAutoService.pause()` |

```mermaid
sequenceDiagram
  participant T as QTimer
  participant AI as AiAutoService
  participant G as ApprovalGate
  participant D as ApprovalDialog
  T->>AI: tick_infer
  AI-->>G: ActionProposal BUY
  alt approval_required
    G->>D: show_modal
    D-->>G: approved
    G->>AI: execute_via_OrderPort
  else auto_without_approval
    G->>AI: execute_direct RiskGuard_only
  end
```

---

## SCR-ML — `MlLabWidget`

| UC | UC-007 |
|----|--------|
| 스택 인덱스 | 4 |

```mermaid
flowchart TB
  ML[MlLabWidget]
  ML --> Split[QSplitter]
  Split --> DataPane[QGroupBox dataset]
  DataPane --> EventCount[QLabel tier3_count]
  DataPane --> ExportBtn[QPushButton export_parquet_btn]
  DataPane --> PreviewBtn[QPushButton preview_btn]
  Split --> TrainPane[QGroupBox training]
  TrainPane --> BuildBtn[QPushButton build_sequences_btn]
  TrainPane --> TrainBtn[QPushButton start_train_btn]
  TrainPane --> Progress[QProgressBar]
  TrainPane --> Metrics[QLabel metrics_label]
  ML --> Models[QGroupBox deployed_models]
  Models --> ModelList[QListWidget artifact_list]
  Models --> ApplyBtn[QPushButton apply_to_ai_btn]
  Models --> RollbackBtn[QPushButton rollback_btn]
```

| Worker | UI 피드백 |
|--------|-----------|
| `train_rnn_personal` | `QProgressBar` + `QPlainTextEdit` log (optional dock) |

---

## 모드 간 데이터 흐름

```mermaid
sequenceDiagram
  participant UI as yst_ui_QStackedWidget
  participant TM as trading_modes
  participant ES as event_store
  participant ML as ml_pipeline

  UI->>TM: set_mode DAY
  TM->>TM: DayTradeService.analyze
  TM-->>UI: DaySuggestion DTOs
  UI->>ES: daytrade_suggestion
  UI->>TM: prefill_order

  UI->>TM: set_mode AI
  TM->>ML: infer
  ML-->>TM: ActionProposal
  TM->>TM: ApprovalGate
  TM-->>UI: ApprovalRequest
```

---

**다음**: [UI-003-storyboards-system-android.md](UI-003-storyboards-system-android.md)
