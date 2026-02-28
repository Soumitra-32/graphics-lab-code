
# Scan Converting Character - Outline Font
import matplotlib.pyplot as plt

x = [0,1,1,0,0]
y = [0,0,2,2,0]

plt.plot(x,y)
plt.gca().set_aspect('equal', 'box')
plt.title("Outline Character")
plt.grid(True)
plt.show()
