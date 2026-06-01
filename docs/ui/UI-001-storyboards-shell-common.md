# 화면 콘티 — 셸·온보딩·공통 HTS (PySide6)

| TraceID | UI-001 |
|---------|------------|
| Qt6 정본 | [UI-QT6-layout-conventions.md](UI-QT6-layout-conventions.md) |

도식은 **Mermaid만** 사용합니다. 위젯 이름은 `objectName` / 클래스명 기준입니다.

---

## SCR-000 — 기동·스플래시

| UC | UC-001 |
|----|--------|
| 진입 | `QApplication` 실행 직후 |

```mermaid
flowchart TB
  subgraph Splash[SplashScreen QWidget frameless]
    Logo[QLabel app_logo pixmap]
    Title[QLabel YSTrading]
    Progress[QProgressBar indeterminate]
    Status[QLabel status_text]
  end
```

| 위젯 | 역할 |
|------|------|
| `QProgressBar` | `setRange(0,0)` 무한 진행 |
| `status_text` | 「볼트 확인」「프로필 로드」 |

```mermaid
stateDiagram-v2
  [*] --> Loading
  Loading --> Onboarding: vault_missing
  Loading --> ProfilePick: vault_ok
  Loading --> Error: vault_decrypt_fail
  ProfilePick --> Shell: profile_ok
  Onboarding --> ProfilePick: wizard_finished
  Error --> Onboarding: user_opens_settings
```

---

## SCR-001 — 최초 설정 (`QWizard`)

| UC | UC-001 |

```mermaid
flowchart LR
  W[QWizard objectName_onboarding_wizard]
  W --> P1[QWizardPage welcome]
  W --> P2[QWizardPage kis_credentials]
  W --> P3[QWizardPage connection_test]
  P2 --> PaperForm[QFormLayout paper_app_key_secret]
  P2 --> LiveForm[QFormLayout live_app_key_secret_account]
  P3 --> Result[QLabel test_result_badge]
```

| 페이지 | 주요 위젯 |
|--------|-----------|
| 환영 | `QLabel` 설명 · `QPushButton` 다음 |
| 키 | `QLineEdit` echoMode=Password · `QPushButton` import_json_btn |
| 테스트 | `QPushButton` run_test_btn · `QLabel` success/fail |

```mermaid
sequenceDiagram
  participant U as User
  participant W as QWizard
  participant K as kis_core_adapter
  U->>W: 다음_키_입력
  W->>K: test_connection_paper
  K-->>W: ok_or_error
  W-->>U: SCR-002_이동
```

---

## SCR-002 — 프로필 선택

| UC | UC-001, UC-011 |

```mermaid
flowchart TB
  D[ProfileDialog QDialog]
  D --> Title[QLabel headline]
  D --> Cards[QHBoxLayout]
  Cards --> PaperCard[QFrame paper_card]
  Cards --> LiveCard[QFrame live_card]
  PaperCard --> PaperRadio[QRadioButton paper_rb]
  LiveCard --> LiveRadio[QRadioButton live_rb]
  D --> StartBtn[QPushButton start_btn default]
```

| 동작 | Qt6 처리 |
|------|----------|
| live 선택 | `live_card` 클릭 → `RiskAckDialog` (`QMessageBox`) → `MainWindow.apply_profile(live)` |
| paper | 녹색 `stylesheet` border on `paper_card` |

---

## SCR-SHELL — 앱 셸

정본 위젯 트리: [UI-QT6 §2](UI-QT6-layout-conventions.md).

```mermaid
sequenceDiagram
  participant Rail as QListWidget_mode_rail
  participant Orch as ModeOrchestrator
  participant Stack as QStackedWidget
  Rail->>Orch: set_mode index
  Orch->>Stack: setCurrentIndex
```

---

## SCR-HOME — 현황 (`HomeDashboardWidget`)

| UC | UC-003, UC-008 |
|----|----------------|
| 탭 | `manual_tabs` index 0 |

```mermaid
flowchart TB
  Home[HomeDashboardWidget]
  Home --> AccountBox[QGroupBox account_summary]
  AccountBox --> Grid[QGridLayout labels]
  Home --> Split[QSplitter Horizontal]
  Split --> Watch[QTableView watchlist_table]
  Split --> IndexScroll[QScrollArea index_cards]
  Home --> Recent[QListView recent_proposals]
  Home --> Footer[TierFooterWidget]
```

