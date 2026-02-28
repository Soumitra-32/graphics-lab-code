
# Scan Converting Rectangle
import matplotlib.pyplot as plt

x = [0, 100, 100, 0, 0]
y = [0, 0, 50, 50, 0]

plt.plot(x, y)
plt.gca().set_aspect('equal', 'box')
plt.title("Rectangle")
plt.grid(True)
plt.show()
