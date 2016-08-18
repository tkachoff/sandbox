# class Item(object):
#     def __init__(self, val, list_i):
#         self.val = val
#         self.list_i = list_i
#
#
# class RangeFinder(object):


matrix = [
    [4, 10, 15, 24, 26],
    [0, 9, 12, 20],
    [5, 18, 22, 30]
]


def get_list_tuples(matrix):
    result = []
    for i in range(len(matrix)):
        # print map(lambda x: (x, i), matrix[i])
        result += map(lambda x: (x, i), matrix[i])
    return sorted(result, key=lambda x: x[0])


# print get_list_tuples(matrix)

def get_range(matrix):
    lt = []
    for i in range(len(matrix)):
        lt += map(lambda x: (x, i), matrix[i])
    lt = sorted(lt, key=lambda x: x[0])
    set_size = len(matrix)
    min_range = float("+infinity")
    result = []
    for i in range(len(lt)):
        s = set()
        for j in range(i, len(lt)):
            s.add(lt[j][1])
            if len(s) == set_size:
                r = lt[j][0] - lt[i][0]
                min_range = min([r, min_range])
                result = lt[i:j+1]
                break
    return result


def get_range2(matrix):
    lt = get_list_tuples(matrix)
    set_size = len(matrix)
    min_range = float("+infinity")
    result = []
    for i in range(len(lt)):
        s = set()
        for j in range(i, len(lt)):
            s.add(lt[j][1])
            if len(s) == set_size:
                r = lt[j][0] - lt[i][0]
                min_range = min([r, min_range])
                result = lt[i:j+1]
                break
    return result


print get_range(matrix)