| 위젯 | 데이터 |
|------|--------|
| `watchlist_table` | `QStandardItemModel` · symbol, price, change% |
| `recent_proposals` | `ProposalCardWidget` delegate 또는 compact row |

```mermaid
flowchart LR
  RowClick[행_클릭] --> Quote[manual_tabs_시세]
  OrderBtn[주문_버튼] --> Dock[order_dock_show]
```

| 상태 | UI |
|------|-----|
| 로딩 | `watchlist_table.setEnabled false` + `QStackedWidget` skeleton page |
| KIS 끊김 | `profile_toolbar` 에 `QLabel` offline_banner |

---

## SCR-QUOTE — 시세 (`QuotePanelWidget`)

| UC | UC-003 |

```mermaid
flowchart TB
  Q[QuotePanelWidget]
  Q --> Header[QHBoxLayout]
  Header --> BackBtn[QToolButton]
  Header --> SymbolTitle[QLabel]
  Header --> FavBtn[QToolButton star]
  Header --> ChartBtn[QPushButton]
  Header --> OrderBtn[QPushButton]
  Q --> PriceRow[QLabel large_price]
  Q --> Split2[QSplitter]
  Split2 --> QuoteLeft[QTableView bid_ask_or_summary]
  Split2 --> QuoteRight[QFormLayout day_ohlcv]
  Q --> NewsTeaser[QPushButton open_news]
  Q --> Footer[TierFooterWidget]
```

---

## SCR-CHART — 차트 (`ChartPanelWidget`)

| UC | UC-003, UC-004 |

```mermaid
flowchart TB
  C[ChartPanelWidget]
  C --> Bar[QHBoxLayout toolbar]
  Bar --> SymbolCombo[QComboBox]
  Bar --> IntervalGroup[QButtonGroup QPushButton x3]
  Bar --> IndicatorCombo[QComboBox]
  C --> Chart[QChartView price_chart]
  C --> Legend[QLabel overlay_legend]
  C --> Footer[TierFooterWidget]
```

Day 모드: 동일 `ChartPanelWidget` 인스턴스를 `DayWorkspace` 좌측에 embed; 밴드는 `QLineSeries` 2개 추가.

---

## SCR-ORDER — 주문 (`OrderTicketWidget` in `QDockWidget`)

| UC | UC-002, UC-004, UC-006 |

```mermaid
flowchart TB
  Dock[QDockWidget order_dock width_400]
  Dock --> Ticket[OrderTicketWidget]
  Ticket --> Side[QButtonGroup buy_sell]
  Ticket --> TypeCombo[QComboBox]
  Ticket --> PriceSpin[QDoubleSpinBox]
  Ticket --> QtySpin[QSpinBox]
  Ticket --> ApplyQuote[QPushButton]
  Ticket --> PrefillBanner[QLabel prefill_from_proposal]
  Ticket --> Submit[QPushButton submit_order_btn]
  Ticket --> Footer[TierFooterWidget]
```

```mermaid
sequenceDiagram
  participant U as User
  participant T as OrderTicketWidget
  participant R as RiskGuardDialog
  participant K as OrderPort
  U->>T: submit_order_btn_clicked
  alt profile_live
    T->>R: exec_
    R-->>T: Accepted
  end
  T->>K: place_order
```

---

## SCR-HISTORY — 거래·손익 (`HistoryPanelWidget`)

| UC | UC-008 |

```mermaid
flowchart TB
  H[HistoryPanelWidget]
  H --> Filters[QHBoxLayout period_combo symbol_filter export_btn]
  H --> Tabs[QTabWidget]
  Tabs --> Fills[QTableView fills_table]
  Tabs --> Orders[QTableView orders_table]
  Tabs --> Pnl[QTableView pnl_table]
  Tabs --> Audit[QTableView audit_table]
```

`audit_table` 필터: `ai_proposal`, `ai_approval`, `daytrade_suggestion`.

---

## SCR-MKT / SCR-NEWS — 시장·뉴스

| UC | UC-009, UC-012 |

```mermaid
flowchart TB
  M[MarketInfoWidget]
  M --> FilterBar[QComboBox source_filter tier_filter]
  M --> Grid[QScrollArea cards_grid]
  M --> Legend[QTextBrowser tier_legend]
  M --> NewsTab[QTabWidget]
  NewsTab --> NewsList[QListView news_list]
```

`NewsList` 항목: `QStandardItem` + role `tier`, `published_at`.

---

**다음**: [UI-002-storyboards-trading-modes.md](UI-002-storyboards-trading-modes.md)
