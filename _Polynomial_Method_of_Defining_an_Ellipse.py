
import numpy as np
import matplotlib.pyplot as plt

# Ellipse parameters
a = 5   # Semi-major axis
b = 3   # Semi-minor axis

x = np.linspace(-a, a, 400)
y_upper = b * np.sqrt(1 - (x**2 / a**2))
y_lower = -b * np.sqrt(1 - (x**2 / a**2))

plt.plot(x, y_upper)
plt.plot(x, y_lower)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Polynomial Method of Defining an Ellipse")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
