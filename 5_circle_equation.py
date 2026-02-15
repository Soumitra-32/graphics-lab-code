import numpy as np
import matplotlib.pyplot as plt

r = 5
xc, yc = 0, 0

theta = np.linspace(0, 2*np.pi, 1000)
x = xc + r * np.cos(theta)
y = yc + r * np.sin(theta)

plt.plot(x, y)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.title("Circle Using Equation")
plt.show()
