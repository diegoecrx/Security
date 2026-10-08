# 06 — Mitigations &amp; security requirements

Mitigations become testable security requirements, mapped to OWASP ASVS where applicable
(see [`../security-requirements/`](../security-requirements/)). Each is verified by a
control (SAST/DAST/test) and tracked to closure in the inventory.

| Threat | Requirement | Verified by |
|---|---|---|
| T1 | Login enforces rate limiting and account lockout | DAST, integration test |
| T2 | All DB access uses parameterized queries | SAST, DAST |
| T3 | JWT signature verified; algorithm pinned; `none` rejected | SAST, unit test |
| T4 | Every object access checks ownership (object-level authz) | DAST, unit test |
| T5 | Admin routes enforce RBAC | DAST, unit test |
| T6 | All user-controlled output is context-encoded; CSP set | DAST, SAST |
| T7 | Outbound fetch targets allow-listed; internal ranges blocked | SAST, DAST |
| T8 | No secrets in source; secrets from env/vault; rotation runbook | Secret scanning |
| T9 | Dependencies scanned; criticals remediated; SBOM produced | SCA |
| T10 | Third-party actions pinned to commit hash; least-privilege jobs; OIDC | CI config review |
| T11 | Passwords hashed (argon2/bcrypt); no sensitive data in errors; encryption at rest | SAST, DAST |
| T12 | Security headers and secure cookie flags set | DAST |
| T13 | Security-relevant actions are audit-logged | Integration test |
| T14 | Expensive operations are paginated and rate-limited | DAST |

Residual (accepted) risk after mitigation: [07-residual-risk.md](07-residual-risk.md).
