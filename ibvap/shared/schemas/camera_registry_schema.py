"""
Camera Registry schema (Step 4).
Owned jointly - frozen in Phase 0. All three teams read this.
Do not change field names/types after Phase 0 without team agreement.
"""
from __future__ import annotations
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field


class CameraType(str, Enum):
    VISIBLE = "visible"
    THERMAL = "thermal"


class Camera(BaseModel):
    camera_id: str = Field(..., description="Unique camera identifier, e.g. 'BOP-07-CAM-03'")
    location_name: str
    gps_lat: float
    gps_lon: float
    rtsp_url: str
    zone_coverage: list[str] = Field(
        default_factory=list,
        description="Zone IDs this camera covers (many-to-many, see zone_schema.py)",
    )
    direction_deg: float | None = Field(
        default=None, description="Compass orientation of the camera, 0-360"
    )
    camera_type: CameraType = CameraType.VISIBLE

    model_config = ConfigDict(json_schema_extra={
            "example": {
                "camera_id": "BOP-07-CAM-03",
                "location_name": "North Ridge Checkpoint",
                "gps_lat": 32.1234,
                "gps_lon": 77.5678,
                "rtsp_url": "rtsp://10.0.7.3:554/stream1",
                "zone_coverage": ["zone-north-ridge"],
                "direction_deg": 45.0,
                "camera_type": "visible",
            }
        })
