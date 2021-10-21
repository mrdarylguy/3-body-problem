import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
import os

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
        self.diamter = diameter
        self.width = width 
        self.orbital_period = orbital_period
        self.gravity = gravity
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.attached_AI = attached_AI
