import RPi.GPIO as gpio
import time

gpio.setwarnings(False)

def distance(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(12, gpio.OUT)
    gpio.setup(16, gpio.IN)
    
    time.sleep(0.00001)
    gpio.output(12, False)
    while gpio.input(16) == 0:
        nosig = time.time()
        
    while gpio.input(16) == 1:
        sig = time.time()
    
    tl = sig - nosig
    
    if measure == 'cm':
        distance = tl / 0.000058
    elif measure == 'in':
        distance = tl / 0.000148
    else:
        print('improper choice of measurement: in or cm')
        distance = None
    
    gpio.cleanup()
    return distance


try:
    print(distance('cm'))
except KeyboardInterrupt:
    gpio.cleanup()
