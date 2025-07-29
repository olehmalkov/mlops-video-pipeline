import os
import json

def test_dummy():
    assert True

def test_output_files_exist_and_valid():
    # Check if output directory exists
    output_dir = "output"
    assert os.path.isdir(output_dir), "Output directory does not exist."

    # Check if at least one image exists in output directory
    images = [f for f in os.listdir(output_dir) if f.endswith('.jpg')]
    assert len(images) > 0, "No output images found."

    # Check if metadata.json exists
    metadata_path = os.path.join(output_dir, "metadata.json")
    assert os.path.isfile(metadata_path), "metadata.json not found."

    # Check if metadata.json is valid JSON and has expected structure
    with open(metadata_path) as f:
        data = json.load(f)
        assert isinstance(data, list), "metadata.json is not a list."
        assert all("image" in d and "detections" in d for d in data), "Invalid detection format in metadata.json."
