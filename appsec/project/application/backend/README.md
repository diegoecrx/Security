# Backend (FastAPI)

Starter skeleton. Build the endpoints from [`../../docs/02-architecture.md`](../../docs/02-architecture.md)
and introduce intentional vulnerabilities per [`../../docs/05-vulnerability-catalog.md`](../../docs/05-vulnerability-catalog.md).

- `app/main.py` — minimal FastAPI app (`/health`, `/docs`).
- `requirements.txt` — pinned dependencies.
- `Dockerfile` — container image used by `docker-compose.yml`.

Run: `make up` (from the project root), then http://localhost:8000/docs.

Keep each vulnerability small and isolated; fix it in a clean, reviewable diff on a
`*-remediated` tag so before/after is reproducible.
