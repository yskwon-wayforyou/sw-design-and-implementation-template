#!/usr/bin/env python3
"""Encrypt KIS credentials JSON → secrets.enc (ADR-006). Never commit plain input."""
from __future__ import annotations

import argparse
import base64
import json
import os
import secrets
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PLAIN = ROOT / "secrets" / "plain" / "kis_credentials.json"
DEFAULT_OUT = ROOT / "secrets" / "secrets.enc"
DEFAULT_KEY_FILE = ROOT / "secrets" / ".master.key"


def _load_or_create_key(key_file: Path, from_env: bool) -> bytes:
    env = os.environ.get("YST_SECRETS_KEY")
    if from_env and env:
        raw = base64.urlsafe_b64decode(env.encode("ascii"))
        if len(raw) != 32:
            raise SystemExit("YST_SECRETS_KEY must decode to 32 bytes (urlsafe base64)")
        return raw
    if key_file.exists():
        return base64.urlsafe_b64decode(key_file.read_text().strip().encode("ascii"))
    raw = secrets.token_bytes(32)
    key_file.parent.mkdir(parents=True, exist_ok=True)
    key_file.write_text(base64.urlsafe_b64encode(raw).decode("ascii"))
    print(f"Created master key: {key_file} (gitignored — back up locally)", file=sys.stderr)
    return raw


def encrypt(plaintext: bytes, key: bytes) -> bytes:
    try:
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    except ImportError as e:
        raise SystemExit("pip install cryptography") from e

    nonce = secrets.token_bytes(12)
    ct = AESGCM(key).encrypt(nonce, plaintext, None)
    return b"YST1" + nonce + ct


def main() -> None:
    p = argparse.ArgumentParser(description="Encrypt KIS credentials (ADR-006)")
    p.add_argument("--input", type=Path, default=DEFAULT_PLAIN)
    p.add_argument("--output", type=Path, default=DEFAULT_OUT)
    p.add_argument("--key-file", type=Path, default=DEFAULT_KEY_FILE)
    p.add_argument("--use-env-key", action="store_true", help="Use YST_SECRETS_KEY only")
    p.add_argument(
        "--copy-to",
        type=Path,
        action="append",
        default=[],
        help="Additional output paths (e.g. android assets)",
    )
    args = p.parse_args()

    if not args.input.exists():
        raise SystemExit(f"Missing {args.input} — create from kis_credentials.json.example")

    key = _load_or_create_key(args.key_file, args.use_env_key)
    data = args.input.read_bytes()
    json.loads(data.decode("utf-8"))  # validate

    blob = encrypt(data, key)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(blob)
    print(f"Wrote {args.output} ({len(blob)} bytes)")

    for dest in args.copy_to:
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(blob)
        print(f"Copied → {dest}")


if __name__ == "__main__":
    main()
