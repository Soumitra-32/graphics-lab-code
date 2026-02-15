clc; clear; close all;

x1=2; y1=3;
x2=10; y2=8;

dx = abs(x2-x1);
dy = abs(y2-y1);

p = 2*dy - dx;
x = x1;
y = y1;

while x <= x2
    plot(x,y,'o'); hold on;
    x = x + 1;
    if p < 0
        p = p + 2*dy;
    else
        y = y + 1;
        p = p + 2*(dy-dx);
    end
end

grid on;
title('Bresenham Line Algorithm');
