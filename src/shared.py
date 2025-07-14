# src/shared.py
import threading

# lock سراسری برای دسترسی thread-safe به داده‌ها
lock = threading.Lock()
