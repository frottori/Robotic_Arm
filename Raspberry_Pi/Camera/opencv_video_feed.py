import cv2
import time
from picamera2 import Picamera2

# Initialize camera
picam2 = Picamera2()

# Configure preview for video (you can tweak resolution)
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "BGR888"
picam2.configure("preview")

# Start camera
picam2.start()

# Define video writer (filename, codec, fps, resolution)
output_filename = "captured_video.avi"
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # or 'MJPG' for smaller files
fps = 20.0
resolution = (640, 480)

out = cv2.VideoWriter(output_filename, fourcc, fps, resolution)

# Capture video for 10 seconds
start_time = time.time()
duration = 5  # seconds

print(f"🎥 Recording video for {duration} seconds...")

while time.time() - start_time < duration:
    frame = picam2.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    out.write(frame)

print(f"Video saved as '{output_filename}'")

# Release resources
out.release()
picam2.stop()
