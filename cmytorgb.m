%% CMY to RGB Conversion

% Given CMY values (0-1)
C = 0.70;
M = 0.90;
Y = 0.10;

% CMY to RGB conversion
R = 1 - C;
G = 1 - M;
B = 1 - Y;

% Display numeric results
fprintf('R = %.3f\n', R);
fprintf('G = %.3f\n', G);
fprintf('B = %.3f\n', B);

% Create 1x1 RGB and CMY color blocks for display
cmy_image = cat(3, C, M, Y);   % CMY color
rgb_image = cat(3, R, G, B);   % Converted RGB color

% Display figures
figure;
subplot(1,2,1), imshow(cmy_image), title('CMY Color');
subplot(1,2,2), imshow(rgb_image), title('Converted RGB Color');
