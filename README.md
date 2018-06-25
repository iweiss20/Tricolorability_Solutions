# Tricolorability Solutions
A program that checks the number of ways to tricolor a knot or link with more than two crossings.

Please note: The output will always at least give 3 as an answer. This is because this method of checking for colorings allows for a knot or link to be considered to be tri-colorable by the trivial coloring of one color. So, in order to have the correct solution to your question, you must always subtract 3 from the output.

# How To Use

The program will ask for two prompts, and then it will display the answer.

Prompt 1: "How many strands do you have?" The answer to this question depends on the link or knot. For example, the trefoil knot has three strands and the figure-8 knot has 4 strands, while the whitehead link has 5 strands and the Hopf-link has 2.


Prompt 2: "Please input the strand code:" For more information about strand code, please see the section on strand code. The answer to this question depends on the link or knot, but its output should be relatively the same.

Example: [1 2 3 3 1 2 2 3 1] - Trefoil Knot

Example: [1 2 3 2 6 1 3 4 1 4 5 3 5 2 6 6 4 5] - Stevedore Knot

Example: [1 5 4 4 3 2 2 4 5 5 3 1 3 1 2] - Whitehead Link


# Strand Code

![Stevedore Knot](https://github.com/iweiss20/Tricolorability_Solutions/blob/master/Stevedore%20Knot.png)

Strand code is very similar to gauss code. First, you must arbitrarily label all of the strands from 1 - n, where n is the number of strands. Then, pick a strand. In this example of the Stevedore knot, we will start with strand 1. Looking at where strand 1 is part of an over crossing, we note that it interacts with strands 2 and 3. Thus, we have [1 2 3] as part of our strand code. Then, we move onto strand 2 and see it acts as an over crossing for strands 6 and 1, thus [2 6 1] is part of the strand code as well, all together, the strand code for the Stevedore knot is [1 2 3 2 6 1 3 4 1 4 5 3 5 2 6 6 4 5].

# Example Inputs and Output
## Trefoil Knot
Prompt 1: 3

Prompt 2: [1 2 3 3 1 2 2 3 1]

Output: 9

## Stevedore Knot
Prompt 1: 6

Prompt 2: [1 2 3 2 6 1 3 4 1 4 5 3 5 2 6 6 4 5]

Output: 9


## Whitehead Link
Prompt 1: 5

Prompt 2:[1 5 4 4 3 2 2 4 5 5 3 1 3 1 2]

Output: 3



# Note

The authors believe, but have not confirmed that this program only works for prime links and knots.

# Bibliography  
## Author

Justin Roberts

## Title

Knot Knotes

## University

Edinburgh University

## Date

March 1999
