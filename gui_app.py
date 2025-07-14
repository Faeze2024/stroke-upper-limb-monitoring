import streamlit as st
from src.video_processor import process_video

# حالت پیش‌فرض برای فلگ stop
if 'stop_processing' not in st.session_state:
    st.session_state['stop_processing'] = False

st.title("🧠 Stroke Upper Limb Monitoring")

input_type = st.radio("Select Input Type:", ["Webcam", "Video File"])
video_path = None
if input_type == "Video File":
    video_file = st.file_uploader("Upload video file", type=["mp4", "mov", "avi"])
    if video_file:
        video_path = f"temp_{video_file.name}"
        with open(video_path, "wb") as f:
            f.write(video_file.read())

csv_filename = "data/session_data.csv"

if st.button("▶ Start Processing"):
    st.session_state['stop_processing'] = False
    process_video(input_type, video_path, csv_filename, state_key="session_data")

# دکمه توقف
if st.button("⏹ Stop"):
    st.session_state['stop_processing'] = True

# پیام راهنما
st.info("⚠ برای توقف پردازش، روی دکمه ⏹ Stop کلیک کنید.")
