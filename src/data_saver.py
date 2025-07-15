import os
import csv

def init_csv(filename):
    folder = os.path.dirname(filename)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "left_shoulder", "right_shoulder", "left_elbow", "right_elbow"])

def save_angles(filename, timestamp, left_shoulder, right_shoulder, left_elbow, right_elbow):
    with open(filename, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, left_shoulder, right_shoulder, left_elbow, right_elbow])
