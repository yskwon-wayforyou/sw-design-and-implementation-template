# QS-019 — 공급망·의존성

| TraceID | QS-019 |
|---------|--------|

## 자극

릴리스 태그 `v1.0.0` 생성.

## 응답

- `requirements.txt` / lock 해시 고정
- SBOM artifact 첨부(GitHub Release)
- `pip audit` high **0** (또는 documented exception)

## 허용 기대

- 재현 가능 빌드
- 알려진 critical CVE 미패치 **0건** (릴리스 시)

## 측정

- CI: lockfile drift check
- release workflow SBOM step
