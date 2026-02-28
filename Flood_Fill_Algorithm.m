
% Flood Fill Algorithm (4-connected)
function flood_fill(x,y,old_color,new_color,img)
if img(x,y,:) == old_color
    img(x,y,:) = new_color;
    flood_fill(x+1,y,old_color,new_color,img);
    flood_fill(x-1,y,old_color,new_color,img);
    flood_fill(x,y+1,old_color,new_color,img);
    flood_fill(x,y-1,old_color,new_color,img);
end
end
