import os
import json
from collections import Counter
from time import time

def generate_report(output_dir, total_frames, total_images, detections_per_frame, time_metrics, class_distribution):
    report = [
        "# Dataset Report",
        f"- Frames extracted: {total_frames}",
        f"- Detections: {sum(detections_per_frame)}",
        "- Class distribution:"
    ] + [f"  - {cls}: {cnt}" for cls, cnt in class_distribution.items()]

    with open(os.path.join(output_dir, 'report.md'), 'w') as f:
        f.write("\n".join(report))
