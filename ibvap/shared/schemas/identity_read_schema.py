"""
Read-only view into Team 2's identity data, for Team 3's dashboard.
Fixes gap: Team 3 needs this directly (Steps 40, 44), not just as
part of an alert event. Served by reasoning/read_api/identity_read_api.py.
"""
from __future__ import annotations
from pydantic import BaseModel, Field


class AuthorizationView(BaseModel):
    status: str = Field(..., description="'authorized' or 'unauthorized'")
    person_id: str | None = None
    level: int | None = None
    matched_embedding_version: str | None = None


class MovementLogEntry(BaseModel):
    camera_id: str
    zone_id: str
    timestamp: str


class GlobalIdentityView(BaseModel):
    global_identity_id: str
    authorization: AuthorizationView
    movement_history: list[MovementLogEntry]
    group_id: str | None = Field(
        default=None, description="Step 17 discrete group entity, if currently grouped"
    )
