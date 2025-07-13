# gui_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.pose_estimation import get_landmarks
from src.angle_calculation import calculate_angle
from src.data_saver import init_csv, save_angles

st.set_page_config(page_title="Motion Analysis App", layout="wide")

st.title("🎥 Motion Analysis Dashboard")

# Button to simulate live recording (placeholder)
if st.button("Start Live Recording"):
    st.info("This feature requires connecting to a camera and implementing live processing (not implemented here).")

# Upload CSV file to visualize
uploaded_file = st.file_uploader("Upload a CSV file with joint angles:", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Data Preview")
    st.dataframe(df)

    # Plot angle trends over time
    st.subheader("📈 Joint Angles Over Time")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['timestamp'], df['left_shoulder'], label='Left Shoulder')
    ax.plot(df['timestamp'], df['right_shoulder'], label='Right Shoulder')
    ax.plot(df['timestamp'], df['left_elbow'], label='Left Elbow')
    ax.plot(df['timestamp'], df['right_elbow'], label='Right Elbow')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Angle (degrees)')
    ax.legend()
    st.pyplot(fig)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
