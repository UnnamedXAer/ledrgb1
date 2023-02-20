from gpiozero import RGBLED
import RPi.GPIO as GPIO
from time import sleep

# led = RGBLED(22, 27, 17)

# for r in range(2):
# 	for g in range(2):
# 		for b in range(2):
# 			led.color = (r, g, b)
# 			sleep(0.25)
# led.close()


class MyLed:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


attrs = ["r", "g", "b"]

l1 = MyLed(22, 27, 17)
l2 = MyLed(16, 20, 21)
l3 = MyLed(5, 6, 13)


leds = [l1, l2, l3]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for led in leds:
    print("led: ", led, "\n")
    for pin in attrs:
        print("prop: ", pin, ", val: ", led.__dict__[pin])
        GPIO.setup(led.__dict__[pin], GPIO.OUT)
        led.__dict__[pin] = GPIO.PWM(led.__dict__[pin], 100)
        led.__dict__[pin].start(0)
        print(", new val: ", led.__dict__[pin], "\n")

cnt = 0

while True:
    for duty in range(1, 101, 1):
        for led in leds:
            # for pin in attrs:
            led.r.ChangeDutyCycle(duty)
            led.g.ChangeDutyCycle(duty*0.8)
            led.b.ChangeDutyCycle(0 if duty < 30 else (duty-30)/3)
        sleep(0.02)
        # sleep(0.02)
    # sleep(0.5)
    for duty in range(100, 0, -1):
        for led in leds:
            led.r.ChangeDutyCycle(duty)
            led.g.ChangeDutyCycle(duty*0.8)
            led.b.ChangeDutyCycle(0 if duty < 30 else (duty-30)/3)
            # for pin in attrs:
            #   led.__dict__[pin].ChangeDutyCycle(duty)
        sleep(0.02)
    print("cycle: ", cnt)
    cnt += 1
