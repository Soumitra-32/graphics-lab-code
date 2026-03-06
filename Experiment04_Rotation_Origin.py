import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,3,2,1])
y = np.array([1,1,3,1])
theta = np.radians(45)
x_new = x*np.cos(theta) - y*np.sin(theta)
y_new = x*np.sin(theta) + y*np.cos(theta)
plt.plot(x,y)
plt.plot(x_new,y_new)
plt.title("Rotation about Origin")
plt.gca().set_aspect('equal')
plt.show()