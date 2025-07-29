import sys
import os
import numpy as np
import cv2
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from extractor import extract_frames


def create_dummy_video(video_path, frame_count=60, width=100, height=100):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_path, fourcc, 1, (width, height))
    for i in range(frame_count):
        frame = np.random.randint(0, 255, (height, width, 3), np.uint8)
        cv2.putText(frame, str(i), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        video.write(frame)
    video.release()


def test_frame_extraction(tmp_path):
    video_path = str(tmp_path / "test.mp4")
    create_dummy_video(video_path, frame_count=60)
    output_dir = tmp_path / "frames"
    frames = extract_frames(video_path, str(output_dir), step=30)
    assert len(frames) == 2
    for frame in frames:
        assert os.path.exists(frame)


def create_duplicate_video(video_path, frame_count=10):
    # Create a video with all frames identical (duplicates)
    height, width = 64, 64
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_path, fourcc, 5.0, (width, height))
    frame = np.full((height, width, 3), 128, dtype=np.uint8)  # gray frame
    for _ in range(frame_count):
        out.write(frame)
    out.release()


def test_frame_deduplication(tmp_path):
    # Create a temporary video with duplicate frames
    video_path = tmp_path / "dup_test.mp4"
    create_duplicate_video(str(video_path), frame_count=10)
    output_dir = tmp_path / "frames"
    frames = extract_frames(str(video_path), str(output_dir), step=1, hash_threshold=1)
    # Only one unique frame should be saved
    assert len(frames) == 1, f"Expected 1 unique frame, got {len(frames)}"
