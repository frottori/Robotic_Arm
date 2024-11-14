#include <Servo.h>   
#define SERVO_PIN 7  // PWM Signal
Servo servo;   

void example(){
}

// Swift movement
void Smove(int degrees) {
  for (int pos = 0; pos <= degrees; pos += 1) { // move from 0 to degrees
    servo.write(pos);
    delay(15); // wait 15ms to allow the servo to reach the position
  }
  for (int pos = degrees; pos >= 0; pos -= 1) { // move back from to 0 degrees
    servo.write(pos);
    delay(15);
  }
}

// Gradual Movement
void Gmove(int targetAngle) {
  int currentAngle = servo.read();
  if (currentAngle < targetAngle) {
    for (int pos = currentAngle; pos <= targetAngle; pos++) {
      servo.write(pos);
      delay(10);
    }
  } else {
    for (int pos = currentAngle; pos >= targetAngle; pos--) {
      servo.write(pos);
      delay(10);
    }
  }
}

void setup() {
  servo.attach(SERVO_PIN);  // Connect D7 of Arduino with PWM signal pin of servo motor
}

void loop() {
  // Gradual Movement
  // servo.write(0);
  // Gmove(90);

  // Swift Movement
  //Smove(360);

  servo.write(0);  
  delay(3000);
  servo.detach();  //Stop.
  delay(2000);

  servo.attach(SERVO_PIN);  //Always use attach function after detach to re-connect your servo with the board
  servo.write(180);
  delay(3000);
  servo.detach();  //Stop
  delay(2000);
  servo.attach(SERVO_PIN);
}
