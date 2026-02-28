
# Translation Transformation
import numpy as np
import matplotlib.pyplot as plt

square = np.array([[0,0],[50,0],[50,50],[0,50],[0,0]])
tx, ty = 30, 20

translated = square + np.array([tx, ty])

plt.plot(square[:,0], square[:,1])
plt.plot(translated[:,0], translated[:,1])
plt.gca().set_aspect('equal', 'box')
plt.title("Translation Transformation")
plt.legend(["Original","Translated"])
plt.grid(True)
plt.show()
