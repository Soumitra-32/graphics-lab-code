clc; clear; close all;
P = [1 3 2 1; 1 1 3 1];
S = [2 0; 0 2];
P_new = S * P;
plot(P(1,:), P(2,:), 'b', 'LineWidth', 2); hold on;
plot(P_new(1,:), P_new(2,:), 'r', 'LineWidth', 2);
legend('Original', 'Scaled');
title('Matrix Scaling');
grid on; axis equal;