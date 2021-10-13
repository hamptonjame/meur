#include <ZumoMotors.h>
ZumoMotors motors;
String cmd;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  motors.setSpeeds(0,0);
  delay(2000);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    cmd = Serial.readStringUntil('\n');
    cmd.trim();
    if(cmd == "forward") {
      motors.setSpeeds(200,200);
    } else if(cmd == "backward") {
      motors.setSpeeds(-200,-200);
    } 
    else if(cmd == "left") {
      motors.setSpeeds(-200,200);
    } else if(cmd == "right") {
      motors.setSpeeds(200,-200);
    }
  } else {
    delay(1000);
    motors.setSpeeds(0,0);
  }
}
