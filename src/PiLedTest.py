import time
from time import sleep
from hal import hal_led as led
from hal import hal_input_switch as sw

def main():
  sw.init()
  led.init()
  while True:
    while sw.read_slide_switch() == 1:
      led.set_output(0, 1)
      sleep(0.2)

      led.set_output(0, 0)
      sleep(0.2)

    while sw.read_slide_switch() == 0:
      end_time = time.time() + 5
      print("this is end time: ", end_time)

      while time.time() < end_time:
        led.set_output(0, 1)
        sleep(0.1)

        led.set_output(0, 0)
        sleep(0.1)

      while sw.read_slide_switch() == 0:
        led.set_output(0, 0)
        sleep(0.1)
    

if __name__ == "__main__":
    main()