
% Scan Converting Sector using Trigonometric Method
clc; clear; close all;
r = 50; theta = linspace(0, pi/3, 200);
x = [0 r*cos(theta) 0];
y = [0 r*sin(theta) 0];
fill(x,y,'c'); axis equal; grid on;
title('Sector - Trigonometric Method');
