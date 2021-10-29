"""
This is a script to extract astrophysical data and recommend 
if the particular Halo is habitable.

"""

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
            halo = Halo(number=ring_data[ring]["number"],
                        diameter=ring_data[ring]["diameter"],
                        width=ring_data[ring]["width"],
                        orbital_period=ring_data[ring]["orbital_period"],
                        gravity=ring_data[ring]["gravity"],
                        min_temp=ring_data[ring]["min_temp"],
                        max_temp=ring_data[ring]["max_temp"],
                        attached_AI=ring_data[ring]["attached_AI"])

            calculateOrbitalPeriod(halo)


            ring_info.append(halo)


ring_data = open("ring_data.json")
ring_data = json.load(ring_data)

rings_to_study = ["04"]
ring_info = []

# extractRingData(rings_to_study, ring_data, ring_info)

