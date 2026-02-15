clc;
clear;
close all;


x1 = 2;  y1 = 3
x2 = 12; y2 = 8;
m = (y2 - y1) / (x2 - x1);
c = y1 - m * x1;


figure;
hold on;
grid on;
axis([0 15 0 15]);
axis square;
title('Scan Conversion Using Floating Point Method');
xlabel('X-axis');
ylabel('Y-axis');


for x = x1:x2
    y = m * x + c;          
    plot(x, round(y), 'ks', 'MarkerSize', 8, 'MarkerFaceColor', 'k');
end


plot([x1 x2], [y1 y2], 'r-', 'LineWidth', 1.5);

legend('Scan Converted Pixels', 'Ideal Line');
