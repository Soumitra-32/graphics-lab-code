


clc;
clear;
close all;


c = -0.7 + 0.27015i;   
maxIter = 200;        


x = linspace(-1.5, 1.5, 1000);
y = linspace(-1.5, 1.5, 1000);
[X, Y] = meshgrid(x, y);
Z = X + 1i*Y;


J = zeros(size(Z));


for k = 1:maxIter
    Z = Z.^2 + c;
    mask = abs(Z) <= 2;   
    J(mask) = J(mask) + 1;
end


figure;
imagesc(x, y, J);
axis equal tight;
colormap(hot);
colorbar;
title('Julia Set');
xlabel('Real Axis');
ylabel('Imaginary Axis');
