# Protex AI Dataset Generation Pipeline

## Overview
This project provides a reproducible, containerized pipeline for generating computer vision datasets from timelapse video. The pipeline extracts frames, performs (mock) object detection, and generates a summary report. It is designed for scalability, automation, and observability, following MLOps best practices.

---

## Features
- **Containerized**: Easily deployable with Docker
- **Automated**: Makefile for build, run, test, and clean
- **Unit-tested**: Pytest-based tests for all key functions
- **Frame deduplication**: Uses perceptual hashing to skip duplicate frames
- **Input validation**: Checks video file existence and validity before processing
- **Reporting**: Generates Markdown report with dataset statistics
- **Extensible**: Modular code for easy improvements

---

## Quick Start

### 1. Build Docker Image
```bash
docker build -t protex-dataset-pipeline .
```

### 2. Run the Pipeline in Docker
```bash
docker run --rm \
    -v $(pwd)/output:/app/output \
    -v $(pwd)/timelapse_test.mp4:/app/timelapse_test.mp4 \
    protex-dataset-pipeline \
    --video timelapse_test.mp4 --output_dir output
```
- `--video` — path to input video (must be available in the container)
- `--output_dir` — directory for results
- `--config` — (optional) model config path

### 3. Run Locally (for development)
```bash
python main.py --video timelapse_test.mp4 --output_dir output
```

### 4. Run Tests
```bash
pip install -r requirements.txt
pytest tests/
```
Or using Makefile:
```bash
make test
```

### 5. Clean Output
```bash
make clean
```

---

## Project Structure
- `main.py` — main pipeline script (argument parsing, orchestration)
- `extractor.py` — frame extraction from video (with deduplication and validation)
- `detector.py` — mock object detection
- `reporter.py` — report generation
- `output/` — generated images, metadata, and report
- `tests/` — unit tests for all modules (including deduplication)
- `Makefile` — automation for build/run/test/clean
- `Dockerfile` — containerization

---

## Output
- Extracted frames: `output/frame_XXXX.jpg` (duplicates skipped)
- Detection metadata: `output/metadata.json`
- Markdown report: `output/report.md`

---

## Report Example
```
# Dataset Report
- Frames extracted: 408
- Detections: 846
- Class distribution:
  - car: 276
  - tree: 302
  - person: 268
```

---

## Improvements for Production
- Add real object detection (YOLO, etc.)
- Frame deduplication (perceptual hashing, already implemented)
- Input validation (already implemented)
- Logging and monitoring (W&B, Prometheus, CSV)
- Cloud deployment (IaC, autoscaling)

---
