
% Translation Transformation
clc; clear; close all;

square = [0 0; 50 0; 50 50; 0 50; 0 0];
tx = 30; ty = 20;

translated = square + [tx ty];

plot(square(:,1), square(:,2));
hold on;
plot(translated(:,1), translated(:,2));
axis equal; grid on;
title('Translation Transformation');
legend('Original','Translated');
