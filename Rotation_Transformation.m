
% Rotation Transformation
clc; clear; close all;

square = [0 0; 50 0; 50 50; 0 50; 0 0];
theta = 45 * pi/180;

R = [cos(theta) -sin(theta); sin(theta) cos(theta)];
rotated = (R * square')';

plot(square(:,1), square(:,2));
hold on;
plot(rotated(:,1), rotated(:,2));
axis equal; grid on;
title('Rotation Transformation (45 Degrees)');
legend('Original','Rotated');
