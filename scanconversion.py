#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      CSELAB-2
#
# Created:     01/02/2026
# Copyright:   (c) CSELAB-2 2026
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# Line endpoints
x1, y1 = 2, 3
x2, y2 = 12, 8

# Calculate slope and intercept
m = (y2 - y1) / (x2 - x1)
c = y1 - m * x1

# Prepare figure
plt.figure(figsize=(6,6))
plt.grid(True)
plt.axis([0, 15, 0, 15])
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Scan Conversion Using Floating Point Method')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Floating point scan conversion
x_pixels = []
y_pixels = []

for x in range(x1, x2 + 1):
    y = m * x + c
    y_round = round(y)
    x_pixels.append(x)
    y_pixels.append(y_round)
    plt.plot(x, y_round, 'ks', markersize=8)  # plot pixel as black square

# Plot ideal line for comparison
plt.plot([x1, x2], [y1, y2], 'r-', linewidth=1.5)

plt.legend(['Scan Converted Pixels', 'Ideal Line'])
plt.show()
