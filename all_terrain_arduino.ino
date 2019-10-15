//Includes required to use Roboclaw library
#include <SoftwareSerial.h>
#include "RoboClaw.h"

//See limitations of Arduino SoftwareSerial
SoftwareSerial serial(19, 18);
RoboClaw roboclaw(&serial, 10000);

#define address 0x80

char rcv_buffer[64];

void setup() {
  //Open roboclaw serial ports
  roboclaw.begin(9600);
  Serial.begin(9600);
}

void loop() {
  receiveBytes();
  
  //  roboclaw.ForwardBackwardM1(address,96); //start Motor1 forward at half speed
  //  roboclaw.ForwardBackwardM2(address,32); //start Motor2 backward at half speed
  //  delay(2000);
  //
  //  roboclaw.ForwardBackwardM1(address,32);
  //  roboclaw.ForwardBackwardM2(address,96);
  //  delay(2000);
}
