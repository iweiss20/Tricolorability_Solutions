def main():
    """

    :return: 0
    """

    arcs = int(input("How many arcs do you have? "))

    array = build_array(arcs)

    return 0


def build_array(arcs):
    """

    :param arcs:
    :return:
    """

    # gauss_code = list(input("Please input  extended gauss code: "))
    gauss_code = [int(x) for x in input("Please input  extended gauss code: ")
        .split()]
    print(gauss_code)
    array = []
    array.append([])

    if gauss_code[0] < 0:
        gauss_code.append(gauss_code[0])

    # for i in range(arcs):

    return array

if __name__== '__main__':
    main()