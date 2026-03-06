import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,3,2,1])
y = np.array([1,1,3,1])
tx, ty = 3, 2
x_new = x + tx
y_new = y + ty
plt.plot(x,y)
plt.plot(x_new,y_new)
plt.title("Translation")
plt.gca().set_aspect('equal')
plt.show()