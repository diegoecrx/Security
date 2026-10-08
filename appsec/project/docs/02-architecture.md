# 02 — Architecture

## Components

| Layer | Technology | Notes |
|---|---|---|
| Backend API | Python 3.12 + FastAPI | JWT auth; the primary attack surface |
| Database | PostgreSQL 16 | Accounts, transactions, users, audit |
| Cache / session | Redis 7 | Rate-limit counters, token/session state |
| Frontend | React + TypeScript (optional early) | Thin client over the API |
| Runtime | Docker + Docker Compose | Kubernetes/Terraform in v1.0 |

## Pipeline (security flow)

```
Developer ──PR──▶ GitHub
                   │
                   ▼
        ┌───────────────────────────┐
        │  CI: pre-deploy gates      │
        │  1. Secret scanning        │  (Gitleaks)
        │  2. SAST                   │  (Semgrep / CodeQL)
        │  3. SCA + SBOM             │  (pip-audit, Trivy, Syft)
        │  4. IaC scanning           │  (Checkov / tfsec / Trivy)
        └───────────┬───────────────┘
                    ▼
           Build image ──▶ Container scan (Trivy)
                    │
                    ▼
        Deploy (docker compose) ──▶ DAST (OWASP ZAP: baseline + authenticated + API)
                    │
                    ▼
        Normalize findings ──▶ Risk-based security gate
                    │
             ┌──────┴──────┐
            PASS          FAIL (block)
```

## API surface (intentional attack surface)

```
POST   /api/auth/register
POST   /api/auth/login
GET    /api/users/me
GET    /api/accounts
GET    /api/accounts/{id}
POST   /api/transfers
GET    /api/transactions
GET    /api/transactions/{id}
POST   /api/beneficiaries
DELETE /api/beneficiaries/{id}
GET    /api/admin/users
GET    /api/admin/audit
```

## Trust boundaries

1. **Internet → API** — unauthenticated and authenticated client traffic.
2. **API → database** — queries; injection and data-exposure boundary.
3. **API → Redis** — session/rate-limit state.
4. **User → Admin** — privilege boundary (RBAC enforcement point).
5. **CI → registry/deploy** — build and supply-chain boundary.

## Assets

User credentials; JWT signing secret; account and transaction data; PII; the database;
admin functionality; API and infrastructure credentials. Full register:
[`security/threat-model/03-assets.md`](../security/threat-model/03-assets.md).

## Data flow (login + transfer)

```
User ─creds─▶ /auth/login ─verify─▶ DB ─issue JWT─▶ User
User ─JWT + transfer─▶ /transfers ─authz check─▶ DB (debit/credit) ─▶ audit log
```

Threats concentrate at the authorization check in `/transfers` and the object lookup in
`/transactions/{id}` and `/accounts/{id}` (IDOR / broken object-level authorization).
