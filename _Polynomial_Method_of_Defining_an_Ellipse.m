
% Polynomial Method of Defining an Ellipse
a = 5;  % Semi-major axis
b = 3;  % Semi-minor axis

x = linspace(-a, a, 400);
y_upper = b * sqrt(1 - (x.^2 / a^2));
y_lower = -b * sqrt(1 - (x.^2 / a^2));

plot(x, y_upper, 'b', x, y_lower, 'b');
axis equal;
title('Polynomial Method of Defining an Ellipse');
xlabel('X-axis');
ylabel('Y-axis');
grid on;
