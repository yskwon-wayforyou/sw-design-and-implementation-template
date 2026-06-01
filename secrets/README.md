# KIS 자격증명 (암호화) — ADR-006

| TraceID | SEC-README-001 |

**Git에 평문 키를 넣지 마세요.**

## 1. 최초 설정 (오너 PC)

1. `plain/kis_credentials.json` 작성 (`kis_credentials.json.example` 참고)
2. `pip install cryptography`
3. 암호화:

```bash
python3 scripts/encrypt_secrets.py \
  --copy-to resources/secrets.enc \
  --copy-to android/app/src/main/assets/secrets.enc
```

4. 앱 복호화용 키 임베드(개인 빌드):

```bash
python3 scripts/embed_key.py
```

5. macOS 런타임 복사(선택):

```bash
mkdir -p ~/.YSTrading
cp secrets/secrets.enc ~/.YSTrading/secrets.enc
```

## 2. 파일

| 경로 | 설명 |
|------|------|
| `plain/kis_credentials.json` | **gitignore** — 평문 |
| `.master.key` | **gitignore** — AES 키 (base64) |
| `secrets.enc` | 암호화 blob (저장소 포함 가능, 키 없으면 무용) |
| `resources/secrets.enc` | macOS 번들용 |
| `android/.../assets/secrets.enc` | Android APK |

## 3. 환경 변수 (대안)

```bash
export YST_SECRETS_KEY="$(python3 -c 'import base64,secrets; print(base64.urlsafe_b64encode(secrets.token_bytes(32)).decode())')"
python3 scripts/encrypt_secrets.py --use-env-key
```

## 4. Python API

```python
from yst_credentials import load_credentials

creds = load_credentials()
key, secret, acct = creds.for_profile("paper")
```

## 5. 키 유출 시

한국투자증권 Open API 포털에서 **앱키 재발급** 후 1~3 단계 반복.
