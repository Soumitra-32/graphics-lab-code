import matplotlib.pyplot as plt

r = 5
xc, yc = 0, 0

x = 0
y = r
p = 1 - r

x_points = []
y_points = []

while x <= y:
    points = [(x,y),(-x,y),(x,-y),(-x,-y),
              (y,x),(-y,x),(y,-x),(-y,-x)]
    
    for pt in points:
        x_points.append(xc + pt[0])
        y_points.append(yc + pt[1])
    
    x += 1
    if p < 0:
        p += 2*x + 1
    else:
        y -= 1
        p += 2*(x - y) + 1

plt.plot(x_points, y_points, marker='o', linestyle='None')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.title("Midpoint Circle Algorithm")
plt.show()
