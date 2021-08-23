import machine
import time

led_extern = machine.Pin(15, machine.Pin.OUT)

while True:
  led_extern.value(1)
  time.sleep(5)
  led_extern.value(0)
  time.sleep(5)
