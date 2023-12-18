import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.subplot()

theta = np.linspace(0, 20*np.pi, 1000)

R = 0.9
r = 0.3

x = (R-r)*np.cos(theta) + r*np.cos(((R-r)/r)*theta)
y = (R-r)*np.sin(theta) - r*np.sin(((R-r)/r)*theta)

beta = np.linspace(0, 10*np.pi, 1000)
circle1_x = R*np.cos(beta)
circle1_y = R*np.sin(beta)
ax.plot(circle1_x, circle1_y, 'green', lw=1)
ax.set_title("Hipocykloida", fontsize=20)
ax.set_aspect('equal')
circle2_x = r*np.cos(beta)
circle2_y = r*np.sin(beta)

dx = (R-r)*np.cos(theta)
dy = (R-r)*np.sin(theta)

hypocycloids = []
circles = []
points = []

def anim(*args):
    i= args[0]
    if len(circles) > 0:
        circles.pop().remove()
        hypocycloids.pop().remove() 
        points.pop().remove()

    circle, = ax.plot(dx[i]+circle2_x, dy[i]+circle2_y, 'black', lw=1)
    hypocycloid, = ax.plot(x[:i+1], y[:i+1], lw=1, color='red')
    point, = ax.plot(x[i], y[i], markersize=5, marker='o', color='black')

    circles.append(circle)
    hypocycloids.append(hypocycloid)
    points.append(point)
    return fig,

animation = FuncAnimation(fig, anim, frames=4500, interval=100, blit=False, repeat_delay=100000000000)

plt.show()