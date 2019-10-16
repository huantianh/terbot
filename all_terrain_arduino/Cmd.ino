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

      roboclaw.ForwardM1(address, 50);
      roboclaw.ForwardM2(address, 50);
      Serial.println("Moving Forward!");
      break;

    /////////////////////////////////////////////////////////////////            Move Robot Backward
    case 'b':
    case 'B':

      roboclaw.BackwardM1(address, 50);
      roboclaw.BackwardM2(address, 50);
      Serial.println("Moving Backward!");
      break;

  
    /////////////////////////////////////////////////////////////////            Left
    case 'l':
    case 'L':

      roboclaw.ForwardM1(address, 20);
      roboclaw.ForwardM2(address, 50);
      Serial.println("Left!");
      break;

    /////////////////////////////////////////////////////////////////            Right
    case 'r':
    case 'R':

      roboclaw.ForwardM1(address, 50);
      roboclaw.ForwardM2(address, 20);
      Serial.println("Right!");
      break;  
  
  }
}
