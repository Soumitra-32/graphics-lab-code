clc; clear; close all;

r = 5;
xc = 0; yc = 0;

theta = 0:0.01:2*pi;

x = xc + r*cos(theta);
y = yc + r*sin(theta);

plot(x, y);
axis equal;
grid on;
title('Circle Using Equation');
