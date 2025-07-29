import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from reporter import generate_report

def test_report_creation(tmp_path):
    frames = [f"frame_{i}.jpg" for i in range(5)]
    detections = [
        {"image": f"frame_{i}.jpg", "detections": [{"class": "car", "confidence": 0.9}]}
        for i in range(5)
    ]
    generate_report(frames, detections, str(tmp_path))
    report_path = tmp_path / "report.md"
    assert report_path.exists()
    content = report_path.read_text()
    assert "Dataset Report" in content
