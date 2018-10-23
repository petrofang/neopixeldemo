# g603's CircuitPython NeoPixel Code for Adafruit Hallowing. 2018.
import time
import board
import neopixel
import touchio

# things you might want to adjust:
nap = 0.0667            # time between frames (seconds)
snooze = 1              # time to pause when complete
COLOR1 = (248, 48, 0)   # (orange)
COLOR2 = (0, 48, 0)     # (green)
COLOR3 = (24, 0, 32)    # (purple)

# Create a neopixel array object for Hallowing with 30 neopixels.
pin = board.EXTERNAL_NEOPIXEL
STRIP = neopixel.NeoPixel(pin, 30, brightness=0.15, auto_write=True)

# create touchio objects:
touchA5 = touchio.TouchIn(board.A5)
touchA2 = touchio.TouchIn(board.A2)

# check for touch input
def checkForTouch():
    if touchA2.value:
        if STRIP.brightness < 1:
            STRIP.brightness += 0.05
    elif touchA5.value:
        if STRIP.brightness > 0.05:
            STRIP.brightness += -0.05

# rotate through alternating colors 
while True:
    for x in range(0, 30, 2):
        STRIP[x] = COLOR1
        time.sleep(nap)
        checkForTouch()
    for x in range(1, 31, 2):
        STRIP[x] = COLOR2
        time.sleep(nap)
        checkForTouch()
    time.sleep(snooze)
    
    for x in range(0, 30, 2):
        STRIP[x] = COLOR3
        time.sleep(nap)
        checkForTouch()
    for x in range(1, 31, 2):
        STRIP[x] = COLOR1
        time.sleep(nap)
        checkForTouch()
    time.sleep(snooze)

    for x in range(0, 30, 2):
        STRIP[x] = COLOR2
        time.sleep(nap)
        checkForTouch()
    for x in range(1, 31, 2):
        STRIP[x] = COLOR3
        time.sleep(nap)
        checkForTouch()
    time.sleep(snooze)
    
