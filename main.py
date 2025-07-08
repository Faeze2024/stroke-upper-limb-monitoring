import cv2
import mediapipe as mp
import numpy as np
import csv
import time

mp_pose = mp.solutions.pose # type: ignore
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))
    return np.degrees(angle)

# آماده‌سازی فایل CSV
csv_filename = 'joint_angles.csv'
with open(csv_filename, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow'])

cap = cv2.VideoCapture(0)

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks:
            h, w, _ = frame.shape
            lm = results.pose_landmarks.landmark

            left_shoulder = [lm[11].x * w, lm[11].y * h]
            left_elbow = [lm[13].x * w, lm[13].y * h]
            left_wrist = [lm[15].x * w, lm[15].y * h]
            left_hip = [lm[23].x * w, lm[23].y * h]

            right_shoulder = [lm[12].x * w, lm[12].y * h]
            right_elbow = [lm[14].x * w, lm[14].y * h]
            right_wrist = [lm[16].x * w, lm[16].y * h]
            right_hip = [lm[24].x * w, lm[24].y * h]

            # زاویه‌ها
            left_elbow_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
            right_elbow_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)
            left_shoulder_angle = calculate_angle(left_hip, left_shoulder, left_elbow)
            right_shoulder_angle = calculate_angle(right_hip, right_shoulder, right_elbow)

            # ذخیره در CSV
            timestamp = time.time()
            with open(csv_filename, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, left_shoulder_angle, right_shoulder_angle,
                                 left_elbow_angle, right_elbow_angle])

            # نمایش روی تصویر
            cv2.putText(frame, f"L-Elbow: {int(left_elbow_angle)}", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
            cv2.putText(frame, f"R-Elbow: {int(right_elbow_angle)}", (30, 90),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
            cv2.putText(frame, f"L-Shoulder: {int(left_shoulder_angle)}", (30, 130),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
            cv2.putText(frame, f"R-Shoulder: {int(right_shoulder_angle)}", (30, 170),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

        cv2.imshow("Pose with Angles", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
