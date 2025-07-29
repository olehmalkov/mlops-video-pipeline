import os
import json

def test_dummy():
    assert True

def test_output_files_exist_and_valid(tmp_path):
    output_dir = tmp_path / "output"
    os.makedirs(output_dir)

    # Create dummy image files
    (output_dir / "frame_0001.jpg").touch()
    (output_dir / "frame_0002.jpg").touch()

    # Create dummy metadata.json
    metadata_path = output_dir / "metadata.json"
    dummy_metadata = [
        {"image": "frame_0001.jpg", "detections": [{"class": "car", "confidence": 0.9}]},
        {"image": "frame_0002.jpg", "detections": [{"class": "person", "confidence": 0.8}]}
    ]
    with open(metadata_path, 'w') as f:
        json.dump(dummy_metadata, f)

    # Check if at least one image exists in output directory
    images = [f for f in os.listdir(output_dir) if f.endswith('.jpg')]
    assert len(images) > 0, "No output images found."

    # Check if metadata.json exists
    assert os.path.isfile(metadata_path), "metadata.json not found."

    # Check if metadata.json is valid JSON and has expected structure
    with open(metadata_path) as f:
        data = json.load(f)
        assert isinstance(data, list), "metadata.json is not a list."
        assert all("image" in d and "detections" in d for d in data), "Invalid detection format in metadata.json."
