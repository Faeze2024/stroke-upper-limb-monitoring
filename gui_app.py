# gui_app.py
import streamlit as st
import tempfile
import threading
import pandas as pd
import matplotlib.pyplot as plt
from src import video_processor, report_generator

st.set_page_config(page_title="Pose Angle Tracker", layout="wide")
st.title("🧍‍♂️ Pose Angle Tracker")

input_type = st.radio("Select input type:", ("Webcam", "Upload video"))
video_path = None

if input_type == "Upload video":
    video_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])
    if video_file:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video_file.read())
        video_path = tfile.name
elif input_type == "Webcam":
    st.info("Webcam will be used directly when you click Start.")

csv_filename = 'joint_angles.csv'
state_key = 'processed_data'

# دکمه پردازش و اجرای در thread جدا
if st.button("🚀 Start Processing"):
    thread = threading.Thread(
        target=video_processor.process_video,
        args=(input_type, video_path, csv_filename, state_key)
    )
    thread.start()
    st.info("Processing started in background thread...")

# اگر داده پردازش‌شده موجود باشه، نمایش
if state_key in st.session_state:
    data = st.session_state[state_key]
    if data:
        df = pd.DataFrame(data)
        st.subheader("📊 Angle Visualization")
        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(df["timestamp"], df["left_elbow"], label="Left Elbow")
        ax.plot(df["timestamp"], df["right_elbow"], label="Right Elbow")
        ax.plot(df["timestamp"], df["left_shoulder"], label="Left Shoulder")
        ax.plot(df["timestamp"], df["right_shoulder"], label="Right Shoulder")
        ax.set_xlabel("Timestamp")
        ax.set_ylabel("Angle (degrees)")
        ax.legend()
        st.pyplot(fig)

        # دکمه دانلود CSV
        with open(csv_filename, "rb") as f:
            st.download_button("⬇️ Download CSV", f, file_name="joint_angles.csv", mime="text/csv")

# دکمه تولید PDF
if st.button('📄 Generate PDF Report'):
    report_generator.generate_pdf_report(csv_filename, 'report.pdf')
    st.success('PDF report created! 📄✅')
