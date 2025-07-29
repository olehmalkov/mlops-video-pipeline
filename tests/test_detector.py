import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from detector import run_detection


def test_detection_output(tmp_path):
    dummy_images = [tmp_path / f"img_{i}.jpg" for i in range(3)]
    for img in dummy_images:
        img.write_bytes(b"\x00")
    detections = run_detection([str(p) for p in dummy_images], str(tmp_path))
    assert len(detections) == 3
    meta_path = tmp_path / "metadata.json"
    assert meta_path.exists()
    with open(meta_path) as f:
        data = json.load(f)
        assert isinstance(data, list)
        assert "image" in data[0]

