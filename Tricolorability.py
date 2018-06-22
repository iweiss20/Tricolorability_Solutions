def main():
    """

    :return: 0
    """

    strands = int(input("How many strands do you have? "))

    array = build_array(strands)

    return 0


def build_array(strands):
    """

    :param strands:
    :return:
    """

    # gauss_code = list(input("Please input  extended gauss code: "))
    gauss_code = [int(x) for x in input("Please input strand code: ")
        .split()]
    print(gauss_code)
    array = [strands]
    array.append([strands])

    for i in range(0, strands):
        if i == 0:
            j = abs(gauss_code[i+1])
            k = abs(gauss_code[i+2])
            array[i][i] = 1
            array[i][j - 1] = 1
            array[i][k - 1] = 1
        else:
            j = abs(gauss_code[3 * i + 1])
            k = abs(gauss_code[3 * i + 2])
            array[i][i] = 1
            array[i][j - 1] = 1
            array[i][k - 1] = 1


    return array


if __name__== '__main__':
    main()