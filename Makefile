# Makefile for Protex AI Dataset Generation Pipeline

IMAGE_NAME=protex-dataset-pipeline
VIDEO=timelapse_test.mp4
OUTPUT_DIR=output

.PHONY: build run test clean

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm -v $(PWD)/$(OUTPUT_DIR):/app/$(OUTPUT_DIR) \
	    -v $(PWD)/$(VIDEO):/app/$(VIDEO) \
	    $(IMAGE_NAME) \
	    --video $(VIDEO) --output_dir $(OUTPUT_DIR)

test:
	pip install -r requirements.txt
	pytest tests/

clean:
	rm -rf $(OUTPUT_DIR)/*
