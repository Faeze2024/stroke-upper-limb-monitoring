# 🧠 Stroke Upper Limb Monitoring

A computer vision-based tool to monitor and analyze upper limb movements in post-stroke patients, built with Python, MediaPipe BlazePose, and Streamlit.

---

## 📌 About this project

Stroke survivors often suffer from limited range of motion in their upper limbs.  
This project automatically detects and tracks key joint angles (shoulder, elbow, wrist) during rehabilitation exercises.  
It helps clinicians and researchers analyze movement quality over time by:

- Extracting joint coordinates from live webcam or uploaded videos
- Calculating angles
- Storing them in CSV
- Visualizing motion data in real time
- Generating PDF reports

---

## ✨ Features

- ✅ Live tracking of upper limb keypoints (shoulder, elbow, wrist)
- 📐 Calculation and storage of joint angles over time
- 📊 Real-time plotting of joint angles
- 📸 Capture and save snapshot images during exercise
- 📝 Generate PDF reports from tracked data
- 🔄 Multi-threaded processing with thread-safe design (Lock) for better performance
- 🧩 Modular code structure for easier extension or customization

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YourUsername/stroke-upper-limb-monitoring.git
cd stroke-upper-limb-monitoring
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ⚙️ How to activate the virtual environment (Windows)

We included a script named `activate_venv.bat`.

📦 Steps:

1. If you haven't created the virtual environment yet:

```bash
python -m venv venv
```

2. Activate:

Just double-click on:
```
activate_venv.bat
```

✅ You'll see your prompt change to `(venv)`

To deactivate, just type:
```
deactivate
```

---

## 🚀 How to use

Run the Streamlit app:

```bash
streamlit run gui_app.py
```

Features:

- Choose between webcam or uploaded video
- Start processing to:
  - Capture frames
  - Detect landmarks
  - Calculate angles
  - Save data as CSV
- 📊 Visualize angles over time in a real-time chart
- 📸 Take snapshot of current frame
- 📝 Generate PDF report with one click

---

## 📊 Output

- CSV file with timestamps and calculated joint angles
- Real-time matplotlib chart
- Saved snapshot images
- PDF report from tracked data

---

## 🛠 Project structure

```
stroke-upper-limb-monitoring/
├── data/                  # Saved CSV files & snapshots
├── plots/                 # Generated plots
├── src/                   # Core Python modules
│   ├── angle_calculation.py
│   ├── camera_stream.py
│   ├── data_saver.py
│   ├── pose_estimation.py
│   ├── report_generator.py
│   ├── snapshot.py
│   └── video_processor.py
├── gui_app.py             # Streamlit main app
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ✅ TODO

- Fully live video preview while processing
- Add multiprocessing or asyncio to improve performance on large videos
- Add docstrings & auto-generated documentation
- Export data in more formats (Excel, JSON)
- User authentication and session management

---

## 🤖 Built with

- Python
- MediaPipe BlazePose
- OpenCV
- Streamlit
- NumPy
- Matplotlib

---

## 📝 License

This project is licensed under the MIT License.

---

⭐ If you like this project, please star the repo or contribute!