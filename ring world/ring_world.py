"""
This is a script to extract astrophysical data and recommend 
if the particular Halo is habitable.

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ring_data

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
        period = np.sqrt(self.gravity / radius)
        return period

    def extractRingData(self, rings_to_study):
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


rings_to_study = [] 
ring_info = []
    
