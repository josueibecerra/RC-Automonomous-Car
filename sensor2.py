import RPi.GPIO as gpio
import time

def distance():
    gpio.setmode(gpio.BOARD)

    TRIG = 12
    ECHO = 16

    gpio.setup(TRIG, gpio.OUT)
    gpio.output(TRIG, 0)

    gpio.setup(ECHO, gpio.IN)

    try:
        time.sleep(0.1)

        gpio.output(TRIG, 1)
        time.sleep(0.00001)
        gpio.output(TRIG, 0)

        while gpio.input(ECHO) == 0:
            pass
        start = time.time()

        while gpio.input(ECHO) == 1:
            pass

        stop = time.time()

        distance = (stop-start)*17000
        gpio.cleanup()
        return distance
    except:
        distance = 100
        gpio.cleanup()
        return distance

distance()