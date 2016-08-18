def find_zeros_array(array):

    if len(array) == 0 or array[0] == 1:
        return 0
    first = 0
    last = len(array)
    while last - first != 1:
        guess = (last + first) / 2
        if array[guess] == 0 and (len(array) == guess + 1 or array[guess + 1]) == 1:
            return guess + 1
        elif array[guess] == 1 and array[guess - 1] == 0:
            return guess
        elif array[guess] == 0 and array[guess + 1] == 0:
            first = guess + 1
        else:
            last = guess


def get_zeros(matrix):
    result = 0
    for i in matrix:
        result += find_zeros_array(i)
    return result


def find_one_diagonal(martix):
    d_size = min(len(matrix), len(matrix[0]))

    return find_zeros_array([matrix[i][i] for i in range(d_size)])

if __name__ == "__main__":
    matrix = [
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0]
    ]

    matrix2 = [
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ]

# print find_one_diagonal(matrix)


vector = [[0]]

print find_one_diagonal(vector)