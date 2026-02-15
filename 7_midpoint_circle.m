clc; clear; close all;

r = 5;
xc = 0; yc = 0;

x = 0;
y = r;
p = 1 - r;

while x <= y
    plot(xc+x, yc+y,'o'); hold on;
    plot(xc-x, yc+y,'o');
    plot(xc+x, yc-y,'o');
    plot(xc-x, yc-y,'o');
    plot(xc+y, yc+x,'o');
    plot(xc-y, yc+x,'o');
    plot(xc+y, yc-x,'o');
    plot(xc-y, yc-x,'o');
    
    x = x + 1;
    if p < 0
        p = p + 2*x + 1;
    else
        y = y - 1;
        p = p + 2*(x - y) + 1;
    end
end

axis equal; grid on;
title('Midpoint Circle Algorithm');
