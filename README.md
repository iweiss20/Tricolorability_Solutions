# Tricolorability Solutions
A program that checks the number of ways to tricolor a knot or link with more than two crossings

# How To Use

The program will ask for two prompts, and then it will display the answer.

Prompt 1: "How many strands do you have?" The answer to this question depends on the link or knot. but, for example, the trefoil knot has three strands and the figure-8 knot has 4 strands, while the whitehead link has 5 strands and the Hopf-link has 2.


Prompt 2: "Please input the strand code:" For more information about strand code, please see the section on strand code. The answer to this question depends on the link or knot, but its output should be relatively the same.

Example: [1 2 3 3 1 2 2 3 1] - Trefoil Knot
Example: [1 2 6 6 1 2 5 6 1 3 4 2 4 5 3 5 4 3] - Square Knot
Example: [1 5 4 4 3 2 2 4 5 5 3 1 3 1 2] - Whitehead Link


# Strand Code


# Example Inputs and Output
## Trefoil Knot
Prompt 1: 3
Prompt 2: [1 2 3 3 1 2 2 3 1] 
Output: 9

## Square Knot
Prompt 1: 6
Prompt 2: [1 2 6 6 2 1 5 6 1 3 4 2 4 5 3 5 4 3]
Output: 27