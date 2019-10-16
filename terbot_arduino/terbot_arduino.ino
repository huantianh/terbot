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
  roboclaw.begin(115200);
  Serial.begin(115200);
}

void loop() {
  receiveBytes();
}
