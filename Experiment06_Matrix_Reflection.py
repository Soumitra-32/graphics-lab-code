import numpy as np
import matplotlib.pyplot as plt
P = np.array([[1,3,2,1],[1,1,3,1]])
R = np.array([[1,0],[0,-1]])
P_new = R @ P
plt.plot(P[0],P[1])
plt.plot(P_new[0],P_new[1])
plt.title("Matrix Reflection")
plt.gca().set_aspect('equal')
plt.show()