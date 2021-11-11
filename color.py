#!/usr/bin/env python3

import time
from unicornhatmini import UnicornHATMini

print("""Unicorn HAT Mini: colour.py

Display the selected color on the Unicorn HAT Mini's pixels.

Press Ctrl+C to exit!

""")

unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(1)
while True:
    # set all pixels to red
    unicornhatmini.set_all(255, 0, 0)
    unicornhatmini.show()
    time.sleep(1.0 / 10)
