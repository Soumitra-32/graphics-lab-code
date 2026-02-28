
# Boundary Fill Algorithm (4-connected)
def boundary_fill(x, y, fill_color, boundary_color, canvas):
    if canvas[x][y] != boundary_color and canvas[x][y] != fill_color:
        canvas[x][y] = fill_color
        boundary_fill(x+1, y, fill_color, boundary_color, canvas)
        boundary_fill(x-1, y, fill_color, boundary_color, canvas)
        boundary_fill(x, y+1, fill_color, boundary_color, canvas)
        boundary_fill(x, y-1, fill_color, boundary_color, canvas)
