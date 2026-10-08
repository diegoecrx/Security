# 01 — System overview

## Purpose
SecureBank is a simulated banking/payment API and web client used to exercise an end-to-end
AppSec program. It is intentionally vulnerable and runs locally only.

## Scope
In scope: the API (FastAPI), database (PostgreSQL), cache (Redis), the web client, the
CI/CD pipeline, and the container/IaC definitions. Out of scope: real payment processors,
production hosting, real user data.

## Actors
- **Anonymous user** — can register and log in.
- **Authenticated user** — owns accounts, makes transfers, views own transactions.
- **Admin** — manages users, views audit logs.
- **CI/CD pipeline** — builds, scans and deploys; privileged.
- **Attacker** — external, unauthenticated or an authenticated low-privilege user.

## Key use cases
Register, authenticate (JWT), view profile/accounts, transfer funds, list transactions,
manage beneficiaries, administer users, read audit logs.

See [02-data-flow-diagram.md](02-data-flow-diagram.md) for flows and boundaries.
