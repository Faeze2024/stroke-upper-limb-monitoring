import pandas as pd
import matplotlib.pyplot as plt

# خواندن داده‌های واقعی و مرجع
df_user = pd.read_csv('joint_angles.csv')
df_ref = pd.read_csv('reference_angles.csv')

plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
plt.plot(df_user['left_shoulder'], label='User Left Shoulder', color='blue')
plt.plot(df_ref['left_shoulder'], label='Reference Left Shoulder', color='red', linestyle='dashed')
plt.title('Left Shoulder Angle')
plt.ylabel('Angle (deg)')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(df_user['right_shoulder'], label='User Right Shoulder', color='blue')
plt.plot(df_ref['right_shoulder'], label='Reference Right Shoulder', color='red', linestyle='dashed')
plt.title('Right Shoulder Angle')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(df_user['left_elbow'], label='User Left Elbow', color='blue')
plt.plot(df_ref['left_elbow'], label='Reference Left Elbow', color='red', linestyle='dashed')
plt.title('Left Elbow Angle')
plt.ylabel('Angle (deg)')
plt.xlabel('Frame')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(df_user['right_elbow'], label='User Right Elbow', color='blue')
plt.plot(df_ref['right_elbow'], label='Reference Right Elbow', color='red', linestyle='dashed')
plt.title('Right Elbow Angle')
plt.xlabel('Frame')
plt.legend()

plt.tight_layout()
plt.show()
