# RealSense Depth Detector

A Python package for object detection with depth information using Intel RealSense cameras.

## Installation

```bash
pip install .
```

## Usage

```python
from realsense_depth_detector import DepthDetector, DepthConfig
from ultralytics import YOLO

# Configure depth planes
config = DepthConfig(
    depth_planes={
        "close": (0.2, 1.0),
        "medium": (1.0, 2.0),
        "far": (2.0, 5.0)
    },
    active_plane="medium"
)

# Initialize
model = YOLO("yolov8n.pt")
detector = DepthDetector(model, config)

# Process frames
frame, detections = detector.process_frame()

# Clean up
detector.release()
```

## Requirements

- pyrealsense2
- numpy
- opencv-python
- ultralytics (for YOLO)
