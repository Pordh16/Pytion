from machine import Pin
from utime import sleep

print("AUTISTIC")

led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(13, Pin.OUT)
led4 = Pin(12, Pin.OUT)
led5 = Pin(11, Pin.OUT)
while True:
  led1.toggle()
  sleep(0.5)
  led2.toggle()
  sleep(0.5)
  led3.toggle()
  sleep(0.5)
  led4.toggle()
  sleep(0.5)
  led5.toggle()
  sleep(0.5)
 