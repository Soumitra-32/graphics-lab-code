clc;
clear;
close all;


maxIter = 200;   


x = linspace(-2.5, 1, 1000);
y = linspace(-1.5, 1.5, 1000);
[X, Y] = meshgrid(x, y);
C = X + 1i*Y;


Z = zeros(size(C));
M = zeros(size(C));   


for k = 1:maxIter
    Z = Z.^2 + C;
    mask = abs(Z) <= 2;     
    M(mask) = M(mask) + 1;
end


figure;
imagesc(x, y, M);
axis equal tight;
colormap(hot);
colorbar;
title('Mandelbrot Set');
xlabel('Real Axis');
ylabel('Imaginary Axis');
