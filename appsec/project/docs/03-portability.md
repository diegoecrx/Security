# 03 — Portability: working across two machines

Requirement: the project is developed on this machine and on a second personal machine in
another location. Changes must be easy to make and to replicate between them. The design
below makes the repository the single source of truth and the runtime reproducible on any
machine, so "replicate" is just `git pull` plus one command.

## Principle

Everything is code or configuration committed to Git. No machine-specific state. The only
per-machine item is the local `.env` file (secrets/local values), which is never committed
and is recreated from `.env.example`.

## The backbone

```
GitHub (remote)  ──clone/pull/push──  Machine A  (this computer)
      │
      └──────────clone/pull/push──────  Machine B  (personal computer)
```

1. **Git + a GitHub remote** — the authoritative copy. Work flows A → GitHub → B and back.
   Use feature branches and PRs (this also exercises the PR-based security gates).
2. **Docker Compose** — the runtime (API, PostgreSQL, Redis) comes up identically on any
   machine with `make up`. No local language/database installs required to *run* it.
3. **Dev container** (`.devcontainer/devcontainer.json`) — an identical development
   environment (Python, Node, tool versions) on both machines, used either with local
   Docker or with **GitHub Codespaces** (zero local setup — the strongest cross-machine
   option).
4. **Pinned versions** — Python, Node and scanner versions are pinned so results match
   across machines.
5. **Makefile** — one command vocabulary (`make up`, `make scan`, `make sast`, `make dast`)
   that works the same everywhere.

## Daily workflow

```bash
# Start of a session on either machine
git pull

# ... make changes ...
make up            # run the app locally
make scan          # run local security scans before pushing

git add -A && git commit -m "..." && git push

# On the other machine, to replicate:
git pull           # identical code + config
make up            # identical runtime
```

## Three ways to run — pick per machine

| Option | Local setup needed | Notes |
|---|---|---|
| **A. GitHub Codespaces** (devcontainer in the cloud) | None (browser or VS Code) | Best for a second/low-spec machine; identical env everywhere; free tier available. |
| **B. Local Docker + devcontainer** | Docker Desktop (or Rancher Desktop / Podman) + VS Code | Fully local; fastest iteration. |
| **C. Native tools + CI for containers** | Python 3.12, Node 20, Git | Run the app natively; let GitHub Actions run the container/scan steps. Avoids a local container engine entirely. |

Mix freely: e.g. Option B on the main machine, Option A on the personal machine.

## Windows note (container engine)

Docker Desktop on Windows uses the WSL2 backend by default. If you prefer to avoid WSL:

- Use **GitHub Codespaces** (Option A) — containers run in the cloud, nothing local.
- Or **Rancher Desktop** / **Podman Desktop** (can run without the Docker/WSL stack in some
  configurations), or Docker Desktop with the Hyper-V backend where available.
- Or **Option C** — develop with native Windows Python/Node and run all container and scan
  steps in GitHub Actions. The app (FastAPI + a local PostgreSQL/Redis, or SQLite for dev)
  runs natively; the pipeline proves the containerized flow.

Choose one engine per machine; the repo does not care which.

## What is committed vs. local

| Committed (replicates automatically) | Local only (recreate per machine) |
|---|---|
| Source, Dockerfiles, `docker-compose.yml` | `.env` (from `.env.example`) |
| `.devcontainer/`, `Makefile`, pinned versions | Docker images / volumes (rebuilt) |
| CI workflows, scanner configs | IDE personal settings |
| Threat model, docs, reports | — |

## Reproducibility checklist

- [ ] Remote set (`git remote -v`) and both machines clone from it.
- [ ] `.env` present locally on each machine; **never** committed.
- [ ] `make up` brings the stack up cleanly from a fresh clone.
- [ ] Tool versions pinned (compose image tags, `requirements.txt`, action versions).
- [ ] No absolute machine paths in code or config.
- [ ] `.gitignore` excludes `.env`, build artifacts, local volumes, scanner caches.
