"""Build HTML scenario test report with inline screenshots."""

from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any


def write_html_report(run_dir: Path, meta: dict[str, Any]) -> Path:
    steps = meta.get("steps") or []
    outcome = meta.get("outcome", "unknown")
    index_path = run_dir / "index.html"

    step_cards = []
    for s in steps:
        step_cards.append(_step_card_html(run_dir, s))

    body = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Scenario Report — {html.escape(meta.get('uc', ''))} {html.escape(outcome)}</title>
  <style>
    :root {{
      --pass: #1a7f37; --fail: #cf222e; --review: #9a6700; --bg: #f6f8fa;
    }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      margin: 0; background: var(--bg); color: #1f2328; line-height: 1.5; }}
    header {{ background: #fff; border-bottom: 1px solid #d0d7de; padding: 1.25rem 2rem; }}
    h1 {{ margin: 0 0 0.5rem; font-size: 1.35rem; }}
    .meta {{ font-size: 0.9rem; color: #656d76; }}
    .badge {{ display: inline-block; padding: 0.15rem 0.5rem; border-radius: 6px;
      font-size: 0.8rem; font-weight: 600; color: #fff; }}
    .badge.pass {{ background: var(--pass); }}
    .badge.fail {{ background: var(--fail); }}
    .badge.review {{ background: var(--review); }}
    .badge.inconclusive {{ background: #656d76; }}
    main {{ max-width: 960px; margin: 0 auto; padding: 1.5rem 2rem 3rem; }}
    .step {{ background: #fff; border: 1px solid #d0d7de; border-radius: 8px;
      margin-bottom: 1.25rem; overflow: hidden; }}
    .step-header {{ padding: 1rem 1.25rem; border-bottom: 1px solid #d0d7de; }}
    .step-header h2 {{ margin: 0; font-size: 1.05rem; }}
    .step-body {{ padding: 1rem 1.25rem; }}
    .shot {{ max-width: 100%; border: 1px solid #d0d7de; border-radius: 6px; cursor: pointer; }}
    .shot:hover {{ box-shadow: 0 4px 12px rgba(0,0,0,.12); }}
    dl {{ margin: 0.75rem 0 0; font-size: 0.9rem; }}
    dt {{ font-weight: 600; color: #656d76; margin-top: 0.5rem; }}
    dd {{ margin: 0.15rem 0 0; }}
    pre {{ background: #f6f8fa; padding: 0.75rem; overflow: auto; font-size: 0.8rem;
      border-radius: 6px; }}
    #lightbox {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,.85);
      z-index: 1000; align-items: center; justify-content: center; }}
    #lightbox.show {{ display: flex; }}
    #lightbox img {{ max-width: 95vw; max-height: 95vh; }}
  </style>
</head>
<body>
  <header>
    <h1>시나리오 테스트 리포트</h1>
    <p class="meta">
      UC: <strong>{html.escape(str(meta.get('uc', '')))}</strong> ·
      SCR: {html.escape(str(meta.get('scr', '')))} ·
      NBDE: {html.escape(str(meta.get('nbde', '')))} ·
      <span class="badge {html.escape(outcome)}">{html.escape(outcome.upper())}</span>
    </p>
    <p class="meta">
      run: {html.escape(run_dir.name)} ·
      git: {html.escape(str(meta.get('git_sha', '')))} ·
      {html.escape(str(meta.get('finished_at', '')))} ·
      {meta.get('duration_ms', 0)} ms
    </p>
    <p class="meta">test: {html.escape(str(meta.get('test_nodeid', '')))}</p>
  </header>
  <main>
    <section>
      <h2>단계별 진행 ({len(steps)} steps)</h2>
      {''.join(step_cards)}
    </section>
  </main>
  <div id="lightbox" onclick="this.classList.remove('show')">
    <img id="lightbox-img" alt="screenshot"/>
  </div>
  <script>
    document.querySelectorAll('.shot').forEach(img => {{
      img.addEventListener('click', () => {{
        const lb = document.getElementById('lightbox');
        document.getElementById('lightbox-img').src = img.src;
        lb.classList.add('show');
      }});
    }});
  </script>
</body>
</html>
"""
    index_path.write_text(body, encoding="utf-8")
    return index_path


def _step_card_html(run_dir: Path, s: dict[str, Any]) -> str:
    verdict = s.get("analysis_verdict", "inconclusive")
    assertion = s.get("assertion", "")
    shot_rel = s.get("screenshot", "")
    shot_html = ""
    if shot_rel:
        shot_path = run_dir / shot_rel
        if shot_path.exists():
            shot_html = f'<p><img class="shot" src="{html.escape(shot_rel)}" alt="step {s.get("index")}"/></p>'

    ui_json = html.escape(json.dumps(s.get("ui_snapshot") or {}, ensure_ascii=False, indent=2))
    err = s.get("error") or ""
    err_html = f"<pre>{html.escape(err)}</pre>" if err else ""

    return f"""
    <article class="step">
      <div class="step-header">
        <h2>Step {s.get('index')}: {html.escape(s.get('title', ''))}</h2>
        <span class="badge {html.escape(verdict)}">분석: {html.escape(verdict)}</span>
        <span class="badge {'pass' if assertion == 'pass' else 'fail'}">assert: {html.escape(assertion)}</span>
        <span class="meta"> {s.get('duration_ms', 0)} ms</span>
      </div>
      <div class="step-body">
        {shot_html}
        <dl>
          <dt>기대 동작</dt>
          <dd>{html.escape(s.get('expectation') or '—')}</dd>
          <dt>수행 로그</dt>
          <dd>{html.escape(s.get('action_log') or '—')}</dd>
          <dt>분석 메모</dt>
          <dd>{html.escape(s.get('analysis_notes') or '—')}</dd>
          <dt>UI 스냅샷</dt>
          <dd><pre>{ui_json}</pre></dd>
        </dl>
        {err_html}
      </div>
    </article>
    """
