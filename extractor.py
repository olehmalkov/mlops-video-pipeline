import cv2
import os
from PIL import Image
import imagehash


def extract_frames(video_path, output_dir, step=10, hash_threshold=5):
    """
    Extract unique frames from video using perceptual hashing for deduplication.
    Args:
        video_path (str): Path to input video.
        output_dir (str): Directory to save frames.
        step (int): Save every N-th frame.
        hash_threshold (int): Hamming distance threshold for considering frames as duplicates.
    Returns:
        list: List of saved frame file paths.
    """
    # Input validation: check if file exists
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Cannot open video file: {video_path}")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if total_frames == 0:
        raise ValueError(f"Video file contains no frames: {video_path}")

    os.makedirs(output_dir, exist_ok=True)
    frame_idx = 0
    saved = []
    prev_hash = None
    duplicate_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_idx % step == 0:
            # Convert frame to PIL Image for hashing
            pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            curr_hash = imagehash.phash(pil_img)
            # Deduplication: compare with previous hash
            if prev_hash is None or abs(curr_hash - prev_hash) > hash_threshold:
                filename = os.path.join(output_dir, f"frame_{frame_idx:04d}.jpg")
                cv2.imwrite(filename, frame)
                saved.append(filename)
                prev_hash = curr_hash
            else:
                duplicate_count += 1
        frame_idx += 1

    cap.release()
    print(f"[INFO] Total frames processed: {frame_idx}")
    print(f"[INFO] Unique frames saved: {len(saved)}")
    print(f"[INFO] Duplicate frames skipped: {duplicate_count}")
    return saved
