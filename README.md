# australia-cdr-dashboard

## Summary
The idea behind this is to have a universal display of all Australia's Financial Instruments that uses the Consumer Data Right API to be shown on a dashboard. It would help users determine which one might be fitting to their financial goal and it would be updated accordingly 

## Phase 1 — Public product ingestion (the pipeline spine)
Seed from the real CDR Register (`api.cdr.gov.au`) to get the ~117 live bank base URIs, then hit each bank's public, unauthenticated `GET /banking/products`. Build the processing machinery here while nothing hard is in front of it: fetch → land raw JSONB → normalize → idempotent upsert → handle per-holder `x-v` version negotiation and partial failures.

## Phase 2 — Orchestration, transformation, quality
Incremental ingestion driven by `updated-since`; dbt models (staging → intermediate → marts) with tests; capture rate changes over time as history rather than overwriting.

## Phase 3 — Authenticated recipient flow against the mock (the scarce skill)
Stand up the ACCC mock holder / sandbox, then put the hard auth layer *in front of the same Phase 1 pipeline spine*: dynamic client registration, then the FAPI / CDR Security Profile handshake — OAuth2 + OIDC, mTLS, PAR, PKCE — plus the consent flow. Once authorised, pull the endpoints you couldn't touch before (`/banking/accounts`, `/balances`, `/transactions`) for the consented mock customer.


## Phase 4 — Transaction enrichment & categorization
On that mock transaction data, build the insight layer: classify transactions (groceries, salary, utilities), detect recurring payments, derive cashflow.
