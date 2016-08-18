# 1000000001
# 9999999997
import math

import collections

n = 100


def get_max_multipier(n):
    mult = math.sqrt(n)
    if mult % 1 == 0:
        return int(mult)
    else:
        return int(mult) + 1


def get_array(n):
    # max_mult = get_max_multipier(n)
    res = [0] * (n + 1)
    for i in range(2, (n // 2) + 1):
        for j in range(i, (n // i) + 1):
            res[i * j] += 1
    return res


def get_prime(n):
    res = get_array(n)
    result = []
    for i in range(len(res)):
        if res[i] == 0:
            result.append(i)
    return result


print get_array(100)
print get_prime(1000000000)