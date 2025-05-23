import socket
import time
from time import sleep
from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_dc_motor as dc_motor
from hal import hal_buzzer as buzzer
from hal import hal_servo as servo
import version as ver

import PiDemo as demo

import hal.hal_input_switch as switch
import hal.hal_led as led

def ledTest():

    if (switch.read_slide_switch() == 1):
        demo.blink_led_once(1/5)
    else:
        for x in range(0, 25):
            demo.blink_led_once(1/10)
            if (switch.read_slide_switch() == 1):
                break
        while (switch.read_slide_switch() == 0):
            led.set_output(0, 0)

def main():
    led.init()
    switch.init()
    while True:
        ledTest()

# Main entry point
if __name__ == "__main__":

    main()
