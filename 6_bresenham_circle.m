clc; clear; close all;

r = 5;
xc = 0; yc = 0;

x = 0;
y = r;
d = 3 - 2*r;

while x <= y
    plot(xc+x, yc+y,'o'); hold on;
    plot(xc-x, yc+y,'o');
    plot(xc+x, yc-y,'o');
    plot(xc-x, yc-y,'o');
    plot(xc+y, yc+x,'o');
    plot(xc-y, yc+x,'o');
    plot(xc+y, yc-x,'o');
    plot(xc-y, yc-x,'o');
    
    if d < 0
        d = d + 4*x + 6;
    else
        d = d + 4*(x-y) + 10;
        y = y - 1;
    end
    x = x + 1;
end

axis equal; grid on;
title('Bresenham Circle Algorithm');
