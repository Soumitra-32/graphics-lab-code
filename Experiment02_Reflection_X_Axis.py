import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,3,2,1])
y = np.array([1,1,3,1])
x_new = x
y_new = -y
plt.plot(x,y)
plt.plot(x_new,y_new)
plt.title("Reflection about X-axis")
plt.gca().set_aspect('equal')
plt.show()