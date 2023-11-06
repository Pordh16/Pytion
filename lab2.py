from machine import Pin
import time

pin13 = Pin(13,Pin.OUT)
pin14 = Pin(14,Pin.OUT)
pin15 = Pin(15,Pin.OUT)


while True:
    pin13.on()
    pin14.on()
    pin15.on()
    time.sleep_ms(500)
    pin13.off()
    pin14.off()
    pin15.off()
    time.sleep_ms(500)
    pin13.on()
    pin14.on()
    pin15.on()