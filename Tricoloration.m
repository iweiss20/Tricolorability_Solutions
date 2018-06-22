close all;
clear all;

strands = input('How many strands do you have? ');
% int_strands = str2num(strands);
%Users need to input as a list
gauss_code = input('Please input strand code: ');
% int_gauss_code = str2num(gauss_code);
array = ones(strands, strands);

% print(gauss_code{1, 1});

% print(strands);

%  for i=1:strands
%      array{i, int_gauss_code{3 * i}} = 1;
%      array{i, int_gauss_code{3 * i + 1}} = 1;
%      array{i, int_gauss_code{3 * i + 2}} = 1;
%  end
 
 array(strands, 1:strands) = 0;

 Nullity = length(null(array));

%  print(Nullity);