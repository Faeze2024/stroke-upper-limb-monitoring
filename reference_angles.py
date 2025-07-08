import numpy as np
import pandas as pd

num_frames = 200

# شبیه‌سازی حرکت رفت و برگشت برای شانه چپ
left_shoulder = np.concatenate([
    np.linspace(20, 160, num_frames//2),
    np.linspace(160, 20, num_frames//2)
])

# شانه راست هم تقریباً مشابه با کمی تغییر (مثلاً کمی کمتر)
right_shoulder = np.concatenate([
    np.linspace(25, 150, num_frames//2),
    np.linspace(150, 25, num_frames//2)
])

# شبیه‌سازی خم و باز شدن آرنج چپ
left_elbow = np.concatenate([
    np.linspace(150, 90, num_frames//2),
    np.linspace(90, 150, num_frames//2)
])

# آرنج راست هم تقریباً مشابه
right_elbow = np.concatenate([
    np.linspace(145, 100, num_frames//2),
    np.linspace(100, 145, num_frames//2)
])

# ساخت دیتافریم
df = pd.DataFrame({
    'left_shoulder': left_shoulder,
    'right_shoulder': right_shoulder,
    'left_elbow': left_elbow,
    'right_elbow': right_elbow
})

# ذخیره در CSV
df.to_csv('reference_angles.csv', index=False)

print('✅ Reference data created and saved to reference_angles.csv')
