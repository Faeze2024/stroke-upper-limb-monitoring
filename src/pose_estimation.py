# src/pose_estimation.py

import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose #type: ignore
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

def get_landmarks(frame):
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    if results.pose_landmarks:
        return results.pose_landmarks.landmark
    return None
