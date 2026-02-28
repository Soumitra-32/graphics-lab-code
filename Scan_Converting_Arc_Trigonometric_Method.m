
% Scan Converting Arc using Trigonometric Method
clc; clear; close all;
r = 50; xc = 0; yc = 0;
theta = linspace(0, pi/2, 200);
x = xc + r*cos(theta);
y = yc + r*sin(theta);
plot(x,y); axis equal; grid on;
title('Arc - Trigonometric Method');
