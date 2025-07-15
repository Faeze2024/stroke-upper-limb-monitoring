import cv2
import time
import streamlit as st
from src.pose_estimation import get_landmarks
from src.angle_calculation import calculate_angle
from src.data_saver import init_csv, save_angles
import threading

# قفل سراسری برای ایمنی در multithreading
lock = threading.Lock()

def process_video(input_type, video_path, csv_filename, state_key):
    cap = None
    if input_type == "Webcam":
        cap = cv2.VideoCapture(0)
    elif video_path:
        cap = cv2.VideoCapture(video_path)
    else:
        st.warning("No video source provided!")
        return

    init_csv(csv_filename)
    data = []
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) if input_type != "Webcam" else 0
    frame_idx = 0

    progress_bar = st.empty()
    video_placeholder = st.empty()  # برای نمایش فریم به کاربر

    stop = False
    stop_button = st.button("🛑 Stop processing")

    while cap.isOpened() and not stop:
        ret, frame = cap.read()
        if not ret:
            break

        # نمایش تصویر فریم در Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)


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

            # ذخیره ایمن در فایل
            with lock:
                save_angles(csv_filename, timestamp, left_shoulder_angle, right_shoulder_angle,
                            left_elbow_angle, right_elbow_angle)

            data.append({
                "timestamp": timestamp,
                "left_elbow": left_elbow_angle,
                "right_elbow": right_elbow_angle,
                "left_shoulder": left_shoulder_angle,
                "right_shoulder": right_shoulder_angle
            })

        frame_idx += 1
        if input_type != "Webcam" and frame_count > 0:
            progress = min(frame_idx / frame_count, 1.0)
            progress_bar.progress(progress)

        if stop_button:
            stop = True
            break

    cap.release()
    st.session_state[state_key] = data
    st.success("✅ Processing completed!")
