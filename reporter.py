import os
import json
from collections import Counter
from time import time

def generate_report(images, detections, output_dir):
    class_counts = Counter()
    for det in detections:
        for d in det['detections']:
            class_counts[d['class']] += 1

    report = [
        "# Dataset Report",
        f"- Frames extracted: {len(images)}",
        f"- Detections: {sum(len(d['detections']) for d in detections)}",
        "- Class distribution:"
    ] + [f"  - {cls}: {cnt}" for cls, cnt in class_counts.items()]

    with open(os.path.join(output_dir, 'report.md'), 'w') as f:
        f.write("\n".join(report))
