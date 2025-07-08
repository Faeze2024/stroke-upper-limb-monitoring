# 🧠 Smart Upper Limb Monitoring System

A Python-based system for monitoring and analyzing upper limb joint angles (shoulder, elbow, wrist) for stroke rehabilitation using MediaPipe BlazePose.

---

## 📌 Project Goals
- Extract real-time joint keypoints from webcam/video
- Calculate and record joint angles over time
- Plot angle changes for visual analysis
- Compare patient's motion to reference movement
- Help clinicians monitor and evaluate stroke rehabilitation progress

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
pip install -r requirements.txt
```

---

## 🚀 Usage

### Step 1: Capture joint angles
Run the script to detect upper limb keypoints and calculate joint angles:
```bash
python main.py
```
- Use webcam or video file as input.
- Extract shoulder, elbow, and wrist keypoints.
- Save joint angles to CSV.

---

### Step 2: Plot and analyze
The script also:
- Plots joint angle curves over time.
- Compares patient’s data with synthetic reference data.
- Saves plots to `output/` folder.

---

## 📊 Output

- CSV file with frame-by-frame joint angles
- Angle plots (`plot_patient.png`)
- Comparison plots (`plot_comparison.png`)

---

## 🧩 Project Structure

```
├── main.py                # Main script to process video and compute angles
├── reference_data.py      # Generates synthetic reference angles
├── utils.py               # Helper functions (angle calculation, plotting)
├── output/                # Generated CSV and plots
│   ├── angles.csv
│   ├── plot_patient.png
│   └── plot_comparison.png
├── requirements.txt
├── README.md
└── TODO.md
```

---

## ✅ Current progress
- [x] Extract and save joint angles (shoulder, elbow, wrist)
- [x] Plot angles over time
- [x] Generate synthetic reference data
- [x] Compare patient data to reference

---

## 📌 Planned improvements (see TODO.md)
- Apply smoothing filter to angle data
- Compute and display quantitative error (e.g., MAE, RMSE)
- Build unit tests for helper functions
- Add more metrics (speed, range of motion)
- Create an interactive dashboard or web app

---

## 🤝 Contributing
Feel free to fork this repository and open pull requests!
For major changes, please open an issue first to discuss what you’d like to add.

---

## 📄 License
MIT License

---
Test push from local
