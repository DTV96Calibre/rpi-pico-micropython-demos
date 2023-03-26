""" This code is untested
"""
from machine import Pin, Timer

lamp = Pin(20, Pin.OUT)
led = Pin("LED", Pin.OUT)
led_timer = Timer()

def untouchPin(pin):
    pin.init(mode=Pin.IN, value=None)
def touchPin(pin):
    pin.init(mode=Pin.OUT, value=0)
    
def tick(led_timer):
    global led
    global lamp
    led.toggle()
    if (led.value()):
        touchPin(lamp)
    else:
        untouchPin(lamp)

led_timer.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)


    