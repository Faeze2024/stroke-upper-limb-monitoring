import cv2
import threading

class CameraStream:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        self.frame = None
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.update, daemon=True)
            self.thread.start()

    def update(self):
        while self.running:
            ret, frame = self.stream.read()
            if ret:
                self.frame = frame

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
        self.stream.release()
