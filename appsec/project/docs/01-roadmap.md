# 01 — Roadmap (phased build)

Build in thin, shippable releases. Each release is a git tag. Do not start a release before
the previous one works end to end. Target: 8–12 weeks part-time.

Legend: each phase lists **deliverables** and the **evidence** committed to the repo.

## v0.1 — Application (week 1–2)

- Deliverables: FastAPI backend, PostgreSQL, Redis, JWT auth; endpoints for register,
  login, users/me, accounts, transfers, transactions, beneficiaries, admin; `docker-compose.yml`;
  minimal React frontend (optional at this stage).
- Evidence: running stack via `make up`; OpenAPI schema at `/docs`.
- Guardrail: keep it small. Enough surface to host real vulnerabilities, no more.

## v0.2 — Threat model (week 2)

- Deliverables: complete [`security/threat-model/`](../security/threat-model/) 01–07;
  STRIDE threat register; risk ratings; mitigations mapped to planned controls.
- Evidence: DFD, trust boundaries, threat table, residual-risk note.

## v0.3 — SAST (week 3)

- Deliverables: intentionally introduce code vulnerabilities (catalog
  [`docs/05`](05-vulnerability-catalog.md)); Semgrep (and/or CodeQL) in CI on PRs; PR gate.
- Evidence: tags `v0.3-sast-vulnerable` and `v0.3-sast-remediated`; `reports/sast/` before &amp; after.

## v0.4 — SCA (week 4)

- Deliverables: pin intentionally vulnerable dependencies; pip-audit + Trivy; SBOM (Syft);
  prioritize by CVSS + EPSS + reachability; remediation.
- Evidence: `reports/sca/`, `reports/sbom/`; remediation commits; prioritization write-up.

## v0.5 — Secret scanning (week 5)

- Deliverables: Gitleaks in CI + pre-commit; fake secrets; git-history persistence demo on
  a dedicated branch; rotation procedure.
- Evidence: `reports/secrets/`; documented history scan; `.pre-commit-config.yaml`.

## v0.6 — DAST (week 6)

- Deliverables: deploy via compose in CI; OWASP ZAP baseline + authenticated + API scan;
  validate findings; before/after.
- Evidence: `reports/dast/` before &amp; after; ZAP config under `scanners/dast/`.

## v0.7 — DevSecOps pipeline (week 7–8)

- Deliverables: unified GitHub Actions pipeline (secrets → SAST → SCA → IaC → build →
  container scan → deploy → DAST → gate); IaC scanning (Checkov/tfsec/Trivy); container
  scanning (Trivy).
- Evidence: green pipeline; gate blocking a deliberately failing PR.

## v0.8 — AppSec platform (week 9–10)

- Deliverables: normalized findings inventory (schema); risk-based security gates; SLAs;
  metrics (counts, MTTR, SLA compliance, gate pass/fail); static dashboard/report.
- Evidence: `security/vulnerability-management/findings.json`; metrics report; gate policy.

## v1.0 — Production-like (week 11–12, stretch)

- Deliverables: Terraform and/or Kubernetes manifests (scanned); SBOM distribution;
  supply-chain controls (pinned actions, SLSA provenance, OpenSSF Scorecard); complete docs.
- Evidence: IaC under `infrastructure/`; provenance/attestation; `docs/` complete.

## First thin slice (do this before breadth)

Take **IDOR on `/api/transactions/{id}`** end to end: threat-model entry → vulnerable code
→ SAST (note it only *hints* at authorization gaps) → DAST (confirms IDOR) → fix
(object-level authorization) → unit test → DAST regression → closed in the inventory.
This validates the whole loop on one finding before you scale out. Template:
[`docs/06-demo-playbook.md`](06-demo-playbook.md).
