"""
CONTRACT A -> B  (Perception team -> Reasoning team)
Frozen in Phase 0. Do not change without agreement from both teams -
Team 2 builds and tests its entire codebase against this exact shape,
initially using shared/fixtures/mock_detection_events.json.
"""
from __future__ import annotations
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field


class DetectionClass(str, Enum):
    PERSON = "person"
    CAR = "car"
    TRUCK = "truck"
    MOTORCYCLE = "motorcycle"
    BICYCLE = "bicycle"


class BoundingBox(BaseModel):
    x1: float
    y1: float
    x2: float
    y2: float


class PostureSignals(BaseModel):
    """Step 12 output - neutral observations only, no suspicion label."""
    crawling: bool = False
    crouching_sustained: bool = False
    sudden_level_change: bool = False
    compressed_silhouette: bool = False
    arm_tucked: bool = False
    sustained_upward_gaze: bool = False
    jittery_head: bool = False


class FaceMatchResult(BaseModel):
    """Step 10 output. None if no face detected/matched in this frame."""
    face_bbox: BoundingBox | None = None
    matched_person_id: str | None = Field(
        default=None, description="Set if matched against Step 26 personnel DB"
    )
    matched_watchlist_id: str | None = Field(
        default=None, description="Set if matched against threat watchlist"
    )
    match_confidence: float | None = None
    embedding_version: str | None = None


class AnprResult(BaseModel):
    """Step 11 output. None if no plate read in this frame."""
    plate_text: str | None = None
    plate_confidence: float | None = None


class TrackEvent(BaseModel):
    """
    One tracked object, one frame. This is the unit Team 1 publishes
    and Team 2 consumes (shared/schemas -> perception/publisher ->
    reasoning/consumer).
    """
    camera_id: str
    local_track_id: str = Field(..., description="ByteTrack ID, valid only within this camera")
    frame_timestamp: str = Field(..., description="ISO-8601 UTC timestamp")
    detection_class: DetectionClass
    bbox: BoundingBox
    confidence: float

    # Optional per-frame enrichments (present only when computed this frame)
    reid_embedding: list[float] | None = Field(
        default=None, description="Step 18 OSNet appearance embedding, present periodically not every frame"
    )
    posture_signals: PostureSignals | None = None
    face_match: FaceMatchResult | None = None
    anpr_result: AnprResult | None = None

    model_config = ConfigDict(json_schema_extra={
            "example": {
                "camera_id": "BOP-07-CAM-03",
                "local_track_id": "trk-118",
                "frame_timestamp": "2026-09-16T05:12:33.204Z",
                "detection_class": "person",
                "bbox": {"x1": 210.5, "y1": 88.0, "x2": 265.0, "y2": 310.2},
                "confidence": 0.94,
                "reid_embedding": None,
                "posture_signals": {
                    "crawling": False,
                    "crouching_sustained": False,
                    "sudden_level_change": False,
                    "compressed_silhouette": False,
                    "arm_tucked": False,
                    "sustained_upward_gaze": False,
                    "jittery_head": False,
                },
                "face_match": None,
                "anpr_result": None,
            }
        })
