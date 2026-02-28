
# Rotation Transformation
import numpy as np
import matplotlib.pyplot as plt

square = np.array([[0,0],[50,0],[50,50],[0,50],[0,0]])
theta = np.deg2rad(45)

R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])

rotated = square.dot(R.T)

plt.plot(square[:,0], square[:,1])
plt.plot(rotated[:,0], rotated[:,1])
plt.gca().set_aspect('equal', 'box')
plt.title("Rotation Transformation (45 Degrees)")
plt.legend(["Original","Rotated"])
plt.grid(True)
plt.show()
