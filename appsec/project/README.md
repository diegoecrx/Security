# SecureBank — End-to-End AppSec Platform

An intentionally vulnerable banking/payment application used to design and operate a
complete Application Security program: **threat modeling → SAST → SCA → secret scanning
→ CI/CD security → DAST**, with risk-based security gates, SBOM generation, and
vulnerability management with measurable remediation SLAs.

> **Status:** scaffolding. See [`docs/01-roadmap.md`](docs/01-roadmap.md) for the phased plan.

---

## ⚠️ Safety notice

This repository **intentionally contains vulnerabilities and fake credentials** for
education and demonstration. Rules:

- **Run locally only.** Never deploy to a public/internet-facing host.
- **No real secrets, ever.** All credentials are fake placeholders (see `.env.example`).
- Keep the real `.env` out of git (it is `.gitignore`d).
- Intentional vulnerabilities are catalogued in [`docs/05-vulnerability-catalog.md`](docs/05-vulnerability-catalog.md)
  and isolated per git branch/tag so the before/after state is reproducible.

---

## What this demonstrates

| Capability | Where |
|---|---|
| Threat modeling (STRIDE, DFD, risk register) | [`security/threat-model/`](security/threat-model/) |
| SAST | `.github/workflows/security.yml`, [`scanners/sast/`](scanners/sast/) |
| SCA (CVE + EPSS + reachability, SBOM) | [`scanners/sca/`](scanners/sca/), `reports/sbom/` |
| Secret scanning (incl. git history) | [`scanners/secrets/`](scanners/secrets/) |
| DAST (authenticated, API) | `.github/workflows/dast.yml`, [`scanners/dast/`](scanners/dast/) |
| IaC & container security | [`infrastructure/`](infrastructure/), `security.yml` |
| Risk-based security gates | [`security/security-gates/`](security/security-gates/) |
| Vulnerability management (inventory, SLA, metrics) | [`security/vulnerability-management/`](security/vulnerability-management/) |

Design and reasoning behind each control are in the companion reference set one level up
(`../SAST.html`, `../DAST.html`, `../SCA.html`, `../Secret-Scanning.html`,
`../CICD-Security.html`, `../Threat-Modeling.html`, `../OAuth-OIDC-JWT.html`).

## Architecture

See [`docs/02-architecture.md`](docs/02-architecture.md). In summary: developer → GitHub
(PR) → CI security gates (secrets, SAST, SCA, IaC) → build + container scan + SBOM →
deploy (docker-compose) → DAST → security gate → report.

## Documentation index

| Document | Purpose |
|---|---|
| [`docs/00-project-review.md`](docs/00-project-review.md) | Critical review, realism assessment, improvements |
| [`docs/01-roadmap.md`](docs/01-roadmap.md) | Phased build plan (v0.1 → v1.0) with tasks |
| [`docs/02-architecture.md`](docs/02-architecture.md) | Components, data flows, attack surface |
| [`docs/03-portability.md`](docs/03-portability.md) | Working across two machines; reproducible env |
| [`docs/04-tooling.md`](docs/04-tooling.md) | The free/OSS toolchain and how to run each tool |
| [`docs/05-vulnerability-catalog.md`](docs/05-vulnerability-catalog.md) | Intentional vulnerabilities (CWE/STRIDE/fix) |
| [`docs/06-demo-playbook.md`](docs/06-demo-playbook.md) | Attack → detection → remediation template |

## Quick start (once the application exists)

```bash
git clone <your-remote> securebank && cd securebank
cp .env.example .env            # fill in fake/local values
make up                         # start app + db + redis (docker compose)
make scan                       # run the local security scans
```

Prerequisites and the two-machine setup: [`docs/03-portability.md`](docs/03-portability.md).

## Licence

MIT (code). See [`LICENSE`](LICENSE). Intentional vulnerabilities are for demonstration
only; use at your own risk and only in isolated local environments.
