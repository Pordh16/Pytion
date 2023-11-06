from machine import Pin
import time

pin13 = Pin(13,Pin.OUT)
pin14 = Pin(14,Pin.OUT)
pin15 = Pin(15,Pin.OUT)

for i in range(0,100,1):
    pin13.on()
    time.sleep_ms(250)
    pin13.off()
    time.sleep_ms(250)

    pin14.on()
    time.sleep_ms(250)
    pin14.off()
    time.sleep_ms(250)


    pin15.on()
    time.sleep_ms(250)
    pin15.off()
    time.sleep_ms(250)

    pin14.on()
    time.sleep_ms(250)
    pin14.off()
    time.sleep_ms(250)

    pin13.on()
    time.sleep_ms(250)
    pin13.off()
    time.sleep_ms(250)

