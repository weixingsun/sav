#! /usr/bin/python3
# -------------------------------------------------------------------------
from serial     import *
from time       import time, sleep
from os         import system
from WiiProxy      import MultiWii
# -------------------------------------------------------------------------
class Init(object):
    # ---------------------------------------------------------------------
    s = None
    c = None
    WRITE_DELAY  = 0.05
    TAKEOFF_TIME = 10   # in seconds
    default_channels = [1500, 1500, 1500, 1000]
    # ---------------------------------------------------------------------

    def __init__(self):
        self.s = Serial()
        self.s.port             = "/dev/ttyACM0"
        self.s.baudrate         = 115200
        self.s.bytesize         = EIGHTBITS
        self.s.parity           = PARITY_NONE
        self.s.stopbits         = STOPBITS_ONE
        self.s.write_timeout    = 3
        self.s.xonxoff          = False
        self.s.rtscts           = False
        self.s.dsrdtr           = False
        
        try:
            self.s.open()
        except SerialException:
            print("init serial port error")
            exit()
        self.c= MultiWii(self.s)
        if not self.c: exit()
        #sleep(MultiWii.INIT_TIMEOUT)

    # ---------------------------------------------------------------------

    #system("clear")
    #controller= i.getMW()

    #def getMW(self):
    #    return self.c

    def arm(self):
        self.c.arm()

    def disarm(self):
        self.c.disarm()

    def close(self):
        self.disarm()
        self.s.close()
        self.s = None

    def get_channels(self):
        return self.c.get_channels(raw=True)

    def set_channels(self,channels):
        self.c.set_channels(channels)

    def reset_channels(self):
        self.set_channels(self.default_channels)
    # ---------------------------------------------------------------------
    def takeoff(self):
        init_time = time()
        time_last = 0
        while time_last < self.TAKEOFF_TIME:
            #print("in takeoff loop, ts=" + str(time_last) +" round="+str(round(time_last)))
            channels = [1500, 1500, 1500, 1000+5*round(time_last)]
            self.set_channels(channels)
            #print(controller.get_channels(False, True))
            print(self.get_channels())
            sleep(0.5)
            time_last = time()-init_time
