import cv2
from picamera2 import Picamera2

# Initialize camera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "BGR888"
picam2.configure("preview")

# Start camera
picam2.start()

# Capture frame (in RGB format)
frame = picam2.capture_array()

# Convert RGB to BGR for OpenCV
frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

# Save to file
cv2.imwrite("captured_image.jpg", frame_bgr)

print("Image saved as 'captured_image.jpg'")