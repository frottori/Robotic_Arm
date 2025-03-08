import serial
import keyboard  # Install using `pip install keyboard`

# Configure the serial connection
arduino = serial.Serial('COM3', 9600)  # Replace 'COM3' with your port

try:
    while True:
        # Send commands based on key presses
        if keyboard.is_pressed('a'):
            arduino.write(b'a')  # Increment Servo 1 angle
        elif keyboard.is_pressed('d'):
            arduino.write(b'd')  # Decrement Servo 1 angle
        elif keyboard.is_pressed(','):
            arduino.write(b',')  # Increment Servo 2 angle
        elif keyboard.is_pressed('.'):
            arduino.write(b'.')  # Decrement Servo 2 angle
        elif keyboard.is_pressed('q'):
            arduino.write(b'q')  # Increment Servo 3 angle
        elif keyboard.is_pressed('e'):
            arduino.write(b'e')  # Decrement Servo 3 angle
        elif keyboard.is_pressed('w'):
            arduino.write(b'w')  # Increment Servo 4 angle
        elif keyboard.is_pressed('s'):
            arduino.write(b's')  # Decrement Servo 4 angle
finally:
    arduino.close()
