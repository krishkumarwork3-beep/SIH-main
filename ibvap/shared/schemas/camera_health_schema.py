"""
Camera Health contract (Step 6, extended by Step 36).
Written by perception/publisher/health_event_publisher.py.
Read by reasoning/health_consumer/ (Steps 29/30) and by the edge
write-ahead queue (Step 36), which appends queue_depth when running
on an edge device (Step 47) - this is why queue_depth is optional
and lives in this shared contract rather than a platform-only schema.
"""
from __future__ import annotations
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field


class HealthStatus(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    OFFLINE = "offline"


class CameraHeartbeat(BaseModel):
    camera_id: str
    status: HealthStatus
    expected_fps: float
    actual_fps: float
    frame_is_blank: bool = Field(
        default=False, description="True if frame is statistically uniform (obstructed/covered lens)"
    )
    timestamp: str = Field(..., description="ISO-8601 UTC")

    # Step 36 addition - only populated on edge-deployed devices
    edge_queue_depth_tier1: int | None = Field(
        default=None, description="Count of un-synced Tier-1 (metadata) entries in the local write-ahead queue"
    )
    edge_queue_depth_tier2: int | None = Field(
        default=None, description="Count of un-synced Tier-2 (evidence clip) entries"
    )

    model_config = ConfigDict(json_schema_extra={
            "example": {
                "camera_id": "BOP-07-CAM-03",
                "status": "healthy",
                "expected_fps": 15.0,
                "actual_fps": 14.7,
                "frame_is_blank": False,
                "timestamp": "2026-09-16T05:12:33.204Z",
                "edge_queue_depth_tier1": 0,
                "edge_queue_depth_tier2": 0,
            }
        })
