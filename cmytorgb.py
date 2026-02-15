#-------------------------------------------------------------------------------
# Name:        module2
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
# Given CMY values (0-1)
C = 0.8
M = 0.4
Y = 0.2

# CMY to RGB conversion
R = 1 - C
G = 1 - M
B = 1 - Y

# Display numeric results
print(f"R = {R:.3f}")
print(f"G = {G:.3f}")
print(f"B = {B:.3f}")

# -------------------------------
# Display CMY and RGB as color blocks
cmy_color = np.array([[[C, M, Y]]])
rgb_color = np.array([[[R, G, B]]])

plt.figure(figsize=(4,2))

plt.subplot(1,2,1)
plt.imshow(cmy_color)
plt.title('CMY Color')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(rgb_color)
plt.title('Converted RGB Color')
plt.axis('off')

plt.show()
