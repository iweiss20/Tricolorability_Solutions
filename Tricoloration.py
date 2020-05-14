import numpy as np

# Takes the required input, and breaks it into its necessary components
strands = int(input('How many strands do you have?\n'))
strand_code = input('Please input the strand code:\n')
strand_code = strand_code.split(" ")

array = np.zeros((strands, strands))

# Builds up an array representing the appropriate equations
for i in range(strands - 1):
    for j in range(3):
        array[i, int(strand_code[3 * (i) + (j)]) - 1] = 1

# Reduced Row Echelon Form
for i in range(strands):
    if array[i,i] == 0:
        for j in range(i + 1, strands):
            if array[j, i] != 0:
                array[[i, j]] = array[[j, i]]
                break
    if array[i,i] == -1:
        array[i] = array[i] * -1
    for j in range(i + 1, strands):
        if array[j, i] != 0:
            array[j] = array[j] - (array[i] * array[j, i])

# Calculates the Nullity of the matrix by counting the empty rows
nullity = 0
for i in range(strands):
    empty = False
    for j in range(strands):
        if array[i, j] == 0:
            empty = True
        else:
            empty = False
            break
    if empty:
        nullity += 1

# Solution is 3^nullity. If it is not tricolorable, answer will be 3.
print('Solution: {}'.format(3 ** nullity))
