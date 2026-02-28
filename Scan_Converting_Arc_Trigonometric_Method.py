
# Scan Converting Arc using Trigonometric Method
import numpy as np
import matplotlib.pyplot as plt

r = 50
theta = np.linspace(0, np.pi/2, 200)
x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y)
plt.gca().set_aspect('equal', 'box')
plt.title("Arc - Trigonometric Method")
plt.grid(True)
plt.show()
