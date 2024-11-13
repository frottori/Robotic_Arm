#include <Servo.h>

Servo myServo1,myServo2,myServo3,myServo4; // Create a Servo object

void setup() {
  myServo1.attach(9); // Attach servo to Pin 7
}

void loop() {
  // Move the arm up
  myServo1.write(0); // Move to 0 degrees
  delay(1000); 
  
  // Move the arm down
  myServo1.write(180); // Move to 180 degrees
  delay(1000); 
}
