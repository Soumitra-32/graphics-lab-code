
R = 50;
G = 150;
B = 200;


Rn = R / 255;
Gn = G / 255;
Bn = B / 255;


C = 1 - Rn;
M = 1 - Gn;
Y = 1 - Bn;


fprintf('C = %.3f\n', C);
fprintf('M = %.3f\n', M);
fprintf('Y = %.3f\n', Y);


rgb_image = cat(3, Rn, Gn, Bn);   
cmy_image = cat(3, C, M, Y);      


figure;
subplot(1,2,1), imshow(rgb_image), title('RGB Color');
subplot(1,2,2), imshow(cmy_image), title('CMY Color');
