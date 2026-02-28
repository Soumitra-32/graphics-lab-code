
# Scan Converting Sector using Trigonometric Method
import numpy as np
import matplotlib.pyplot as plt

r = 50
theta = np.linspace(0, np.pi/3, 200)
x = np.concatenate(([0], r*np.cos(theta), [0]))
y = np.concatenate(([0], r*np.sin(theta), [0]))

plt.fill(x, y)
plt.gca().set_aspect('equal', 'box')
plt.title("Sector - Trigonometric Method")
plt.grid(True)
plt.show()
