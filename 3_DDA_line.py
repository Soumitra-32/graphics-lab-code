import matplotlib.pyplot as plt

x1, y1 = 2, 3
x2, y2 = 10, 8

dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))

x_inc = dx / steps
y_inc = dy / steps

x = x1
y = y1

x_points = []
y_points = []

for i in range(steps):
    x_points.append(round(x))
    y_points.append(round(y))
    x += x_inc
    y += y_inc

plt.plot(x_points, y_points, marker='o')
plt.grid()
plt.title("DDA Line Algorithm")
plt.show()
