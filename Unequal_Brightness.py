
# Unequal Brightness Demonstration
import numpy as np
import matplotlib.pyplot as plt

img = np.ones((100,100))
img[:,0:50] = 0.3
img[:,50:100] = 0.8

plt.imshow(img, cmap='gray')
plt.title("Unequal Brightness")
plt.show()
