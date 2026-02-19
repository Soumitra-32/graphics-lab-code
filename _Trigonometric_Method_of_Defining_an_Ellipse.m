
% Trigonometric Method of Defining an Ellipse
a = 5;
b = 3;

theta = linspace(0, 2*pi, 400);
x = a * cos(theta);
y = b * sin(theta);

plot(x, y, 'r');
axis equal;
title('Trigonometric Method of Defining an Ellipse');
xlabel('X-axis');
ylabel('Y-axis');
grid on;
