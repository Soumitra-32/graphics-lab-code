
import numpy as np
import matplotlib.pyplot as plt

a = 5
b = 3
angle = np.pi / 4  # 45 degrees

theta = np.linspace(0, 2*np.pi, 400)
x = a * np.cos(theta)
y = b * np.sin(theta)

x_rot = x * np.cos(angle) - y * np.sin(angle)
y_rot = x * np.sin(angle) + y * np.cos(angle)

plt.plot(x_rot, y_rot)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Ellipse Axis Rotation (45 degrees)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
