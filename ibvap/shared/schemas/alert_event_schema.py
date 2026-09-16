"""
CONTRACT B -> C  (Reasoning team -> Platform team)
Frozen in Phase 0. Team 3 builds and tests its entire codebase against
this exact shape, initially using shared/fixtures/mock_alert_events.json.
Matches Step 30/33's tier1/tier2 breakdown.
"""
from __future__ import annotations
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field


class EventType(str, Enum):
    ZONE_VIOLATION = "zone_violation"
    NO_TRACEABLE_ORIGIN = "no_traceable_origin"
    ROUTE_ANOMALY = "route_anomaly"
    OFF_HOURS = "off_hours"
    BEHAVIOR_ONLY = "behavior_only"


class SeverityBand(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ModelVersions(BaseModel):
    """Step 37 - stamped on every alert for provenance."""
    detection_model_version: str | None = None
    face_model_version: str | None = None
    reid_model_version: str | None = None
    scoring_config_version: str | None = None


class AlertEvent(BaseModel):
    event_id: str
    camera_id: str
    zone_id: str
    global_identity_id: str | None = Field(
        default=None, description="None if identity could not be resolved"
    )
    event_type: EventType
    tier1_flags: list[str] = Field(
        default_factory=list,
        description="Identity-tier flags, e.g. ['zone_violation', 'no_traceable_origin']",
    )
    tier2_observations: list[str] = Field(
        default_factory=list,
        description="Behavior-tier observations, e.g. ['trajectory_jagged', 'stutter_gait']",
    )
    context_multiplier: float
    risk_score: float
    severity: SeverityBand
    event_timestamp: str = Field(..., description="ISO-8601 UTC - when the underlying event occurred")
    snapshot_ref: str | None = Field(
        default=None, description="Reference/path to evidence snapshot, not the raw file itself"
    )
    model_versions: ModelVersions

    model_config = ConfigDict(json_schema_extra={
            "example": {
                "event_id": "evt-2026-09-16-004821",
                "camera_id": "BOP-07-CAM-03",
                "zone_id": "zone-north-ridge",
                "global_identity_id": "gid-88213",
                "event_type": "zone_violation",
                "tier1_flags": ["zone_violation"],
                "tier2_observations": ["trajectory_jagged"],
                "context_multiplier": 1.4,
                "risk_score": 34.2,
                "severity": "medium",
                "event_timestamp": "2026-09-16T05:12:33.204Z",
                "snapshot_ref": "edge://BOP-07-CAM-03/clips/evt-2026-09-16-004821.mp4",
                "model_versions": {
                    "detection_model_version": "yolov8-v3",
                    "face_model_version": "arcface-v2",
                    "reid_model_version": "osnet-v1",
                    "scoring_config_version": "risk-config-2026-09-01",
                },
            }
        })
