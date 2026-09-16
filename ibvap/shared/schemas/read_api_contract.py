"""
Contract for reasoning/read_api/admin_metrics_api.py - the second half
of Team 3's cross-team read access (identity_read_schema.py is the first).
Serves Step 41 (Policy Panel: unsurveyed adjacency edges) and Step 44
(Logs Panel: adjacency staleness + clock-drift fallback counts).
"""
from __future__ import annotations
from pydantic import BaseModel


class AdjacencyEdgeSummary(BaseModel):
    from_camera_id: str
    to_camera_id: str
    is_surveyed: bool
    query_count: int
    min_transit_seconds: int | None = None
    max_transit_seconds: int | None = None


class UnsurveyedEdgesResponse(BaseModel):
    """Step 19/41 - ranked, most-used-first."""
    edges: list[AdjacencyEdgeSummary]


class SystemMetricsResponse(BaseModel):
    """Step 19/23/44 - surfaced on the Logs Panel."""
    adjacency_edges_total: int
    adjacency_edges_surveyed: int
    adjacency_staleness_pct: float
    clock_drift_fallback_event_count: int
