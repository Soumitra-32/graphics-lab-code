
# Scan Line Polygon Fill Algorithm
import matplotlib.pyplot as plt

x = [10, 60, 80, 30]
y = [10, 20, 70, 60]

plt.fill(x, y)
plt.gca().set_aspect('equal', 'box')
plt.title("Scan Line Polygon Fill")
plt.grid(True)
plt.show()
