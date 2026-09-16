# IBVAP - Intelligent Border Video Analytics Platform

AI-based video analytics platform turning existing CCTV infrastructure
into an intelligent surveillance network for SSB border outposts.

## Repo layout

- `shared/` - Phase 0 contracts (schemas, fixtures, auth, config). Jointly owned.
- `perception/` - Team 1: detection, tracking, face/ANPR, posture, night/thermal (Steps 5-17)
- `reasoning/` - Team 2: Re-ID, adjacency graph, authorization, policy, risk scoring (Steps 18-32)
- `platform/` - Team 3: storage, blockchain, security, dashboard (Steps 33-44)
- `edge/` - Deployment bundle for bandwidth-constrained BOPs (Step 47) - packages perception + platform's write-ahead queue to run co-resident on a Jetson.
- `docs/` - architecture and data-flow reference docs.
- `integration/` - Phase 4 (Steps 45-51), populated once Steps 1-44 are functionally complete.

## Getting started (Phase 0)

1. `python -m venv venv && venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
2. `pip install -r requirements.txt`
3. `docker compose up -d` (starts local Postgres)
4. Copy `.env.example` to `.env` and fill in local values
5. Run `pytest shared/` to confirm the schemas import cleanly

See `docs/architecture_diagram.md` for the full system overview and
team boundary rules before writing any code that crosses `shared/`.
