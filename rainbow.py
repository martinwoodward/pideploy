#!/usr/bin/env python3

import time
from colorsys import hsv_to_rgb
from unicornhatmini import UnicornHATMini

unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(1)

# Repeat twice
for i in range(0, 2):        
    # Loop through all hues and set all pixels to rgb values
    for hue in range(1, 100):
        r, g, b = [int(c * 255) for c in hsv_to_rgb(hue/100, 1.0, 1.0)]
        unicornhatmini.set_all(r, g, b)
        unicornhatmini.show()
        time.sleep(0.01)
