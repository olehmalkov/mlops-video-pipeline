import os
import json
import random

CLASSES = ['person', 'car', 'tree']

def run_detection(image_paths, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    detections = []
    for img_path in image_paths:
        det = {
            'image': os.path.basename(img_path),
            'detections': [{
                'class': random.choice(CLASSES),
                'confidence': round(random.uniform(0.5, 1.0), 2)
            } for _ in range(random.randint(1, 3))]
        }
        detections.append(det)
    with open(os.path.join(output_dir, 'metadata.json'), 'w') as f:
        json.dump(detections, f, indent=2)
    return detections
