---
name: python-qt6-commercial-app
description: Build a commercial-quality Python Qt6 GUI app: venv workflow, project structure, testing, packaging (PyInstaller), Windows installer prep, and docs alignment under docs/.
---

# Python + Qt6 상용급 데스크톱 앱 스킬

## 목적

사용자가 짧은 제품 기술만 제공해도, **상용 제품 수준**의 데스크톱 앱을 **설계→구현→테스트→배포 준비**까지 한 사이클로 밀어준다.

이 스킬은 다음을 “기본값”으로 제안한다.

- **가상환경**: `venv` (프로젝트 루트에 `.venv/`)
- **Qt 바인딩**: 기본은 **PySide6(Qt6)** (라이선스/상용 적합성 관점)
- **품질 게이트**: `pytest` + `ruff` + (선택) `mypy`
- **패키징**: `pyinstaller`로 `.exe` 생성 + (선택) Inno Setup 스크립트로 설치 파일 준비
- **문서 위치**: 설계 산출은 `{프로젝트루트}/docs/**`에만 둔다

## 1) 프로젝트 스캐폴드(권장 트리)

```
<project>/
  docs/
    system.md
    business.md
    usecases.md
    usecase/
    domain/
    quality/
    architecture.md
    deployment.md
    asr.md
    adr/
  src/
    <app_package>/
      __init__.py
      app.py
      ui/
      domain/
      services/
      infrastructure/
  tests/
  scripts/
  installer/
  pyproject.toml
  README.md
```

## 2) venv(필수) 가이드 — Windows PowerShell

프로젝트 루트에서:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e .[dev]
```

## 3) 개발 품질 기준(최소)

- `ruff`는 **CI에서 실패**하게(형식/정적 분석)
- `pytest`는 핵심 도메인 로직을 최소 커버
- GUI는 전부 테스트하지 않더라도, **도메인/서비스 계층**은 테스트로 고정

## 4) PyInstaller(배포 준비)

필수 산출:

- `scripts/build.ps1`: 빌드 1-클릭 스크립트
- `installer/` 아래: 설치 프로그램(선택) 스크립트 초안
- `docs/deployment.md`: 빌드/릴리스/롤백/헬스/관측/보안 포함 목차(템플릿 룰 준수)

## 5) 상용 제품 체크(문서에 남길 것)

- SLO/지원/업데이트 정책(자동 업데이트 여부 포함)
- 에러 리포팅/로그(개인정보 마스킹 포함)
- 의존성 라이선스/고지(OSS 사용 시)

