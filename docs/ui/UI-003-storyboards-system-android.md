# 화면 콘티 — 설정·승인·Android·예외 (PySide6 + WebView)

| TraceID | UI-003 |
|---------|------------|
| Qt6 정본 (macOS) | [UI-QT6-layout-conventions.md](UI-QT6-layout-conventions.md) |
| O-01·O-02 확정 | [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) (배경 [DEC-003](../decision/DEC-003-open-issues-guide.md)) |

도식은 **Mermaid만** 사용합니다.

---

## SCR-SETTINGS — `SettingsDialog`

| 진입 | `settings_btn` · `QAction` Preferences |

```mermaid
flowchart TB
  S[SettingsDialog QDialog size_900x600]
  S --> Split[QSplitter]
  Split --> Nav[QListWidget settings_nav]
  Split --> Stack[QStackedWidget settings_pages]
  Nav --> P0[AccountPage]
  Nav --> P1[AiPolicyPage]
  Nav --> P2[DaytradePage]
  Nav --> P3[DataPage]
  Nav --> P4[AndroidPage]
  Nav --> P5[AdvancedPage]
```

### 페이지별 Qt6 위젯

| 페이지 | 주요 위젯 |
|--------|-----------|
| Account | `QRadioButton` paper/live · `QPushButton` test_connection · `QLabel` kis_status |
| AI 매매 | `QCheckBox` ai_auto_without_approval · `QSpinBox` ai_approval_ttl_sec |
| 단타 | `QComboBox` daytrade_sensitivity · `QSpinBox` daytrade_auto_refresh_sec |
| 데이터 | `QCheckBox` show_tier_badges · `QCheckBox` use_websocket |
| Android | `QLineEdit` sync_hub_url · `QPushButton` open_pairing_wizard → SCR-AND-PAIR |
| 고급 | `QPlainTextEdit` log_path_readonly |

```mermaid
flowchart LR
  AutoCheck[ai_auto_without_approval toggled On]
  AutoCheck --> Warn[QMessageBox warning]
  Warn --> Audit[EventStore ai_policy_change]
```

---

## SCR-APPROVAL — `ApprovalDialog`

| UC | UC-006, UC-010 |

```mermaid
flowchart TB
  D[ApprovalDialog QDialog minWidth_480]
  D --> Header[QHBoxLayout title TTL_Label]
  D --> Summary[QGroupBox order_summary]
  Summary --> Side[QLabel BUY_or_SELL]
  Summary --> Symbol[QLabel]
  Summary --> Qty[QLabel]
  D --> Confidence[QLabel]
  D --> Rationale[QGroupBox checkable]
  Rationale --> FeatureList[QTableWidget 3rows]
  Rationale --> Similar[QLabel]
  D --> Footer[TierFooterWidget]
  D --> Buttons[QDialogButtonBox reject defer approve]
```

| `QDialogButtonBox` | 역할 |
|--------------------|------|
| Approve | `ApprovalGate.approve` → `RiskGuardDialog` if live |
| Reject | `QComboBox` reject_reason |
| Defer | close, queue 유지 |

```mermaid
sequenceDiagram
  participant Mac as MainWindow
  participant Badge as QToolButton approval_badge
  participantDlg as ApprovalDialog
  Mac->>Badge: setText count
  Badge->>Dlg: clicked show queue pick
  Dlg->>Dlg: user Approve
```

---

## SCR-RISK — `RiskGuardDialog`

| UC | UC-011 |

```mermaid
flowchart TB
  R[RiskGuardDialog QDialog]
  R --> Icon[QLabel warning_pixmap]
  R --> Title[QLabel live_order_confirm]
  R --> Body[QFormLayout symbol side qty price]
  R --> Amount[QLabel estimated_amount]
  R --> SkipCheck[QCheckBox skip_today_not_recommended]
  R --> Box[QDialogButtonBox Cancel Execute]
```

| 트리거 | 호출 위치 |
|--------|-----------|
| live 주문 | `OrderTicketWidget.submit` |
| AI 무승인 실행 | `AiAutoService.execute` |

---

## SCR-AND-PAIR — Android 페어링 (macOS 측 Qt6)

