#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CSELAB-2
#
# Created:     01/02/2026
# Copyright:   (c) CSELAB-2 2026
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Mandelbrot set parameters
width, height = 800, 800          # Image resolution
x_min, x_max = -2.0, 1.0          # x-axis range
y_min, y_max = -1.5, 1.5          # y-axis range
max_iter = 300                     # Maximum iterations

# -------------------------------
# Create a 2D grid of complex numbers
x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y                     # Complex plane
Z = np.zeros(C.shape, dtype=complex)

# Initialize output image
mandelbrot = np.zeros(C.shape, dtype=int)

# -------------------------------
# Iterate Mandelbrot equation
for i in range(max_iter):
    mask = np.abs(Z) <= 2          # Points that haven't escaped
    Z[mask] = Z[mask]**2 + C[mask]
    mandelbrot[mask] = i

# -------------------------------
# Display the Mandelbrot set
plt.figure(figsize=(8,8))
plt.imshow(mandelbrot, extent=[x_min, x_max, y_min, y_max], cmap='inferno')
plt.title('Mandelbrot Set')
plt.xlabel('Re')
plt.ylabel('Im')
plt.axis('off')
plt.show()

