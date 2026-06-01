"""Load encrypted KIS credentials — memory only, no logging of secrets."""
from __future__ import annotations

import base64
import json
import os
from dataclasses import dataclass
from pathlib import Path

_MAGIC = b"YST1"


@dataclass(frozen=True)
class KisCredentials:
    paper_app_key: str
    paper_app_secret: str
    paper_account: str
    live_app_key: str
    live_app_secret: str
    live_account: str

    def for_profile(self, profile: str) -> tuple[str, str, str]:
        if profile == "paper":
            return self.paper_app_key, self.paper_app_secret, self.paper_account
        if profile == "live":
            return self.live_app_key, self.live_app_secret, self.live_account
        raise ValueError(f"unknown profile: {profile}")


def _resolve_master_key() -> bytes:
    env = os.environ.get("YST_SECRETS_KEY")
    if env:
        raw = base64.urlsafe_b64decode(env.encode("ascii"))
        if len(raw) != 32:
            raise ValueError("YST_SECRETS_KEY must be 32 bytes (urlsafe base64)")
        return raw
    # Build-time embedded obfuscated key (personal app); set by scripts/embed_key.py
    from yst_credentials._embedded import EMBEDDED_KEY_B64  # noqa: PLC2701

    return base64.urlsafe_b64decode(EMBEDDED_KEY_B64.encode("ascii"))


def _decrypt(blob: bytes, key: bytes) -> bytes:
    if not blob.startswith(_MAGIC):
        raise ValueError("invalid secrets.enc header")
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

    nonce = blob[4:16]
    ct = blob[16:]
    return AESGCM(key).decrypt(nonce, ct, None)


def load_credentials(path: Path | None = None) -> KisCredentials:
    if path is None:
        path = _default_secrets_path()
    blob = path.read_bytes()
    raw = json.loads(_decrypt(blob, _resolve_master_key()).decode("utf-8"))
    paper = raw.get("paper") or {}
    live = raw.get("live") or {}
    return KisCredentials(
        paper_app_key=str(paper.get("app_key", "")),
        paper_app_secret=str(paper.get("app_secret", "")),
        paper_account=str(paper.get("account", "")),
        live_app_key=str(live.get("app_key", "")),
        live_app_secret=str(live.get("app_secret", "")),
        live_account=str(live.get("account", "")),
    )


def _default_secrets_path() -> Path:
    home = Path.home() / ".YSTrading" / "secrets.enc"
    if home.exists():
        return home
    here = Path(__file__).resolve()
    for candidate in (
        here.parents[2] / "secrets" / "secrets.enc",
        here.parents[2] / "resources" / "secrets.enc",
    ):
        if candidate.exists():
            return candidate
    raise FileNotFoundError("secrets.enc not found — run scripts/encrypt_secrets.py")
