# Scanners

Tool configuration lives here; outputs are written to `../reports/<type>/`. Tools and
invocation: [`../docs/04-tooling.md`](../docs/04-tooling.md). Local run: `make scan` (static)
and `make dast` (dynamic, needs `make up`).

| Folder | Tool(s) | Output |
|---|---|---|
| `sast/` | Semgrep (+ optional CodeQL) | `reports/sast/` |
| `sca/` | pip-audit, Trivy, Syft (SBOM) | `reports/sca/`, `reports/sbom/` |
| `dast/` | OWASP ZAP (+ optional Nuclei) | `reports/dast/` |
| `secrets/` | Gitleaks (+ GitHub secret scanning) | `reports/secrets/` |

Normalize outputs into the inventory:
[`../security/vulnerability-management/finding-schema.md`](../security/vulnerability-management/finding-schema.md).
