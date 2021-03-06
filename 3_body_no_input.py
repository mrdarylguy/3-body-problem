import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter as pillow
import os

class Orbit:
    def __init__(self):
          
        #Actual quantities
        self.Sun_actual_mass = 1.99e30
        self.Earth_actual_mass = 5.97e24
        self.Mars_actual_mass = 6.39e23
        self.Astronomical_unit = 1.5e11
        self.Universal_grav_constant = 6.67e-11

        #Relative quantities
        self.Earth_mass = 1 #Default is one Earth mass
        self.Sun_mass = self.Sun_actual_mass / self.Earth_actual_mass # mass = 333000
        self.Mars_mass = self.Mars_actual_mass / self.Earth_actual_mass 

        self.Earth_dist_from_sun = 1 
        self.Mars_dist_from_sun = 1.5

        #Initial Positions
        self.Earth_init_pos_x = 1 
        self.Earth_init_pos_y = 0
        self.Sun_init_pos_x = 0
        self.Sun_init_pos_y = 0
        self.Mars_init_pos_x = 1.5
        self.Mars_init_pos_y = 0

        #Variables for position
        self.Earth_pos_x = None
        self.Earth_pos_y = None
        self.Sun_pos_x = None
        self.Sun_pos_y = None
        self.Mars_pos_x = None
        self.Mars_pos_y = None

        #Initial Velocities
        self.Earth_init_vel_x = 0
        self.Earth_init_vel_y = np.sqrt(self.Sun_mass/self.Earth_dist_from_sun)
        self.Sun_init_vel_x = 0
        self.Sun_init_vel_y = 0
        self.Mars_init_vel_x = 0
        self.Mars_init_vel_y = np.sqrt(self.Sun_mass/self.Mars_dist_from_sun)

        #time granularity of simulation
        self.time = np.linspace(0, 20, 10000)


    def dSdt(self, t, S):
        x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3 = S

        r12 = np.sqrt((x2-x1)**2 + (y2-y1)**2)
        r13 = np.sqrt((x3-x1)**2 + (y3-y1)**2)
        r23 = np.sqrt((x2-x3)**2 + (y2-y3)**2)

        return [ vx1, vy1, vx2, vy2, vx3, vy3,
            self.Sun_mass/r12**3 * (x2-x1) + self.Mars_mass/r13**3 * (x3-x1), #mass 1
            self.Sun_mass/r12**3 * (y2-y1) + self.Mars_mass/r13**3 * (y3-y1),
            self.Earth_mass/r12**3 * (x1-x2) + self.Mars_mass/r23**3 * (x3-x2), #mass 2
            self.Earth_mass/r12**3 * (y1-y2) + self.Mars_mass/r23**3 * (y3-y2),
            self.Earth_mass/r13**3 * (x1-x3) + self.Sun_mass/r23**3 * (x2-x3), #mass 3
            self.Earth_mass/r13**3 * (y1-y3) + self.Sun_mass/r23**3 * (y2-y3)
           ]
    
    def solve_ODE(self):
        sol = solve_ivp(self.dSdt, (0,20), y0=[
                self.Earth_init_pos_x, self.Earth_init_pos_y,
                self.Sun_init_pos_x, self.Sun_init_pos_y,
                self.Mars_init_pos_x, self.Mars_init_pos_y,
                self.Earth_init_vel_x, self.Earth_init_vel_y,
                self.Sun_init_vel_x, self.Sun_init_vel_y,
                self.Mars_init_vel_x, self.Mars_init_vel_y
                ],
                method = 'RK23', t_eval=self.time)

        return sol

    def plot_x_pos(self):

          plt.plot(self.solve_ODE().T[0])
          plt.xlim(0, 800)
          plt.ylim(-1.1, 1.1)
          plt.ylabel("X-coordinate of planet", fontsize=12)
          plt.xlabel("Units of time", fontsize=12)
          plt.title("X coordinate against time", fontsize=16)
          plt.grid()
          plt.show()
          # plt.savefig(".......")

    def plot_orbit(self):
          
          time = 1/np.sqrt(self.Universal_grav_constant * self.Mars_actual_mass / (self.Astronomical_unit)**3) #obtain number of seconds
          time = time / (60*60*24*365.25) * np.diff(self.time)[0] #convert seconds into years

          #Array of positions
          self.time = self.solve_ODE().t
          self.Earth_pos_x = self.solve_ODE().y[0]
          self.Earth_pos_y = self.solve_ODE().y[1]
          self.Sun_pos_x = self.solve_ODE().y[2]
          self.Sun_pos_y = self.solve_ODE().y[3]
          self.Mars_pos_x = self.solve_ODE().y[4]
          self.Mars_pos_y = self.solve_ODE().y[5]

          def animate(i):
                ln1.set_data(
                      [self.Earth_pos_x[i], self.Sun_pos_x[i], self.Mars_pos_x[i]],
                      [self.Earth_pos_y[i], self.Sun_pos_y[i], self.Mars_pos_y[i]]
                      )

                text.set_text('Time = {:.1f} Years'.format(i*time))

          fig, ax = plt.subplots(1, 1, figsize=(8,8))
          ax.grid()
          ln1, = plt.plot([],[], "ro--", lw=3, markersize=6)
          text = plt.text(0.7, 0.7, 'asdasd', fontsize=16, ha='center')
          ax.set_ylim(-2, 2)
          ax.set_xlim(-2, 2)
          ani = animation.FuncAnimation(fig, animate, frames=1000, interval=50)
          ani.save("Earth_mars_trajectory.gif", writer=pillow(fps=20))
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
      orbit.plot_orbit()
