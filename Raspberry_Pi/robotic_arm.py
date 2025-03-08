import RPi.GPIO as GPIO
import time

# Define GPIO pins for the servos
SERVO_PINS = [27, 17, 22, 5, 6, 23]

# Setup
GPIO.setmode(GPIO.BCM)

# Initialize all servo pins as output and store PWM instances in a dictionary
servos = {}
for pin in SERVO_PINS:
    GPIO.setup(pin, GPIO.OUT)
    servos[pin] = GPIO.PWM(pin, 50)
    servos[pin].start(0)

"""Set angle for a specific servo motor."""
def set_angle(pin, angle):
    duty = (angle / 18.0) + 2.5  # Convert angle to duty cycle
    servos[pin].ChangeDutyCycle(duty)
    time.sleep(0.5)  # Allow servo to move

def starting_position():
    set_angle(5, 70) # Elbow
    time.sleep(1)
    set_angle(6, 135) # Shoulder
    time.sleep(1)
    set_angle(23, 0) # Base
    time.sleep(1)
    set_angle(27, 90) # Gripper
    time.sleep(1)
    set_angle(17, 0) # Wrist Pitch
    time.sleep(1)
    # set_angle(22, 0) # Wrist Roll -> dont need to move
    # time.sleep(1)

def pick_up_object():
    set_angle(17,90)
    time.sleep(1)
    set_angle(5, 90)
    time.sleep(1)
    set_angle(6, 105)
    time.sleep(1)
    set_angle(17, 20)
    time.sleep(1)
    set_angle(27, 45)
    time.sleep(1)
    set_angle(5, 70) # Elbow
    time.sleep(1)
    set_angle(6, 135) # Shoulder
    time.sleep(1)
    set_angle(23, 65) # Base
    time.sleep(1)
    set_angle(5, 90)
    time.sleep(1)
    set_angle(27, 90)
    time.sleep(1)
    set_angle(5, 70) # Elbow
    time.sleep(1)
    set_angle(6, 135) # Shoulder
    time.sleep(1)
    set_angle(23, 0) # Base
    time.sleep(1)
try:
    starting_position()
    pick_up_object()
finally:
    # Stop all PWM instances
    for pwm in servos.values():
        pwm.stop()
    GPIO.cleanup()
    print("Robotic arm test complete.")