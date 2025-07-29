import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from reporter import generate_report

def test_report_creation(tmp_path):
    total_frames = 10
    total_images = 5
    detections_per_frame = [1, 2, 1, 0, 1]
    time_metrics = {"Frame extraction": 1.2, "Detection": 3.4, "Total": 4.6}
    class_distribution = {"car": 3, "person": 2}

    generate_report(
        output_dir=str(tmp_path),
        total_frames=total_frames,
        total_images=total_images,
        detections_per_frame=detections_per_frame,
        time_metrics=time_metrics,
        class_distribution=class_distribution,
    )

    report_path = tmp_path / "report.md"
    assert report_path.exists()
    content = report_path.read_text()
    assert "# Dataset Report" in content
    assert f"- Frames extracted: {total_frames}" in content
    assert f"- Detections: {sum(detections_per_frame)}" in content
    assert "car: 3" in content
    assert "person: 2" in content
