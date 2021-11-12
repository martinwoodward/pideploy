#!/usr/bin/env python3

import time
import sys
from unicornhatmini import UnicornHATMini

print("""color.py #rgb

Display the passed color on the Unicorn HAT Mini's pixels, if no augment passed
display a default color.  Color in #000000 hex RGB format.

Press Ctrl+C to exit!
""")

# set rgb hex to white
rgb = '#ffffff'

if len(sys.argv) > 1:
    color = sys.argv[1]
    if color[0] == '#':
        rgb = color

# Set up UniverHATMini
unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(1)

print("rgb: " + rgb)

# Show color on Unicorn HAT Mini until process is terminated
while True:
    # convert rgb string to decimal values and set pixels to that color
    unicornhatmini.set_all(int(rgb[1:3],16), int(rgb[3:5],16), int(rgb[5:7],16))
    unicornhatmini.show()
    time.sleep(1.0 / 10)
