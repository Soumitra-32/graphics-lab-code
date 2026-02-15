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
# Given RGB values (0-255)
R = 50
G = 150
B = 200

# Normalize RGB to 0-1
Rn = R / 255
Gn = G / 255
Bn = B / 255

# RGB to CMY conversion
C = 1 - Rn
M = 1 - Gn
Y = 1 - Bn

# Display numeric results
print(f"C = {C:.3f}")
print(f"M = {M:.3f}")
print(f"Y = {Y:.3f}")

# -------------------------------
# Display RGB and CMY as color blocks
rgb_color = np.array([[[Rn, Gn, Bn]]])
cmy_color = np.array([[[C, M, Y]]])

plt.figure(figsize=(4,2))

plt.subplot(1,2,1)
plt.imshow(rgb_color)
plt.title('RGB Color')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(cmy_color)
plt.title('CMY Color')
plt.axis('off')

plt.show()
