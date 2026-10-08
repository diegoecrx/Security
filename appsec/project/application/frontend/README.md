# Frontend (React + TypeScript) — optional, later phase

A thin client over the API. Optional in v0.1; useful for demonstrating client-side issues
(DOM XSS, token storage) and for a nicer demo. Keep it minimal — the API is the primary
attack surface. Add a `Dockerfile` and enable the `web` service in `docker-compose.yml`
when built.
