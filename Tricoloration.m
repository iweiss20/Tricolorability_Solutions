close all;
clear all;

strands = int(input("How many strands do you have? "));

%Users need to input as a list
gauss_code = int(input("Please input strand code: "));

array = [strand][strand];

for i=1:strands
    array[i][gauss_code[3 * i]] = 1;
    array[i][gauss_code[3 * i + 1]] = 1;
    array[i][gauss_code[3 * i + 2]] = 1;
end;

rref_array = rref(array);