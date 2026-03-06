import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,3,2,1])
y = np.array([1,1,3,1])
sx, sy = 2, 2
x_new = sx*x
y_new = sy*y
plt.plot(x,y)
plt.plot(x_new,y_new)
plt.title("Scaling with Respect to Origin")
plt.gca().set_aspect('equal')
plt.show()