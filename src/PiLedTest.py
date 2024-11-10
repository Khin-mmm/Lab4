import time
from time import sleep

from hal import hal_led as led
from hal import hal_input_switch as switch

def blink_led(delay):
    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

def main():
    led.init()
    switch.init()
    
    while 1:
        if switch.read_slide_switch() == 1:
            blink_led(0.2)

        else:
            startingTime = time.time()
            while time.time() - startingTime < 5:
                blink_led(0.1)

            led.set_output(0, 0)
            time.sleep(1)
    
if __name__ == "__main__":
    main()