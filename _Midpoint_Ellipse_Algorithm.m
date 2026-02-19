
% Midpoint Ellipse Algorithm
a = 5;
b = 3;

x = 0;
y = b;
a2 = a^2;
b2 = b^2;
dx = 2*b2*x;
dy = 2*a2*y;

d1 = b2 - a2*b + 0.25*a2;

hold on;
axis equal;
title('Midpoint Ellipse Algorithm');
xlabel('X-axis');
ylabel('Y-axis');
grid on;

while dx < dy
    plot([x -x x -x], [y y -y -y], 'k.');
    if d1 < 0
        x = x + 1;
        dx = 2*b2*x;
        d1 = d1 + dx + b2;
    else
        x = x + 1;
        y = y - 1;
        dx = 2*b2*x;
        dy = 2*a2*y;
        d1 = d1 + dx - dy + b2;
    end
end

d2 = b2*(x+0.5)^2 + a2*(y-1)^2 - a2*b2;

while y >= 0
    plot([x -x x -x], [y y -y -y], 'k.');
    if d2 > 0
        y = y - 1;
        dy = 2*a2*y;
        d2 = d2 + a2 - dy;
    else
        y = y - 1;
        x = x + 1;
        dx = 2*b2*x;
        dy = 2*a2*y;
        d2 = d2 + dx - dy + a2;
    end
end
