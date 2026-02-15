import matplotlib.pyplot as plt

x1, y1 = 2, 3
x2, y2 = 10, 8

dx = abs(x2 - x1)
dy = abs(y2 - y1)

p = 2*dy - dx
x = x1
y = y1

x_points = []
y_points = []

while x <= x2:
    x_points.append(x)
    y_points.append(y)
    x += 1
    if p < 0:
        p += 2*dy
    else:
        y += 1
        p += 2*(dy - dx)

plt.plot(x_points, y_points, marker='o')
plt.grid()
plt.title("Bresenham Line Algorithm")
plt.show()
