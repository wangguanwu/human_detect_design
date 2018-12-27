import time
import busio
import board
import adafruit_amg88xx
import scipy
import numpy as np
from scipy.interpolate import griddata
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)
frame_x = 8
frame_y = 8
# we need th_bgframes frames  to calculate the average temperature of the bground
th_bgframes = 300
# the counter of the bgframes frames
bgframe_cnt = 0
all_bgframes= []
pre_read_count = 2
# 8X8 grid 
points = [[(math.floor(ix/8),(ix%8)) for ix  in range(0,64)]
grid_x, grid_y = np.mgrid[0:7:32j,0:7:32j]
for i in range(pre_read_count):
    for row in amg.pixels:
        pass

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
        total_frames =  np.zeros((8,8))
        for aitem in  range(len(all_bgframes)):
            total_frames  = total_frames + np.array(all_bgframes[aitem])
        average_temperature = total_frames / th_bgframes
        print(average_temperature)
        # the result of the interpolating for the grid
        inter_result = interpolate(average_temperature , points ,
            grid_x,grid_y,'cubic')
        print("after interpolating"
            )
        print(inter_result)
        break
    
    
#插值(cublic)
def interpolate(pixels , points , grid_x,grid_y , ip_type='cubic'):
    return griddata(points,pixels,(grid_x,grid_y),ip_type)
    
