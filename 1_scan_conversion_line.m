clc; clear; close all;

x1 = 2; y1 = 3;
x2 = 10; y2 = 8;

m = (y2 - y1) / (x2 - x1);

x = x1:x2;
y = y1 + m * (x - x1);

plot(round(x), round(y), 'o');
grid on;
title('Scan Conversion of Line');
