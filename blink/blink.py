import gpiozero from LED
import time from sleep

led = LED(26)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)