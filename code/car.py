#import library
import RPi.GPIO as GPIO
import time

class car:
    def __init__(self):
        #motor pin at 11 and 12, pwm pin at 13
        self.motor1a = 11
        self.motor1b = 12
        self.motorpwm = 13
        #setup pinmode of raspberry pi
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.motor1a, GPIO.OUT)
        GPIO.setup(self.motor1b, GPIO.OUT)
        GPIO.setup(self.motorpwm, GPIO.OUT)
        #setup pwm rate
        self.pwmrate = 0
        
    #function letting car running forward
    def forward(self):
        GPIO.output(self.motor1a, True)
        GPIO.output(self.motor1b, False)
        pwm = GPIO.PWM(self.motorpwm, 1000)
        pwm.start(100)
        #hold the state for 5seconds
        time.sleep(5)
        
    #function driving car backwards
    def back(self):
        GPIO.output(self.motor1a, False)
        GPIO.output(self.motor1b, True)
        pwm = GPIO.PWM(self.motorpwm, 1000)
        pwm.start(100)
        #hold the state for 5seconds
        time.sleep(5)

    #functino stop the car
    def stop(self):
        GPIO.output(self.motor1a, False)
        GPIO.output(self.motor1b, False)


#testing script        
if __name__ == '__main__':
    c = car()
    c.forward()
    c.stop()
    time.sleep(5)
    c.back()
    c.stop()
