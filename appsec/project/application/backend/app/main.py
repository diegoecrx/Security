"""SecureBank API — starter skeleton (v0.1).

This is a minimal, runnable base. Build out the endpoints from
docs/02-architecture.md and introduce the intentional vulnerabilities from
docs/05-vulnerability-catalog.md on dedicated branches/tags.

Run locally: `make up` then open http://localhost:8000/docs
"""
from fastapi import FastAPI

app = FastAPI(title="SecureBank API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


# TODO (v0.1):
#   /api/auth/register, /api/auth/login
#   /api/users/me, /api/accounts, /api/accounts/{id}
#   /api/transfers, /api/transactions, /api/transactions/{id}
#   /api/beneficiaries, /api/admin/users, /api/admin/audit
#
# Introduce vulnerabilities deliberately and catalogue them. Example (APP-001, SQLi) —
# to be added on a *-vulnerable tag, then fixed on a *-remediated tag.
