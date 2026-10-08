# Security requirements

Testable requirements derived from the threat model and mapped to **OWASP ASVS** so the work
ties to a recognised standard. Each requirement has a verifying control (SAST / DAST / test)
and is tracked to closure.

| Req | Requirement | ASVS area | Verified by | Threat |
|---|---|---|---|---|
| SR-01 | Authentication enforces rate limiting and lockout | V2 Authentication | DAST, test | T1 |
| SR-02 | All DB access is parameterized | V5 Validation/Injection | SAST, DAST | T2 |
| SR-03 | JWT signature verified; algorithm pinned | V3 Session / V2 | SAST, test | T3 |
| SR-04 | Object access enforces ownership (object-level authz) | V4 Access Control | DAST, test | T4 |
| SR-05 | Admin functions enforce RBAC | V4 Access Control | DAST, test | T5 |
| SR-06 | Output is context-encoded; CSP set | V5 Validation/Encoding | DAST, SAST | T6 |
| SR-07 | Outbound requests restricted to an allow-list | V5 / SSRF | SAST, DAST | T7 |
| SR-08 | No secrets in source; secrets from env/vault | V6 Cryptography / V14 | Secret scanning | T8 |
| SR-09 | Dependencies scanned; criticals remediated; SBOM produced | V14 Config | SCA | T9 |
| SR-10 | Passwords hashed; no sensitive data in errors | V2 / V7 | SAST, DAST | T11 |
| SR-11 | Security headers and secure cookie flags set | V14 Config | DAST | T12 |
| SR-12 | Security events are audit-logged | V7 Logging | test | T13 |

Reference: OWASP ASVS. Program maturity is tracked against OWASP SAMM.
