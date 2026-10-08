# 07 — Residual risk

Risk remaining after mitigations are implemented, formally recorded and accepted by an
owner. Scoring rubric: Likelihood (Low/Med/High) &times; Impact (Low/Med/High) → Risk.

| ID | Residual risk | Likelihood | Impact | Rating | Decision | Owner |
|---|---|---|---|---|---|---|
| R1 | Zero-day in a maintained dependency | Low | High | Medium | Accept; monitor via SCA + alerts | AppSec |
| R2 | Business-logic abuse not covered by automated tests | Med | High | High | Mitigate via periodic manual review | AppSec |
| R3 | Compromise of a developer machine / token | Low | High | Medium | Accept; OIDC short-lived creds, MFA | Platform |
| R4 | Misconfiguration introduced after scan | Low | Med | Low | Accept; continuous IaC scanning | Platform |

Residual-risk acceptances are reviewed each release. New threats discovered during build
are added to [05-threats.md](05-threats.md) and re-assessed.
