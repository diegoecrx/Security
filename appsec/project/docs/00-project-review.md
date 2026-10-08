# 00 — Project review, realism &amp; improvements

## Verdict

The core idea is sound and worth building. A single realistic application with a complete
AppSec program around it is a materially stronger portfolio artifact than six isolated
tool demos, because it demonstrates *integration, prioritization and operation* — the
parts of the job that distinguish a senior/lead AppSec or DevSecOps candidate from someone
who has merely run scanners. Keep the central thesis; the changes below are refinements,
not redirections.

## Realism assessment

| Dimension | Assessment |
|---|---|
| Technical feasibility | High. Every component uses mature, free, well-documented tooling. |
| Scope | Large but naturally phased. Realistic at **8–12 weeks part-time** if sequenced by release (v0.1 → v1.0). Do not attempt in one sitting. |
| Cost | ~Zero. Entire pipeline runs on free OSS and the GitHub Actions free tier. (Avoid tools that need a paid licence for automation — see below.) |
| Maintenance | Low once stabilized; the app is deliberately small. |
| Career value | High **if** the story is "I operated an AppSec program," backed by real pipelines, reports, commits and metrics — not "I built a vulnerable app." |
| Main risk | Over-scoping early (Kubernetes, Terraform, custom dashboard) and stalling before the pipeline works end to end. Mitigation: ship a thin end-to-end slice first. |

## Improvements (apply these)

1. **Free/OSS toolchain only, for automation.** Replace Burp Suite Professional (paid,
   not CI-friendly on the free tier) with **OWASP ZAP** (automatable) plus **Nuclei** for
   templated checks. Burp *Community* is fine for manual exploration but not for the
   automated gate. Full stack in [`04-tooling.md`](04-tooling.md).

2. **Make before/after reproducible, not narrative.** Represent the "vulnerable" and
   "remediated" states as **git branches/tags per phase** (e.g. tag `v0.3-sast-vulnerable`
   and `v0.3-sast-remediated`), and generate all before/after metrics from **actual
   scanner output** committed under `reports/`. Never hand-type finding counts.

3. **Thin vertical slice first.** Before breadth, get *one* vulnerability through the
   *entire* loop: threat model entry → intentional code → SAST finding → gate → fix →
   DAST confirmation → closed in the inventory. IDOR on a transaction endpoint is the
   ideal first slice (it touches threat modeling, SAST's limits, DAST's strengths, and
   authorization — the most interesting control). Then widen.

4. **Risk-based gates, not severity-only.** The gate logic in
   [`security/security-gates/gate-policy.md`](../security/security-gates/gate-policy.md)
   combines severity (CVSS) with exploit likelihood (EPSS / CISA KEV), exposure
   (internet-facing vs internal) and reachability. This is the single most
   senior-signalling feature; prioritize it over a custom UI.

5. **Vulnerability management: normalize first, dashboard later.** Do not hand-build a web
   dashboard early. Normalize every scanner's output (SARIF where available, else JSON)
   into one findings store with a fixed schema
   ([`security/vulnerability-management/finding-schema.md`](../security/vulnerability-management/finding-schema.md)),
   and render a simple static report/metrics file from it. Optionally adopt **OWASP
   DefectDojo** (OSS) later as the aggregation/SLA layer — itself a strong resume line —
   rather than reinventing it.

6. **Secret-scanning demo needs care.** GitHub *push protection* will block pushing
   realistic-looking secrets. Use obviously-fake, non-matching placeholders for committed
   examples, and stage the "accidental commit → history persistence" demo on a dedicated,
   clearly-labelled branch (or a throwaway local repo) so it is reproducible without
   fighting the platform. Documented in [`scanners/secrets/`](../scanners/secrets/).

7. **Standards alignment adds credibility cheaply.** Map security requirements to **OWASP
   ASVS**, threats to **STRIDE/CWE**, program maturity to **OWASP SAMM**, and supply-chain
   controls to **SLSA / NIST SSDF**. This connects the hands-on work to recognised
   frameworks reviewers know.

8. **Keep Kubernetes/Terraform as v1.0 stretch.** Start on docker-compose. Add IaC
   scanning against the compose/Dockerfiles immediately (cheap), and add real Terraform/K8s
   only once the core loop is solid. Do not let infrastructure block the AppSec story.

9. **Portability is a first-class requirement** (you work across two machines). Treat
   Git + Docker + a devcontainer as the reproducibility backbone so the project is
   identical on any machine. Full design in [`03-portability.md`](03-portability.md).

## What to keep exactly as proposed

- The six-topic lifecycle framing and the phased v0.x releases.
- Threat model stored as versioned markdown in the repo.
- Per-vulnerability "attack → detection → remediation" demonstrations (the highest-value
  artifacts — see [`06-demo-playbook.md`](06-demo-playbook.md)).
- SBOM generation during build.
- A README that tells the program story, backed by evidence.

## Scope guardrails (to avoid stalling)

- **Done &gt; perfect.** A working end-to-end pipeline with 5 real vulnerabilities beats a
  half-built platform with 30 planned ones.
- **No real integrations.** Simulate payments; no live payment processors; test keys only.
- **No public deployment.** Local only; this app is deliberately exploitable.
