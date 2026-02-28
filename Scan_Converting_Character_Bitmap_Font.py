
# Scan Converting Character - Bitmap Font
import matplotlib.pyplot as plt
import numpy as np

bitmap = np.array([[1,0,1],[1,1,1],[1,0,1]])
plt.imshow(bitmap, cmap='gray')
plt.title("Bitmap Character")
plt.show()
