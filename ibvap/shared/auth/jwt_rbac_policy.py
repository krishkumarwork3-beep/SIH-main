"""
Shared JWT/RBAC scaffolding (Step 35). This wraps every API surface
across all 3 teams - perception ingestion endpoints, reasoning's
reasoning/consumer and read_api, and platform's dashboard backend.
Agreed jointly in Phase 0, not decided unilaterally by Team 3.

This file only defines the shared contract (roles, token claim shape,
and the dependency every team's FastAPI routes import). The actual
signing/verification implementation is filled in by Team 3 as part
of Step 35 - this stays here because every team's endpoints import
`require_role` below.
"""
from __future__ import annotations
from enum import Enum
from pydantic import BaseModel


class Role(str, Enum):
    OPERATOR = "operator"
    ADMIN = "admin"
    SURVEY_OFFICER = "survey_officer"   # Step 19 adjacency-graph owner
    SYSTEM = "system"                    # service-to-service calls (e.g. perception -> reasoning)


class TokenClaims(BaseModel):
    sub: str            # person_id or service_id
    role: Role
    exp: int             # unix timestamp
    iat: int


# TODO (Team 3, Step 35): implement real verification here.
# Every team's route handlers depend on this function's signature staying
# stable - do not change the signature without cross-team agreement.
def require_role(*allowed_roles: Role):
    """
    FastAPI dependency factory. Usage in any team's routes:

        @app.get("/some-endpoint")
        def handler(claims: TokenClaims = Depends(require_role(Role.ADMIN))):
            ...
    """
    def _dependency() -> TokenClaims:
        raise NotImplementedError(
            "Team 3 (Step 35): implement JWT verification against a real "
            "Authorization header here, then return TokenClaims."
        )
    return _dependency
