import os
import sys
import time

from get_holiday_color import *

COLORS = [RED for _ in range(10)] + [GREEN for _ in range(10)]

def twiddle(secs):
    len_sleep = 0.1
    times = int(secs / len_sleep)
    frames=['|', '/', '-', '\\']
    for i in range(times):
        color_index = i % len(COLORS)
        index = i % len(frames)
        sys.stdout.write(COLORS[color_index])
        sys.stdout.write(frames[index])
        sys.stdout.flush()
        time.sleep(len_sleep)
        sys.stdout.write('\b')
        sys.stdout.write(DEFAULT_COLOR)

if __name__ == "__main__":
    twiddle(3)
