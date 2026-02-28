
% Unequal Brightness Demonstration
clc; clear; close all;

img = ones(100,100);
img(:,1:50) = 0.3;   % Dark region
img(:,51:100) = 0.8; % Bright region

imshow(img);
title('Unequal Brightness');
