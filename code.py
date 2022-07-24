import time
import board
import neopixel
import touchio

# g603's CircuitPython NeoPixel Code for Adafruit Hallowing. 2022.

# pre-set color shortcuts:
RED = (255, 0, 0)
ORANGE = (255, 64, 0)
YELLOW = (255, 255, 0)
CHARTREUSE = (127, 255, 0)
GREEN = (0, 255, 0)
JADE = (0,255,127)
CYAN = (0, 255, 255)
AZURE = (0, 127, 255)
BLUE = (0, 0, 255)
INDIGO = (63, 0, 255)
VIOLET = (127, 0, 255)
MAGENTA = (255, 0, 255)
ROSE = (255,0,127)
PURPLE = VIOLET
WHITE = (255, 255, 255)
DARK = (6,6,6)


# things you might want to adjust:
COLOR1 = ORANGE
COLOR2 = PURPLE        
COLOR3 = GREEN 
SPEED = 9                       # a number between 1 and 100 works well
nap = 1 / SPEED                   # time between frames (seconds)
snooze = 0                     # time to pause when complete
brightnessIncrement = 0.05    # how much each touch 
         
# Create a neopixel array object for Hallowing with 30 neopixels.
pin = board.EXTERNAL_NEOPIXEL
STRIP = neopixel.NeoPixel(pin, 30, brightness=(0.11), auto_write=True)

# create touchio objects:
touchA5 = touchio.TouchIn(board.A5)
touchA2 = touchio.TouchIn(board.A2)

# check for touch input
def checkForTouch():
    if touchA2.value:
        if STRIP.brightness < (1 - brightnessIncrement):
            STRIP.brightness += brightnessIncrement
            print("%:", end='')
            print(STRIP.brightness * 100)
    elif touchA5.value:
        if STRIP.brightness > brightnessIncrement:
            STRIP.brightness += -(brightnessIncrement)
            print("%:", end='')
            print(STRIP.brightness * 100)

# ############################################################ #            
print("\n\n\nNeopixel Array Animator: python code by Giles\n")
while True:
    print("(R,G,B):")
    
    print(COLOR1)
    for x in range(0, 30, 2):
        STRIP[x] = COLOR1
        time.sleep(nap)
        checkForTouch()
    time.sleep(snooze)
    
    print(COLOR2)
    for x in range(1, 31, 2):
        STRIP[x] = COLOR2
        time.sleep(nap)
        checkForTouch()
    time.sleep(snooze)
    
    print(COLOR3)
    for x in range(0, 30, 2):
        STRIP[x] = COLOR3
        time.sleep(nap)
        checkForTouch()
    time.sleep(snooze)
    
    print(COLOR1)
    for x in range(1, 31, 2):
        STRIP[x] = COLOR1
        time.sleep(nap)
        checkForTouch()
    time.sleep(snooze)

    print(COLOR2)
    for x in range(0, 30, 2):
        STRIP[x] = COLOR2
        time.sleep(nap)
        checkForTouch()
    time.sleep(snooze)
    
    print(COLOR3)
    for x in range(1, 31, 2):
        STRIP[x] = COLOR3
        time.sleep(nap)
        checkForTouch()
    time.sleep(snooze)
