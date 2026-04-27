---
description: 배포/릴리스 준비(패키징, 설치 프로그램, 릴리스 체크리스트)를 설계 문서와 스크립트로 정리하도록 안내합니다.
---

# /productization/prepare-deployment

## 산출 위치

설계·분석 산출물은 **현재 단위 프로젝트 루트의 `docs/`** 아래에만 둔다.

## 목표

- `docs/deployment.md`에 “실행 가능한 절차”를 남긴다(빌드/롤백/관측/보안 포함).
- 데스크톱 앱의 경우: 패키징(Python이면 PyInstaller)과 설치 프로그램(선택)을 준비한다.
