import RPi.GPIO as GPIO
import time

SERVO_PIN = 17  # Change to the pin you're testing

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Create PWM instance at 50Hz
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def set_angle(angle):
    duty = (angle / 18.0) + 2.5  # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)

try:
    print("Moving servo...")
    set_angle(90)
    time.sleep(1)
    set_angle(0)
    time.sleep(1)
    set_angle(180)
    time.sleep(1)

finally:
    pwm.stop()
    GPIO.cleanup()
    print("Test complete.")
