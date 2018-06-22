close all;
clear all;

strands = 4; %= input('How many strands do you have? ');
% int_strands = str2num(strands);
%Users need to input as a list
% gauss_code = input('Please input strand code: ');
% gauss_code = [1 2 6 6 2 1 5 6 1 3 4 2 4 5 3 5 4 3];
gauss_code = [1 3 2 3 1 4 4 1 2 2 3 4];
% int_gauss_code = str2num(gauss_code);
array = zeros(strands, strands);

% print(gauss_code(1, 1));

% print(strands);

 for i=1:strands-1
     if i == 1
         array(i, gauss_code(1, 1)) = 1;
         array(i, gauss_code(1, 2)) = 1;
         array(i, gauss_code(1, 3)) = 1;
     else
         array(i, gauss_code(1, 3 * i + 1)) = 1;
         array(i, gauss_code(1, 3 * i + 2)) = 1;
         array(i, gauss_code(1, 3 * i + 3)) = 1;
     end
 end
 
%  array(strands, 1:strands) = 0;
array = rref(array);
 counter = 0;
 for i=1:strands
     check = true;
     for j = 1:strands
         if array(i,j)==0
             check = true;
         else
             check = false;
             break
         end
     end
     
     if check == true
         counter = counter + 1;
     end
 end
 
 Nullity = 3 ^ counter;
 

 disp(Nullity);