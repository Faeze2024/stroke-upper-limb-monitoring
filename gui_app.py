# gui_app.py یا main.py

import cv2
import time
from src.pose_estimation import get_landmarks
from src.angle_calculation import calculate_angle
from src.data_saver import init_csv, save_angles

csv_filename = 'joint_angles.csv'
init_csv(csv_filename)

cap = cv2.VideoCapture(0)

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        landmarks = get_landmarks(frame)
        if landmarks:
            h, w, _ = frame.shape
            lm = landmarks

            left_shoulder = [lm[11].x * w, lm[11].y * h]
            left_elbow = [lm[13].x * w, lm[13].y * h]
            left_wrist = [lm[15].x * w, lm[15].y * h]
            left_hip = [lm[23].x * w, lm[23].y * h]

            right_shoulder = [lm[12].x * w, lm[12].y * h]
            right_elbow = [lm[14].x * w, lm[14].y * h]
            right_wrist = [lm[16].x * w, lm[16].y * h]
            right_hip = [lm[24].x * w, lm[24].y * h]

            left_elbow_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
            right_elbow_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)
            left_shoulder_angle = calculate_angle(left_hip, left_shoulder, left_elbow)
            right_shoulder_angle = calculate_angle(right_hip, right_shoulder, right_elbow)

            timestamp = time.time()
            save_angles(csv_filename, timestamp, left_shoulder_angle, right_shoulder_angle,
                        left_elbow_angle, right_elbow_angle)

            cv2.putText(frame, f"L-Elbow: {int(left_elbow_angle)}", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
            cv2.putText(frame, f"R-Elbow: {int(right_elbow_angle)}", (30, 90),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
            cv2.putText(frame, f"L-Shoulder: {int(left_shoulder_angle)}", (30, 130),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
            cv2.putText(frame, f"R-Shoulder: {int(right_shoulder_angle)}", (30, 170),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

        cv2.imshow("Pose with Angles", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
