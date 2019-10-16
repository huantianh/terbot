/*******************************              GIVING COMMAND                *******************************************/
void parseCommand()
{
  char command = rcv_buffer[0]; // our first byte tells us the command char is equivalent to byte
  switch (command)
  {
    ////////////////////////////////////////////////////////////////            STOP
    case 's':
    case 'S':

      roboclaw.BackwardM1(address, 0);
      roboclaw.BackwardM2(address, 0);
      Serial.println("Stop!");
      break;

    ////////////////////////////////////////////////////////////////             Move Robot Forward
    case 'f':
    case 'F':

      int pwm;
      sscanf(&rcv_buffer[1], " %d \r", &pwm);
      roboclaw.ForwardM1(address, pwm);
      roboclaw.ForwardM2(address, pwm);
      Serial.println("Moving Forward!");
      break;

    /////////////////////////////////////////////////////////////////            Move Robot Backward
    case 'b':
    case 'B':

      int pwm1;
      sscanf(&rcv_buffer[1], " %d \r", &pwm1);
      roboclaw.BackwardM1(address, pwm1);
      roboclaw.BackwardM2(address, pwm1);
      Serial.println("Moving Backward!");
      break;

    /////////////////////////////////////////////////////////////////            Right
    case 'r':
    case 'R':
    
      int pwm2;
      sscanf(&rcv_buffer[1], " %d \r", &pwm2);
      roboclaw.ForwardM1(address, pwm2);
      roboclaw.BackwardM2(address, pwm2);
      Serial.println("Right!");
      break;

    /////////////////////////////////////////////////////////////////            Left
    case 'l':
    case 'L':
    
      int pwm3;
      sscanf(&rcv_buffer[1], " %d \r", &pwm3);
      roboclaw.ForwardM2(address, pwm3);
      roboclaw.BackwardM1(address, pwm3);
      Serial.println("Left!");
      break;

  }
}
