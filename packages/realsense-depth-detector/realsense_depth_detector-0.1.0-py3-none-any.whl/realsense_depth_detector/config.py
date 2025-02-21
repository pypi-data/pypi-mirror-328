from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass
class DepthConfig:
    depth_planes: Dict[str, Tuple[float, float]]
    active_plane: str
    conf_threshold: float = 0.7
    depth_resolution: Tuple[int, int] = (848, 480)
    color_resolution: Tuple[int, int] = (848, 480)
    fps: int = 30
