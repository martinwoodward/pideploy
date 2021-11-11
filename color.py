#!/usr/bin/env python3

import time
from unicornhatmini import UnicornHATMini

unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(1)
while True:
    # set all pixels to green
    unicornhatmini.set_all(0, 255, 0)
    unicornhatmini.show()
    time.sleep(1.0 / 10)
