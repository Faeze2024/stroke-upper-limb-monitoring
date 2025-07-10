# 🧠 Stroke Upper Limb Monitoring

A computer vision-based tool to monitor and analyze upper limb movements in post-stroke patients, built with Python and MediaPipe BlazePose.

---

## 📌 About this project

Stroke survivors often suffer from limited range of motion in their upper limbs.\
This project aims to automatically detect and track key joint angles (shoulder, elbow, wrist) during rehabilitation exercises, helping clinicians and researchers analyze movement quality over time.

We extract joint coordinates from live webcam or images, calculate angles, store them, and visualize motion data in real time.\
Additionally, the tool can compare actual patient motion data against a predefined reference pattern to track progress.

---

## ✨ Features

- Live tracking of upper limb keypoints (shoulder, elbow, wrist)
- Calculation and storage of joint angles over time
- Real-time plotting of joint angles
- Comparison against reference movement curves
- Simple Python interface for extending or customizing

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

## 🚀 How to use

Run the main script to start capturing and analyzing movements:

```bash
python main.py
```

By default, it:

- Captures from webcam
- Detects keypoints
- Calculates angles
- Saves data as CSV
- Draws live plot of angles vs time

---

## 📊 Output

- CSV file with timestamps and calculated joint angles
- Real-time matplotlib chart of movement
- Optional comparison with predefined reference curves for analysis

---

## 🛠 Project structure

```
stroke-upper-limb-monitoring/
├── data/                # Saved CSV files
├── plots/               # Generated plots
├── src/                 # Python scripts and modules
│   ├── pose_estimation.py
│   ├── angle_calculation.py
│   └── plotting.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ✅ TODO

- Add GUI or web dashboard for easier use
- Support for full upper body keypoints
- Save and compare sessions per user/patient
- Generate PDF reports for therapists
- Export data in common formats (Excel, JSON)

---

## 🤖 Built with

- Python
- MediaPipe BlazePose
- OpenCV
- NumPy
- Matplotlib

---

## 📝 License

This project is licensed under the MIT License.

---

If you like this project, feel free to ⭐️ the repo or contribute!

