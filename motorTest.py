import gpiozero as GPIO
import time

class stepperMotor():
    def __init__(self, pin1:int, pin2:int, pin3:int, pin4:int, delay:float = 0.001):
        self.c1 = GPIO.DigitalOutputDevice(pin1)
        self.c2 = GPIO.DigitalOutputDevice(pin2)
        self.c3 = GPIO.DigitalOutputDevice(pin3)
        self.c4 = GPIO.DigitalOutputDevice(pin4)
        self.delay = delay
    
    def allOff(self):
        self.c1.off()
        self.c2.off()
        self.c3.off()
        self.c4.off()

    def stepForwards(self):
        self.c1.on()
        self.c2.on()
        self.c3.off()
        self.c4.off()
        time.sleep(self.delay)
        self.c1.off()
        self.c2.on()
        self.c3.on()
        self.c4.off()
        time.sleep(self.delay)
        self.allOff()

    def stepBackwards(self):
        self.c1.off()
        self.c2.off()
        self.c3.on()
        self.c4.on()
        time.sleep(self.delay)
        self.c1.on()
        self.c2.off()
        self.c3.off()
        self.c4.on()
        time.sleep(self.delay)
        self.allOff()

workingGPIOPins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 22, 23, 24, 25, 26, 27]

motor1 = stepperMotor(22, 23, 24, 25)

while True:
    for a in range(0, 360):
        motor1.stepForwards()
    for a in range(0, 360):
        motor1.stepBackwards()