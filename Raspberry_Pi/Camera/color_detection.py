import cv2
import numpy as np
from picamera2 import Picamera2

# Initialize camera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "BGR888"
picam2.configure("preview")
picam2.start()

# Capture frame
frame = picam2.capture_array()
frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

# Convert to HSV
hsv = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2HSV)

# Define color ranges (HSV)
colors = {
    "Red": ([0, 120, 70], [10, 255, 255]),
    "Blue": ([100, 150, 0], [140, 255, 255]),
    "Green": ([40, 40, 40], [80, 255, 255]),
    "Yellow": ([20, 100, 100], [30, 255, 255])
}
detected_colors = []

# Check for each color
for color_name, (lower, upper) in colors.items():
    lower_bound = np.array(lower)
    upper_bound = np.array(upper)
    
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    if np.any(mask):  # If mask has white pixels, color is detected
        detected_colors.append(color_name)

if detected_colors:
    print("Detected Colors:", ", ".join(detected_colors))
else:
    print("No color detected.")

cv2.imwrite("detected_color.jpg", frame_bgr)