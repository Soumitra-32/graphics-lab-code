import matplotlib.pyplot as plt

x1, y1 = 2, 3
x2, y2 = 10, 8

m = (y2 - y1) / (x2 - x1)
c = y1 - m * x1

x_points = []
y_points = []

for x in range(x1, x2 + 1):
    y = m * x + c
    x_points.append(x)
    y_points.append(round(y))

plt.plot(x_points, y_points, marker='o')
plt.grid()
plt.title("Direct Line Equation")
plt.show()
