# src/data_saver.py

import csv

def init_csv(filename):
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow'])

def save_angles(filename, timestamp, left_shoulder_angle, right_shoulder_angle, left_elbow_angle, right_elbow_angle):
    with open(filename, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, left_shoulder_angle, right_shoulder_angle, left_elbow_angle, right_elbow_angle])
