import streamlit as st
from src.video_processor import process_video

st.title("🧠 Stroke Upper Limb Monitoring")

input_type = st.selectbox("Select input source:", ["Webcam", "Video File"])
video_path = None
if input_type == "Video File":
    video_file = st.file_uploader("Upload video file", type=["mp4", "avi"])
    if video_file:
        video_path = f"temp_videos/{video_file.name}"
        with open(video_path, "wb") as f:
            f.write(video_file.getbuffer())

if st.button("▶️ Start processing"):
    csv_filename = "data/session_data.csv"
    process_video(input_type, video_path, csv_filename, state_key="session_data")
