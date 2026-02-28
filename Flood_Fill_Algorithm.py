
# Flood Fill Algorithm (4-connected)
def flood_fill(x, y, old_color, new_color, canvas):
    if canvas[x][y] == old_color:
        canvas[x][y] = new_color
        flood_fill(x+1, y, old_color, new_color, canvas)
        flood_fill(x-1, y, old_color, new_color, canvas)
        flood_fill(x, y+1, old_color, new_color, canvas)
        flood_fill(x, y-1, old_color, new_color, canvas)
