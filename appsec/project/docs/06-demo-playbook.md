# 06 — Demonstration playbook (attack → detection → remediation)

For every catalogued vulnerability, produce one demonstration following this template. These
are the highest-value portfolio artifacts: they show reasoning, not just tool output. Store
each as `docs/demos/<ID>-<slug>.md` with the referenced evidence under `reports/`.

## Template

```
## <ID> — <title>

1. Threat model reference   — which threat/STRIDE entry predicted this
2. Vulnerable code / config — link to the file and the *-vulnerable tag
3. Attack scenario          — attacker goal and preconditions
4. Exploitation             — exact request(s)/steps; observed result (evidence)
5. Detection                — which control found it; the scanner finding (report link)
6. Risk assessment          — CWE, CVSS, EPSS/KEV, exposure, reachability → priority
7. Remediation              — the fix; link to the *-remediated commit/tag
8. Security test            — unit/integration test asserting the control
9. Regression               — re-run DAST/SAST; finding now absent (report link)
10. Closure                 — status in the vulnerability inventory
```

## Worked example — APP-002 (IDOR, flagship slice)

```
1. Threat model: "Unauthorized access to another user's transaction" (Tampering/EoP, Critical).
2. Vulnerable code: GET /api/transactions/{id} returns the record by id with no owner check.
3. Attack: authenticated as user A, request a transaction id belonging to user B.
4. Exploitation:
     GET /api/transactions/1002   (id owned by another user)
     → 200 OK with user B's transaction  (evidence: reports/dast/app-002-before.json)
5. Detection: DAST (ZAP authenticated scan) flags access-control anomaly; SAST does NOT
   (the code is syntactically valid) — document this gap explicitly.
6. Risk: CWE-639; CVSS ~9.1; internet-facing; reachable → Critical → block deployment.
7. Remediation: enforce `transaction.owner_id == current_user.id` (object-level authorization);
   commit on tag v0.6-app002-remediated.
8. Test: test_transaction_access_denied_for_non_owner() → 403/404.
9. Regression: re-run ZAP authenticated scan → finding absent (reports/dast/app-002-after.json).
10. Closure: APP-002 status = Closed in security/vulnerability-management/findings.json.
```

This single artifact demonstrates threat modeling, the SAST/DAST division of labour,
risk-based prioritization, a real fix, test coverage, and regression verification — the
full loop on one finding.
