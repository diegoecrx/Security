# 02 — Data flow diagram

External entities: **User**, **Admin**. Process: **API**. Data stores: **PostgreSQL**, **Redis**.

```
 [User] ──creds──▶ (API /auth) ──query──▶ [PostgreSQL]
 [User] ◀──JWT──── (API /auth)
 [User] ──JWT+op──▶ (API /transfers,/transactions) ──r/w──▶ [PostgreSQL]
                        │
                        └──rate/session──▶ [Redis]
 [Admin] ──JWT──▶ (API /admin) ──r──▶ [PostgreSQL]
```

## Trust boundaries (threats concentrate here)
1. **Internet → API** — all inbound client traffic (TB1).
2. **API → PostgreSQL** — query construction / data access (TB2).
3. **API → Redis** — session / rate-limit state (TB3).
4. **User → Admin** — privilege boundary within the API (TB4).
5. **CI/CD → build/deploy** — supply-chain boundary (TB5).

Elements and boundaries are the inputs to STRIDE in [05-threats.md](05-threats.md).
