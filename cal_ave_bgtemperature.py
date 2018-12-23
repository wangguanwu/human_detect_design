import time
from typing import List, Any

import busio
import board
import adafruit_amg88xx
import scipy
import numpy as np

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)
# we need th_bgframes frames  to calculate the average temperature of the bground
th_bgframes = 300
# the counter of the bgframes frames
bgframe_cnt = 0
all_bgframes: List[List[Any]] = []

while True:
    temp = []
    for row in amg.pixels:
        # Pad to 1 decimal place
        temp.append(row)
    bgframe_cnt = bgframe_cnt + 1
    all_bgframes.append(temp)
    if bgframe_cnt >= th_bgframes:
        print('next step')
        print(len(all_bgframes))
        print(all_bgframes)
        break



