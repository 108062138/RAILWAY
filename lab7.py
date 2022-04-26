import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(5,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11,GPIO.OUT)
#buzzer
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)

threads = []
pressed = -1
state = 1
count = 0
direction = 1
class Button:
    def Button():
        global pressed
        #if GPIO.input(7) ==GPIO.HIGH:
        #    pressed = False;
        while True:
            if GPIO.input(7) == GPIO.HIGH:
                pressed *= -1
            time.sleep(0.5)

class Light:  
    def Light():
        global pressed
        while True:
            if pressed == 1 or count != 0:
                GPIO.output(3,GPIO.LOW)
                GPIO.output(5,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(3,GPIO.HIGH)
                GPIO.output(5,GPIO.LOW)
                time.sleep(0.5)
            else:
                GPIO.output(3,GPIO.LOW)
                GPIO.output(5,GPIO.LOW)
class Buzzor:        
    def Buzzor():
        while True:
            if pressed == 1 or count !=0:
                GPIO.output(13, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(13,GPIO.LOW)
                time.sleep(0.5)
            else:
                GPIO.output(13, GPIO.LOW)
                
class Servo:        
    def Servo():
        global pressed, state, count, direction
        p = GPIO.PWM(11,50)
        p.start(0)
        while True:
            if pressed == 1:
                if count <5:
                    count+=direction
                p.ChangeDutyCycle(count)
                time.sleep(0.1)
                print("count = {0} and the direction = {1}".format(count,direction))
            else:
                if count > 0:
                    count -= direction
                    p.ChangeDutyCycle(count)
                    time.sleep(0.1)
                    print("count = {0} and the direction = {1}".format(count,direction))


threads.append(threading.Thread(target = Button.Button))
threads.append(threading.Thread(target = Light.Light))
threads.append(threading.Thread(target = Buzzor.Buzzor))
threads.append(threading.Thread(target = Servo.Servo))
threads[0].start()
threads[1].start()
threads[2].start()
threads[3].start()
threads[0].join()
threads[1].join()
threads[2].join()
threads[3].join()
