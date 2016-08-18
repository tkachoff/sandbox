import collections

s = "aaasdff"


def conctruct_dict(s):
    res = collections.defaultdict(int)
    for char in s:
        res[char] += 1
    return res


def get_polindrom(s):
    d = collections.defaultdict(int)
    for char in s:
        d[char] += 1
    result = []
    odd_added = False
    for k, v in d.items():
        if not odd_added:
            if v % 2 != 0:
                odd_added = True
                result = result[:(len(result)/2)] + [k] * v + result[(len(result)/2):]
        else:
            result += [k] * (v // 2)
            result = [k] * (v // 2) + result
    return "".join(result)

print dict(conctruct_dict(s))
print get_polindrom(s)
