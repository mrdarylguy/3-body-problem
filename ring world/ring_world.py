"""
This is a script to extract astrophysical data and recommend 
if the particular Halo is habitable.

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json


class Halo:
    def __init__(self,
                number, 
                diameter,
                width,
                orbital_period,
                gravity,
                min_temp,
                max_temp,
                attached_AI
                ):

        self.number = number
        self.diameter = diameter
        self.width = width
        self.orbital_period = orbital_period
        self.gravity = gravity
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.attached_AI = attached_AI
    
    #Function to calculate the orbital period 
    def calculateOrbitalPeriod(self):
        radius = self.diameter / 2
        period = np.sqrt(self.gravity * 9.81 / radius)
        return period

    def extractRingData(self, rings_to_study=type(list), ring_info=type(list)):

        ring_data = open("ring_data.json")
        ring_data = json.load(ring_data)


        for ring in rings_to_study:
            if ring in ring_data:
                halo = Halo(number=ring["number"], 
                            diameter=ring["diameter"],
                            width=ring["width"],
                            orbital_period=ring["orbital_period"],
                            gravity=ring["gravity"],
                            min_temp=ring["ring_temp"],
                            max_temp=ring["max_temp"],
                            attached_AI=ring["attached_AI"])

                #Calcultate the orbital period if it is not given
                if halo.orbital_period == None:
                    halo.orbital_period == self.calculateOrbitalPeriod

            ring_info.append(halo)

    def habitability(self, ring_info):
        for halo in ring_info:
            if halo.min_temp > -20 and halo.max_temp < 45:
                if halo.gravity > 0.8:
                    halo.habitability = "Habitable"
                    
            else:
                halo.habitability = "Uninhabitable"

        pass

if __name__ == "__main__":

    rings_to_study = ["04"]
    ring_info = []
 
    _Halo = Halo()
    _Halo.extractRingData(rings_to_study,
                          ring_info)

    print(ring_info)

