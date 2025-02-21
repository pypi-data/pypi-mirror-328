import pyrealsense2 as rs
import numpy as np
import cv2
from typing import Tuple, Optional
from .config import DepthConfig

class DepthDetector:
    def __init__(self, model, config: DepthConfig):
        """
        Initialize DepthDetector with YOLO model and configuration
        
        Args:
            model: YOLO model instance
            config: DepthConfig instance with detection parameters
        """
        self.model = model
        self.config = config
        self.pipeline = None
        self._initialize_realsense()

    def _initialize_realsense(self):
        """Configure and start RealSense pipeline"""
        self.pipeline = rs.pipeline()
        rs_config = rs.config()
        
        # Enable streams
        w, h = self.config.depth_resolution
        rs_config.enable_stream(rs.stream.depth, w, h, rs.format.z16, self.config.fps)
        
        w, h = self.config.color_resolution
        rs_config.enable_stream(rs.stream.color, w, h, rs.format.bgr8, self.config.fps)
        
        self.pipeline.start(rs_config)

    def get_aligned_frames(self):
        """Get aligned depth and color frames"""
        frames = self.pipeline.wait_for_frames()
        align = rs.align(rs.stream.color)
        aligned_frames = align.process(frames)
        
        return (aligned_frames.get_depth_frame(),
                aligned_frames.get_color_frame())

    def create_depth_mask(self, depth_frame, min_dist, max_dist):
        """Create mask for specific depth range"""
        depth_image = np.asanyarray(depth_frame.get_data())
        mask = np.logical_and(depth_image > min_dist * 1000,
                            depth_image < max_dist * 1000)
        return mask.astype(np.uint8)

    def process_frame(self) -> Tuple[Optional[np.ndarray], list]:
        """
        Process a single frame and return detections
        
        Returns:
            Tuple containing:
            - Visualization image (or None if no frames available)
            - List of detections with format: [x1, y1, x2, y2, conf, class_id, distance]
        """
        depth_frame, color_frame = self.get_aligned_frames()
        if not depth_frame or not color_frame:
            return None, []

        color_image = np.asanyarray(color_frame.get_data())
        
        # Get depth mask for active plane
        min_dist, max_dist = self.config.depth_planes[self.config.active_plane]
        depth_mask = self.create_depth_mask(depth_frame, min_dist, max_dist)
        
        # Apply depth mask
        masked_image = cv2.bitwise_and(color_image, color_image, mask=depth_mask)
        
        # Perform detection
        results = self.model(masked_image, conf=self.config.conf_threshold)[0]
        
        detections = []
        # Process detections
        for detection in results.boxes.data:
            x1, y1, x2, y2, conf, class_id = detection
            x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
            
            # Calculate center point distance
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)
            distance = depth_frame.get_distance(center_x, center_y)
            
            if min_dist <= distance <= max_dist:
                detections.append([x1, y1, x2, y2, conf, class_id, distance])
                
                # Draw detection on visualization
                cv2.rectangle(color_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f'Object ({self.config.active_plane}): {distance:.2f}m'
                cv2.putText(color_image, label, (x1, y1 - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return color_image, detections

    def release(self):
        """Release resources"""
        if self.pipeline:
            self.pipeline.stop()