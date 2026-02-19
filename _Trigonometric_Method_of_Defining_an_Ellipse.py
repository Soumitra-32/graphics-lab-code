
import numpy as np
import matplotlib.pyplot as plt

a = 5
b = 3

theta = np.linspace(0, 2*np.pi, 400)
x = a * np.cos(theta)
y = b * np.sin(theta)

plt.plot(x, y)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Trigonometric Method of Defining an Ellipse")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
