from machine import Pin, PWM, ADC

adc = ADC(Pin(26))
pwm1 = PWM(Pin(13))
pwm1.freq(1000)

pwm2 = PWM(Pin(14))
pwm2.freq(1000)

pwm3 = PWM(Pin(15))
pwm3.freq(1000)

pwm1.freq(1000)
pwm2.freq(1000)
pwm3.freq(1000)

while True:
    duty = adc.read_u16()
    pwm1.duty_u16(duty)
    duty = adc.read_u16()
    pwm2.duty_u16(duty)
    duty = adc.read_u16()
    pwm3.duty_u16(duty)
    
    
    