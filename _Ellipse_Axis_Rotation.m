
% Ellipse Axis Rotation
a = 5;
b = 3;
angle = pi/4; % 45 degrees

theta = linspace(0, 2*pi, 400);
x = a * cos(theta);
y = b * sin(theta);

x_rot = x * cos(angle) - y * sin(angle);
y_rot = x * sin(angle) + y * cos(angle);

plot(x_rot, y_rot, 'g');
axis equal;
title('Ellipse Axis Rotation (45 degrees)');
xlabel('X-axis');
ylabel('Y-axis');
grid on;
