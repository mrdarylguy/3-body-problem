import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter
import os

#temp folder to store plots
dirName='plots'

try:
    os.mkdir(dirName)
    print("Directory: [",dirName,"] is created")

except FileExistsError:
    print("Directory: [",dirName,"] exists")
    pass


m1 = 1
m2 = 333000
x1_0 = 1
x2_0 = 0
y1_0 = 0
y2_0 = 0
vx1_0 = 0
vy1_0 = np.sqrt(m2)
vx2_0 = 0
vy2_0 = 0

def dSdt(S, t):
    x1, y1, x2, y2, vx1, vy1, vx2, vy2 = S
    r12 = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    return [vx1, vy1, vx2, vy2, 
    m2/r12**3 * (x2-x1),
    m2/r12**3 * (y2-y1),
    m1/r12**3 * (x1-x2),
    m1/r12**3 * (y1-y2)]

t = np.linspace(0,1,10000)

sol = odeint(dSdt, y0=[x1_0, y1_0, x2_0,y2_0, vx1_0, vy1_0, vx2_0, vy2_0],t=t)

plt.plot(sol.T[0])
plt.xlim(0,200)
plt.ylabel("Distance of Earth from the sun (AU)")
plt.xlabel("Years")
plt.title("Earth distance from the Sun against time.")
plt.grid()
# plt.savefig("/Users/daryltng/Documents/GitHub/3-body-problem/plots/Earth_from_sun.png")