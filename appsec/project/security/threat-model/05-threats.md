# 05 — Threats (STRIDE)

Threats enumerated per component/boundary. Risk = likelihood &times; impact. Each maps to a
mitigation ([06](06-mitigations.md)) and, where implemented as an intentional vulnerability,
to the catalog ([`../../docs/05-vulnerability-catalog.md`](../../docs/05-vulnerability-catalog.md)).

| # | Component | Threat | STRIDE | Risk | Mitigation | Catalog |
|---|---|---|---|---|---|---|
| T1 | Login API | Credential brute force | Spoofing | High | Rate limiting, lockout | APP-004 |
| T2 | Login/DB | SQL injection | Tampering | Critical | Parameterized queries | APP-001 |
| T3 | JWT | Token forgery / `alg:none` | Spoofing | High | Verify signature; pin alg | APP-005 |
| T4 | Transactions API | IDOR (object-level authz) | Tampering/EoP | Critical | Object-level authorization | APP-002 |
| T5 | Admin API | Function-level authz bypass | EoP | Critical | RBAC enforcement | APP-003 |
| T6 | Profile/Beneficiary | XSS | Tampering | High | Output encoding; CSP | APP-007 |
| T7 | Beneficiary/webhook | SSRF | Info disclosure | High | URL allow-list; block internal | APP-008 |
| T8 | Source/CI | Hardcoded secret leak | Info disclosure | High | Secret scanning; vault; rotate | APP-006 |
| T9 | Dependencies | Known-vulnerable component | varies | High | SCA; upgrade | APP-014 |
| T10 | Pipeline | Poisoned pipeline / unpinned action | Tampering | Critical | Pin to hash; least privilege | — |
| T11 | Data at rest | Unhashed passwords; data exposure | Info disclosure | Critical | Hashing; encryption; error handling | APP-012 |
| T12 | Transport | Missing headers / cookie flags | Info disclosure | Medium | Security headers; cookie flags | APP-013 |
| T13 | Audit | Action repudiation | Repudiation | Medium | Audit logging | — |
| T14 | API | DoS via unbounded operations | DoS | Medium | Rate limiting; pagination; limits | — |

Likelihood/impact scoring rubric and residual risk in [07-residual-risk.md](07-residual-risk.md).
