# Reports

Committed scanner output, per type. Commit **before** and **after** states (e.g.
`*-before.json` / `*-after.json`, or rely on the `*-vulnerable` / `*-remediated` tags) so the
remediation story is evidence, not narrative. All before/after metrics in the docs must be
generated from these files, never hand-typed.

| Folder | Source |
|---|---|
| `sast/` | Semgrep / CodeQL |
| `sca/` | pip-audit, Trivy |
| `dast/` | OWASP ZAP |
| `sbom/` | Syft (CycloneDX/SPDX) |
| `secrets/` | Gitleaks |
