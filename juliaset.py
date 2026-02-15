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
# Julia set parameters
width, height = 800, 800          # Image resolution
x_min, x_max = -1.5, 1.5          # x-axis range
y_min, y_max = -1.5, 1.5          # y-axis range
max_iter = 300                     # Maximum iterations
c = complex(-0.7, 0.27015)         # Julia constant

# -------------------------------
# Create a 2D grid of complex numbers
x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Initialize output image
julia = np.zeros(Z.shape, dtype=int)

# -------------------------------
# Iterate the Julia set equation
for i in range(max_iter):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask]**2 + c
    julia[mask] = i

# -------------------------------
# Display the Julia set
plt.figure(figsize=(8,8))
plt.imshow(julia, extent=[x_min, x_max, y_min, y_max], cmap='inferno')
plt.title(f'Julia Set for c = {c}')
plt.xlabel('Re')
plt.ylabel('Im')
plt.axis('off')
plt.show()

