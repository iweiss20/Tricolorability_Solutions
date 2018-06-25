% Set MatLab's defaults to empty
close all;
clear all;

% Asks the user for the number of strands in a link or knot
strands = input('How many strands do you have? ');

% Users need to input as a list
strand_code = input('Please input strand code: ');

% Builds an empty array of size Strand x Strand
array = zeros(strands, strands);

% Examines the inputted strand code and fills the array with
% the appropriate 1's in order to satisfy the necessary equations
 for i=1:strands-1
     if i == 1
         array(i, strand_code(1, 1)) = 1;
         array(i, strand_code(1, 2)) = 1;
         array(i, strand_code(1, 3)) = 1;
     else
         array(i, strand_code(1, 3 * i + 1)) = 1;
         array(i, strand_code(1, 3 * i + 2)) = 1;
         array(i, strand_code(1, 3 * i + 3)) = 1;
     end
 end
 
% Sets the last row of the array to zero
array(strands, 1:strands) = 0;

% Takes the Reduced Row Echelon Form of the array
array = rref(array);
Nullity = 0;

% Finds the nullity of the matrix by counting the number of empty rows
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
         Nullity = Nullity + 1;
     end
 end
 
% The solution to 3-colorability is 3 ^ nullity
Solution = 3 ^ Nullity;
 
% Prints out the solution
disp(Solution);
