import itertools


def f1(x, y, z):
    return (x, z + 2, z)


def f2(x, y, z):
    return (y + z * 2, y, z)


def f3(x, y, z):
    return (y - 3, y, z)


def f4(x, y, z):
    return (x, y, x + y)


arr_fun = [f1, f2, f3, f4]


def get_max():
    max = float("-infinity")
    result = []
    for arr in itertools.permutations(arr_fun):
        xyz = (1, 2, 3)
        for fun in arr:
            xyz = fun(*xyz)
        if xyz[0] > max:
            max = xyz[0]
            result = arr
    return max, result


m, vector = get_max()
print m
print vector
