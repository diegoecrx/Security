# Security gate policy (risk-based)

The gate decides whether a change may progress. Severity alone is a weak signal; this policy
combines **severity (CVSS)**, **exploit likelihood (EPSS / CISA KEV)**, **exposure**
(internet-facing vs internal) and **reachability**. This risk-based model is the point of
the project — it demonstrates prioritization, not just scanning.

## Baseline (severity) policy

| Severity | Pre-production | Production |
|---|---|---|
| Critical | Block | Block |
| High | Warn | Block |
| Medium | Warn | Warn |
| Low | Informational | Informational |

## Risk-based override (preferred)

Compute an effective risk from the signals, then gate on it:

```
BLOCK if:
    CVSS >= 9.0
    AND (internet_facing OR reachable)
    AND (EPSS >= 0.5 OR in_CISA_KEV)

REVIEW (manual decision) if:
    CVSS >= 9.0
    AND NOT internet_facing
    AND NOT reachable
    AND EPSS < 0.1

WARN if:
    High severity, not reachable, low EPSS

PASS if:
    below thresholds, or an approved, unexpired exception exists
```

Rationale examples:
- CVSS 9, internet-facing, known exploited → **block** (real, imminent risk).
- CVSS 9, internal-only, not reachable, EPSS < 0.1 → **review** (theoretical; do not auto-block the pipeline).

## Exceptions

A finding may pass with a documented exception: owner, justification, compensating control,
and an **expiry date**. Exceptions are recorded in the inventory and reviewed each release.
Expired exceptions revert to the policy above.

## Inputs

The gate reads the normalized findings
([`../vulnerability-management/finding-schema.md`](../vulnerability-management/finding-schema.md))
and enriches each with EPSS (FIRST), KEV (CISA), the asset's exposure (from the asset
register), and reachability (from SCA/SAST where available).

## Implementation

Start as a script in the pipeline that consumes the normalized `findings.json`, applies the
rules, and exits non-zero to fail the gate. Keep the thresholds in one config file so the
policy is auditable and versioned. Reference: [`../../../CICD-Security.html`](../../../CICD-Security.html).
