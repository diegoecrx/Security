# 04 — Tooling (free / open-source)

All automated tooling is free and CI-capable. Paid tools (e.g. Burp Suite Professional)
are optional for manual exploration only and are never required by the pipeline.

| Stage | Tool | Role | Invocation |
|---|---|---|---|
| Secret scanning | **Gitleaks** | Repo + history + pre-commit | `gitleaks detect`; `gitleaks/gitleaks-action` |
| SAST | **Semgrep** | Pattern/dataflow code analysis | `semgrep ci`; container `semgrep/semgrep` |
| SAST (alt) | **CodeQL** | GitHub-native dataflow | `github/codeql-action` |
| SCA (Python) | **pip-audit** | Dependency CVEs | `pip-audit`; `pypa/gh-action-pip-audit` |
| SCA / container / IaC | **Trivy** | Deps, images, IaC, secrets | `aquasecurity/trivy-action` |
| SCA (alt) | **OWASP Dependency-Check** | Dependency CVEs | CLI / action |
| SBOM | **Syft** | Generate SPDX/CycloneDX | `anchore/sbom-action` |
| SBOM vuln match | **Grype** | Scan an SBOM/image | `anchore/scan-action` |
| IaC | **Checkov**, **tfsec** | Terraform/compose/K8s misconfig | `bridgecrewio/checkov-action` |
| DAST | **OWASP ZAP** | Baseline, authenticated, API scan | `zaproxy/action-baseline`, `action-api-scan` |
| DAST (templated) | **Nuclei** | Templated vulnerability checks | `projectdiscovery/nuclei` |
| Vuln management | **OWASP DefectDojo** (optional) | Aggregation, SLA, dashboard | self-hosted (v0.8+) |
| Dependency updates | **Dependabot / Renovate** | Automated upgrade PRs | native config |
| Supply chain | **Sigstore cosign**, **OpenSSF Scorecard** | Signing, provenance, posture | actions (v1.0) |

## Local vs CI

- **Local** (fast feedback via `make`): Gitleaks, Semgrep, pip-audit/Trivy run against the
  working tree; ZAP baseline against `make up`.
- **CI** (gate of record): the same tools run in GitHub Actions on every PR; results are
  committed to `reports/` and fed to the security gate.

## Output normalization

Prefer **SARIF** output where the tool supports it (Semgrep, CodeQL, Trivy, Gitleaks) so
findings load into GitHub's "Security" tab and normalize consistently. Tools without SARIF
emit JSON that the vulnerability-management normalizer maps to the common schema
([`security/vulnerability-management/finding-schema.md`](../security/vulnerability-management/finding-schema.md)).

## Install (local, Windows-native option)

Pinned, portable binaries where possible (no WSL required):

```
# examples — pin versions in practice
pipx install semgrep
pipx install pip-audit
winget install aquasecurity.trivy        # or download the release binary
winget install Gitleaks.Gitleaks         # or release binary
# OWASP ZAP: download the cross-platform package; run zap.sh/ZAP.exe or the Docker image
```

In Codespaces or the devcontainer, these are preinstalled via the container definition.
