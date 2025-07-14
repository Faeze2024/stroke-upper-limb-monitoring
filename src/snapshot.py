# src/snapshot.py
import cv2
from datetime import datetime

def save_snapshot(frame):
    filename = f"snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    cv2.imwrite(filename, frame)
    return filename
