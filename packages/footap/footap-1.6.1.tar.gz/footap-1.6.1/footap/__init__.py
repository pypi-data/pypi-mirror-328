"""
FootAP - Football Analysis Package
"""

__version__ = "1.6.1"

from .video_processing import track_ball_and_feet
from .main import analyze_ball_touch, main

__author__ = "Dims"

# Exposer les fonctions principales
__all__ = ['analyze_ball_touch', 'track_ball_and_feet', 'main']
