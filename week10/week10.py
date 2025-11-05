from gpiozero import LED
#import time
from time import sleep

led = LED(17)  #GPIO PIN #led = LED(11)
# 라즈베리파이 신호등 
try:
    while True:
        led.on()
        #time.sleep(2)  # delay 2sec 2초 대기
        sleep(2)
        # GPIO.output(LED_PIN, GPIO.LOW)
        led.off()
        #time.sleep(2)  # delay 2sec 2초 대기
        sleep(2)
except KeyboardInterrupt:
    print("Exit Program!")
finally:
    #GPIO.cleanup() #initialize gpio setting
    led.close()


