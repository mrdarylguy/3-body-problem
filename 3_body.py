import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter
import os

class Orbit:
    def __init__(self):
          
        #Actual quantities
        self.Earth_actual_mass = 5.97e24
        self.Astronomical_unit = 1.5e11
        self.Universal_grav_constant = 6.67e-11

        #Relative Mass
        self.Planet_mass = 1 #Default is one Earth mass
        self.Sun_mass = 333000 

        #Initial Positions
        self.Planet_init_pos_x = 1 #Default is one Astronomical Unit
        self.Planet_init_pos_y = 0
        self.Sun_init_pos_x = 0
        self.Sun_init_pos_y = 0

        #Variables for position
        self.Planet_pos_x = None
        self.Planet_pos_y = None
        self.Sun_pos_x = None
        self.Sun_pos_y = None

        #Initial Velocities
        self.Planet_init_vel_x = 0
        self.Planet_init_vel_y = np.sqrt(self.Sun_mass)
        self.Sun_init_vel_x = 0
        self.Sun_init_vel_y = 0

        #time granularity of simulation
        self.time = np.linspace(0,1,10000)

    def dSdt(self, S, t):
        planet_x, planet_y, Sun_x, Sun_y, planet_vx, planet_vy,Sun_vx, Sun_vy = S
        planet_Sun_dist = np.sqrt((Sun_x - planet_x)**2 + (Sun_y - planet_y)**2)

        return [planet_vx, planet_vy,Sun_vx, Sun_vy,
        self.Sun_mass/planet_Sun_dist**3 * (Sun_x - planet_x),
        self.Sun_mass/planet_Sun_dist**3 * (Sun_y - planet_y),
        self.Planet_mass/planet_Sun_dist**3 * (planet_x - Sun_x),
        self.Planet_mass/planet_Sun_dist**3 * (planet_y - Sun_y)]

    def solve_ODE(self):
          sol = odeint(self.dSdt, y0=[
                self.Planet_init_pos_x, self.Planet_init_pos_y,
                self.Sun_init_pos_x, self.Sun_init_pos_y,
                self.Planet_init_vel_x, self.Planet_init_vel_y,
                self.Sun_init_vel_x, self.Sun_init_vel_y
                ],
          t = self.time)

          return sol

    def plot_x_pos(self):

          plt.plot(self.solve_ODE().T[0])
          plt.xlim(0, 200)
          plt.ylim(-1.1, 1.1)
          plt.ylabel("X-coordinate of planet", fontsize=12)
          plt.xlabel("Units of time", fontsize=12)
          plt.title("X coordinate against time", fontsize=16)
          plt.axhline(y=1.0, color="red", linestyle='--')
          plt.axhline(y=min(self.solve_ODE().T[0]), color='red', linestyle="--") 
          plt.grid()
          plt.show()
          # plt.savefig(".......")

    def plot_orbit(self):
          
          time = 1/np.sqrt(self.Universal_grav_constant * self.Earth_actual_mass / (self.Astronomical_unit)**3) #obtain number of seconds
          time = time / (60*60*24*365.25) * np.diff(self.time)[0] #convert seconds into years

          #Array of positions
          self.Planet_pos_x = self.solve_ODE().T[0]
          self.Planet_pos_y = self.solve_ODE().T[1]
          self.Sun_pos_x = self.solve_ODE().T[2]
          self.Sun_pos_y = self.solve_ODE().T[3]

          def animate(i):
                ln1.set_data(
                      [self.Planet_pos_x[i], self.Sun_pos_x[i]], 
                      [self.Planet_pos_y[i], self.Sun_pos_y[i]]
                )

                text.set_text('Time = {:.2f} Years'.format(i*time))

          fig, ax = plt.subplots(1, 1, figsize=(8,8))
          ax.grid()
          ln1, = plt.plot([],[], "ro--", lw=3, markersize=8)
          text = plt.text(0.7, 0.7,'')
          ax.set_ylim(-5, 5)
          ax.set_xlim(-5, 5)
          ani = animation.FuncAnimation(fig, animate, frames=200, interval=50)
          ani.save("orbit_trajectory.gif", writer="pillow", fps=30)
          plt.show()
      #     plt.savefig("..........")

    #temp folder to store plots
    def plot_folder(self, filepath):
          try:
                os.mkdir(filepath)
                print("Directory is created")

          except FileExistsError:
                print("Directory exists")
                pass


if __name__ == '__main__':
      orbit = Orbit()
      # orbit.plot_folder("...........")
      orbit.solve_ODE()
      orbit.plot_x_pos()
      # orbit.plot_orbit()
      