| UC | UC-010 |
|----|--------|
| O-01 | **확정** LAN + 페어링 토큰 — [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |

```mermaid
flowchart TB
  P[PairingDialog QDialog]
  P --> Url[QLabel hub_url_copyable]
  P --> QR[QLabel qr_pixmap from qrcode]
  P --> Code[QLabel pairing_code large]
  P --> Timer[QLabel code_expires_in]
  P --> Status[QLabel device_connected_count]
  P --> RegenBtn[QPushButton regenerate_code_btn]
```

```mermaid
sequenceDiagram
  participant Mac as SyncHub
  participant Phone as Android
  Mac->>Mac: generate token T
  Phone->>Mac: POST /pair token=T
  Mac-->>Phone: session_token
  Phone->>Mac: API calls with X-Session-Token
```

---

## SCR-AND-SHELL — Android (WebView / 간소 Qt)

Android 네이티브 전체 Qt는 v1 범위 밖; **WebView + HTML** 또는 **Qt Quick** 중 택일은 구현 Phase.

```mermaid
flowchart TB
  subgraph Android[Android_Activity]
    AppBar[MaterialToolbar profile_chip]
    Web[QWebEngineView or WebView sync_hub_ui]
    Nav[BottomNavigationView]
  end
  Nav --> TabHome[home]
  Nav --> TabAppr[approvals]
  Nav --> TabOrder[order]
  Nav --> TabSet[settings]
```

| 탭 | 내용 |
|----|------|
| home | 잔고·관심 JSON render |
| approvals | pending list → SCR-AND-APPROVAL |
| order | 간소 form POST `/orders` |
| settings | read-only profile |

**O-02 알림**: **확정** 폴링 15초 + 로컬 알림 — [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md).

```mermaid
flowchart LR
  subgraph v1 [v1_폴링]
    Timer[WorkManager 15s]
    API[GET approvals_pending]
    Notif[NotificationCompat]
    Timer --> API --> Notif
  end
```

---

## SCR-AND-APPROVAL — Android 승인 화면

```mermaid
flowchart TB
  A[ApprovalFragment or WebView page]
  A --> TTL[TextView countdown]
  A --> Summary[TextView]
  A --> Rationale[TextView collapsed]
  A --> Reject[Button]
  A --> Approve[Button primary]
```

---

## SCR-OFFLINE — 연결 끊김

| 진입 | KIS/WS/SyncHub fail |

```mermaid
stateDiagram-v2
  [*] --> Online
  Online --> Degraded: ws_down_rest_ok
  Online --> Offline: kis_auth_fail
  Degraded --> Online: ws_restored
  Offline --> Online: retry_ok
```

macOS: `QMessageBox` 또는 `OfflineOverlay` `QWidget` on `workspace_stack`.

| 모드 | `QPushButton` |
|------|----------------|
| 조회만 | `offline_readonly_btn` — 캐시 model |
| 주문 | `submit_order_btn.setEnabled false` |

---

## SCR-ERROR — 피드백

| 유형 | Qt6 |
|------|-----|
| 일반 | `QStatusBar.showMessage` 5s |
| 심각 | `QMessageBox.critical` |
| 주문 TR 거부 | `QMessageBox` + `QPushButton` copy audit id |

---

## MVP 화면 목록

```mermaid
mindmap
  root((MVP_Screens))
    Onboarding
      SCR_000
      SCR_001
      SCR_002
    Shell_Common
      SCR_SHELL
      SCR_HOME
      SCR_QUOTE
      SCR_CHART
      SCR_ORDER
      SCR_HIST
      SCR_MKT
    Modes
      SCR_MODE_DAY
      SCR_MODE_LONG
      SCR_MODE_AI
      SCR_ML
    System
      SCR_SETTINGS
      SCR_APPROVAL
      SCR_RISK
      SCR_OFFLINE
    Android
      SCR_AND_PAIR
      SCR_AND_SHELL
      SCR_AND_APPROVAL
```

---

**관련**: [ARC-003](../architecture/ARC-003-trading-modes-greenfield.md) · [ADR-005](../adr/ADR-005-greenfield-ui-and-modes.md)
