def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            print("{}".format(row[i]), end=" " if i < len(row) - 1 else "")
        print()
