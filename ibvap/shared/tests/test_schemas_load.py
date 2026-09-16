"""
Step 1 smoke test - confirms the environment is set up correctly and
every Phase 0 contract loads and validates against its own fixture.
Run with: pytest shared/tests/test_schemas_load.py -v
"""
import json
from pathlib import Path

from shared.schemas.detection_track_schema import TrackEvent
from shared.schemas.alert_event_schema import AlertEvent
from shared.schemas.camera_health_schema import CameraHeartbeat
from shared.schemas.camera_registry_schema import Camera
from shared.schemas.zone_schema import Zone

FIXTURES_DIR = Path(__file__).resolve().parents[1] / "fixtures"


def test_detection_fixture_matches_schema():
    data = json.loads((FIXTURES_DIR / "mock_detection_events.json").read_text())
    events = [TrackEvent(**item) for item in data]
    assert len(events) == 3
    assert events[0].camera_id == "BOP-07-CAM-03"


def test_alert_fixture_matches_schema():
    data = json.loads((FIXTURES_DIR / "mock_alert_events.json").read_text())
    alerts = [AlertEvent(**item) for item in data]
    assert len(alerts) == 2
    assert alerts[1].severity == "high"


def test_health_fixture_matches_schema():
    data = json.loads((FIXTURES_DIR / "mock_camera_health.json").read_text())
    heartbeats = [CameraHeartbeat(**item) for item in data]
    assert len(heartbeats) == 2
    assert heartbeats[1].status == "degraded"


def test_camera_registry_schema_example():
    example = Camera.model_config["json_schema_extra"]["example"]
    cam = Camera(**example)
    assert cam.camera_id == "BOP-07-CAM-03"


def test_zone_schema_example():
    example = Zone.model_config["json_schema_extra"]["example"]
    zone = Zone(**example)
    assert zone.sensitivity_level == 4
