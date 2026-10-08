# 03 — Assets

| Asset | Sensitivity | Why it matters |
|---|---|---|
| User credentials | Critical | Account takeover |
| JWT signing secret | Critical | Forge any user/admin token |
| Account & transaction data | Critical | Financial integrity &amp; confidentiality |
| PII (profile) | High | Privacy / regulatory |
| Database | Critical | Aggregated store of all of the above |
| Admin functionality | Critical | Full control of the system |
| API credentials (3rd-party, fake) | High | Lateral movement |
| Infrastructure credentials | Critical | Environment compromise |
| CI/CD secrets &amp; signing keys | Critical | Supply-chain compromise (one-to-many) |

Assets drive the prioritization of threats and the risk ratings in
[05-threats.md](05-threats.md).
