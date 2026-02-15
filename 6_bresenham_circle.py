import matplotlib.pyplot as plt

r = 5
xc, yc = 0, 0

x = 0
y = r
d = 3 - 2*r

x_points = []
y_points = []

while x <= y:
    points = [(x,y),(-x,y),(x,-y),(-x,-y),
              (y,x),(-y,x),(y,-x),(-y,-x)]
    
    for pt in points:
        x_points.append(xc + pt[0])
        y_points.append(yc + pt[1])
    
    if d < 0:
        d = d + 4*x + 6
    else:
        d = d + 4*(x-y) + 10
        y -= 1
    x += 1

plt.plot(x_points, y_points, marker='o', linestyle='None')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.title("Bresenham Circle Algorithm")
plt.show()
