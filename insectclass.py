from math import floor
import random


class insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flightDist = 0
    
    def fly(self):
        self.flightDist = (random.randint(0,10))

    def getflight(self):
        return self.flightDist
