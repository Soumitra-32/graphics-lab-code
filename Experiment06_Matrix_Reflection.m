clc; clear; close all;
P = [1 3 2 1; 1 1 3 1];
R = [1 0; 0 -1];
P_new = R * P;
plot(P(1,:), P(2,:), 'b', 'LineWidth', 2); hold on;
plot(P_new(1,:), P_new(2,:), 'r', 'LineWidth', 2);
legend('Original', 'Reflected');
title('Matrix Reflection');
grid on; axis equal;