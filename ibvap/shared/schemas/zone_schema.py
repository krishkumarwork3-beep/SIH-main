"""
Zone schema (Step 25). Shared reference used by Team 2 (policy engine)
and Team 3 (dashboard). Frozen in Phase 0.
"""
from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field


class Zone(BaseModel):
    zone_id: str
    name: str
    sensitivity_level: int = Field(..., ge=1, le=5, description="1 (low) - 5 (high)")

    model_config = ConfigDict(json_schema_extra={
            "example": {"zone_id": "zone-north-ridge", "name": "North Ridge", "sensitivity_level": 4}
        })
