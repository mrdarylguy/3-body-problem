import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.shape_base import _put_along_axis_dispatcher
import pandas as pd
import json

class Halo():
    def __init__(self,
                 number,
                 diameter,
                 width,
                 orbital_period,
                 gravity,
                 min_temp,
                 max_temp,
                 attached_AI):
                 
        self.number = number
        self.diameter = diameter
        self.width = width
        self.orbital_period = orbital_period
        self.gravity = gravity
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.attached_AI = attached_AI

def calculateOrbitalPeriod(halo):

    if halo.orbital_period == None:

        radius = halo.diameter / 2 
        period = np.sqrt(halo.gravity * 9.81 / radius)

        halo.orbital_period = period

    elif halo.orbital_period != None:
        pass

def extractRingData(rings_to_study, ring_data, ring_info):

    for ring in rings_to_study:
        if ring in ring_data:
            halo = Halo(number=ring["number"],
                        diameter=ring["diamter"],
                        width=ring["width"],
                        orbital_period=ring["orbital_period"],
                        gravity=ring["gravity"],
                        min_temp=ring["min_temp"],
                        max_temp=ring["max_temp"],
                        attached_AI=ring["attached_AI"])

            calculateOrbitalPeriod(halo)


            ring_info.append(halo)


    pass
