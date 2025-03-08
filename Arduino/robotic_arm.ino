#include <Servo.h>

// Create servo objects for 4 servos
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

// Initial angles
int angle1 = 90, angle2 = 90, angle3 = 90, angle4 = 90;

void setup() {
  servo1.attach(3);
  servo2.attach(5);
  servo3.attach(6);
  servo4.attach(9);

  servo1.write(angle1);
  servo2.write(angle2);
  servo3.write(angle3);
  servo4.write(angle4);

  Serial.begin(9600); // Initialize Serial communication
}

void loop() {
  // Check if data is available
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the incoming character

    // Adjust angles based on commands
    switch (command) {
      case 'a': angle1 = constrain(angle1 + 1, 0, 180); servo1.write(angle1); break;
      case 'd': angle1 = constrain(angle1 - 1, 0, 180); servo1.write(angle1); break;
      case ',': angle2 = constrain(angle2 + 1, 0, 180); servo2.write(angle2); break;
      case '.': angle2 = constrain(angle2 - 1, 0, 180); servo2.write(angle2); break;
      case 'q': angle3 = constrain(angle3 + 1, 0, 180); servo3.write(angle3); break;
      case 'e': angle3 = constrain(angle3 - 1, 0, 180); servo3.write(angle3); break;
      case 'w': angle4 = constrain(angle4 + 1, 0, 180); servo4.write(angle4); break;
      case 's': angle4 = constrain(angle4 - 1, 0, 180); servo4.write(angle4); break;
    }
  }
}
