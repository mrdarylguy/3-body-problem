import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter
import os

#temp folder to store plots
def plots(filepath):
  try:
      os.mkdir(filepath)
      print("Directory is created")
  except FileExistsError:
    print("Directory exists")
  pass

class Orbit:
    def __init__(self):
        #Relative Mass
        self.Planet_mass = 1 #Default is one Earth mass
        self.Sun_mass = 333000 

        #Initial Position
        self.Planet_init_pos_x = 1
        self.Planet_init_pos_y = 0
        self.Sun_init_pos_x = 0
        self.Sun_init_pos_y = 0

        #Initial Velocities
        self.Planet_init_vel_x = 0
        self.Planet_init_vel_y = np.sqrt(self.Sun_mass)
        self.Sun_init_vel_x = 0
        self.Sun_init_vel_y = 0

        #time granularity of simulation
        self.time = np.linspace(0,1,10000)

        #solution array

    def dSdt(self, S, t):
        planet_x, planet_y, Sun_x, Sun_y, planet_vx, planet_vy,Sun_vx, Sun_vy = S
        planet_Sun_dist = np.sqrt((Sun_x - planet_x)**2 + (Sun_y - planet_y)**2)

        return [planet_vx, planet_vy,Sun_vx, Sun_vy,
        self.Sun_mass/planet_Sun_dist**3 * (Sun_x - planet_x),
        self.Sun_mass/planet_Sun_dist**3 * (Sun_y - planet_y),
        self.Sun_mass/planet_Sun_dist**3 * (planet_x - Sun_x),
        self.Sun_mass/planet_Sun_dist**3 * (planet_y - Sun_y)]

    def solve_ODE(self):
          sol = odeint(self.dSdt, y0=[self.Planet_init_pos_x, self.Planet_init_pos_y,
          self.Sun_init_pos_x, self.Sun_init_pos_y,
          self.Planet_init_vel_x, self.Planet_init_vel_y,
          self.Sun_init_vel_x, self.Sun_init_vel_y],
          t = self.time)

          return sol

    def plot_trajectory(self):

          plt.plot(self.solve_ODE().T[0])
          plt.xlim(0,200)
          plt.ylabel("Distance of Planets from the Sun (AU)")
          plt.xlabel("Years")
          plt.title("Planetary distance from the Sun against time.")
          plt.grid()
          plt.show()
          # plt.savefig(".......")

if __name__ == '__main__':
      orbit = Orbit()
      orbit.solve_ODE()
      orbit.plot_trajectory()