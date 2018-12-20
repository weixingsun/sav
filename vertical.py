#! /usr/bin/python3
from Init       import Init
# --------------------------------------------------
i= Init()
i.arm()
i.reset_channels()
# --------------------------------------------------
try:
    #channels = [1500, 1500, 1500, 1200]
    #print(controller.set_channels(channels))
    #print(controller.get_channels(False, True))
    #print(controller.get_channels(raw=True))
    i.takeoff()
except KeyboardInterrupt:
    exit()
finally:
    i.close()
