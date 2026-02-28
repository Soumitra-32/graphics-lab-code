
% Boundary Fill Algorithm (4-connected)
function boundary_fill(x,y,fill_color,boundary_color,img)
if img(x,y,:) ~= boundary_color && img(x,y,:) ~= fill_color
    img(x,y,:) = fill_color;
    boundary_fill(x+1,y,fill_color,boundary_color,img);
    boundary_fill(x-1,y,fill_color,boundary_color,img);
    boundary_fill(x,y+1,fill_color,boundary_color,img);
    boundary_fill(x,y-1,fill_color,boundary_color,img);
end
end
