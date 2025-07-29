from extractor import extract_frames
from detector import run_detection
from report_generator import generate_report
import argparse
import os
import time
from collections import Counter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video', required=True)
    parser.add_argument('--output_dir', required=True)
    parser.add_argument('--config', default="default.yaml")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    time_start = time.perf_counter()

    # Step 1: Extract frames from input video
    t0 = time.perf_counter()
    frames = extract_frames(args.video, args.output_dir)
    t1 = time.perf_counter()

    # Step 2: Run detection on extracted frames
    detections = run_detection(frames, args.output_dir)
    t2 = time.perf_counter()

    # Collect stats for the report
    total_frames = len(frames)
    total_images = len(detections)
    detections_per_frame = [len(d) for d in detections]

    # Count class distribution from all detections
    class_counter = Counter()
    for det_list in detections:
        for det in det_list:
            class_name = det.get("class", "unknown")
            class_counter[class_name] += 1

    time_end = time.perf_counter()
    time_metrics = {
        "Frame extraction": t1 - t0,
        "Detection": t2 - t1,
        "Total": time_end - time_start
    }

    # Step 3: Generate Markdown + HTML report
    generate_report(
        output_dir=args.output_dir,
        total_frames=total_frames,
        total_images=total_images,
        detections_per_frame=detections_per_frame,
        time_metrics=time_metrics,
        class_distribution=dict(class_counter)
    )

if __name__ == "__main__":
    main()
