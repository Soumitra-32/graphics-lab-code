clc; clear; close all;

x1=2; y1=3;
x2=10; y2=8;

dx = x2 - x1;
dy = y2 - y1;

steps = max(abs(dx), abs(dy));

x_inc = dx / steps;
y_inc = dy / steps;

x = x1;
y = y1;

for i=1:steps
    plot(round(x), round(y), 'o'); hold on;
    x = x + x_inc;
    y = y + y_inc;
end

grid on;
title('DDA Line Algorithm');
