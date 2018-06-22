def main():
    """

    :return: 0
    """

    strands = int(input("How many strands do you have? "))

    array = build_array(strands)

    nullity(array)

    return 0


def build_array(strands):
    """
    Builds up the array needed to calculate number of colorings of a prime knot
    :param strands: the number of strands a given knot has
    :return: an array with the proper equations to solve the coloring question
    """

    # 1 2 6 6 1 2 5 6 1 3 4 2 4 5 3 5 4 3

    gauss_code = [int(x) for x in input("Please input strand code: ")
        .split()]

    array = []

    for i in range(0, strands):
        array.append([0] * strands)


    for i in range(0, strands):
        if i == 0:
            array[0][0] = 1
            array[0][abs(gauss_code[1]) - 1] = 1
            array[0][abs(gauss_code[2]) - 1] = 1
        else:
            array[i][gauss_code[3 * i] - 1] = 1
            array[i][abs(gauss_code[3 * i + 1]) - 1] = 1
            array[i][abs(gauss_code[3 * i + 2]) - 1] = 1

    print(array)

    return array


def nullity(array):
    """
    Given a square array, this function will calculate the nullity of the array
    :param array: A square array which represents the knot crossings
    :return: the dimensions of the null space for the given array
    """

    return 0


if __name__== '__main__':
    main()