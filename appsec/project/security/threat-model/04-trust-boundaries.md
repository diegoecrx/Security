# 04 — Trust boundaries

| ID | Boundary | Crossing data | Primary threats |
|---|---|---|---|
| TB1 | Internet → API | Credentials, requests, tokens | Spoofing, injection, DoS |
| TB2 | API → PostgreSQL | Queries, PII, financial data | SQL injection, data exposure |
| TB3 | API → Redis | Session/rate state | Session/state tampering |
| TB4 | User → Admin (in API) | Privileged operations | Elevation of privilege, broken authz |
| TB5 | CI/CD → build/deploy | Source, dependencies, images, secrets | Supply-chain, poisoned pipeline, secret leak |

Controls are assigned per boundary in [06-mitigations.md](06-mitigations.md).
