# Secret scanning

Tools: **Gitleaks** (CLI, CI, pre-commit) and **GitHub Secret Scanning + Push Protection**.

## Pre-commit (prevent at source)
Add `.pre-commit-config.yaml` at the repo root:
```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.4
    hooks:
      - id: gitleaks
```
Then `pre-commit install`.

## Git-history persistence demo (APP-006)
Demonstrate why deleting a secret from the current file is insufficient:
1. On a dedicated, clearly-labelled branch, commit an **obviously-fake** secret.
2. Commit again removing it from the file.
3. Run `gitleaks detect` (scans full history) — the secret is still found in the earlier commit.
4. Document rotation as the real remediation.

## Caution
GitHub push protection may block pushing realistic-looking secrets. Use non-matching, clearly
fake placeholders for committed examples, and keep the history demo on a throwaway/demo branch
(or a local-only repo) so it is reproducible without fighting the platform.

Reference: [`../../../Secret-Scanning.html`](../../../Secret-Scanning.html).
