
import matplotlib.pyplot as plt

def midpoint_ellipse(a, b):
    x = 0
    y = b
    a2 = a*a
    b2 = b*b
    dx = 2*b2*x
    dy = 2*a2*y

    d1 = b2 - a2*b + 0.25*a2
    points = []

    while dx < dy:
        points.append((x, y))
        if d1 < 0:
            x += 1
            dx = 2*b2*x
            d1 += dx + b2
        else:
            x += 1
            y -= 1
            dx = 2*b2*x
            dy = 2*a2*y
            d1 += dx - dy + b2

    d2 = b2*(x+0.5)**2 + a2*(y-1)**2 - a2*b2

    while y >= 0:
        points.append((x, y))
        if d2 > 0:
            y -= 1
            dy = 2*a2*y
            d2 += a2 - dy
        else:
            y -= 1
            x += 1
            dx = 2*b2*x
            dy = 2*a2*y
            d2 += dx - dy + a2

    return points

a = 5
b = 3
points = midpoint_ellipse(a, b)

x_vals = []
y_vals = []

for x, y in points:
    x_vals.extend([x, -x, x, -x])
    y_vals.extend([y, y, -y, -y])

plt.scatter(x_vals, y_vals)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Midpoint Ellipse Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
