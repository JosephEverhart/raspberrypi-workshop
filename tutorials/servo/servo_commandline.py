#!/usr/bin/python

import time
import sys
from RPIO import PWM

start=600
end= 2600
step = (end - start) / 10
def move(dest):
  """Move servo on pin 17 to a given angle"""
  servo = PWM.Servo()
  # Set servo on GPIO17 to 1200s (1.2ms)
  point = (end - start) * int(dest)/180 
  servo.set_servo(17, start + point - (point % 100))
  time.sleep(0.5)

#servo.stop_servo(17)

if __name__ == "__main__":
  import sys
  move(sys.argv[1])
