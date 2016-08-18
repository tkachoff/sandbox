import collections


# s = "aaaaaaabbbbbbbbbccd"


def get_dict(s):
    result = collections.defaultdict(int)
    for i in range(len(s)):
        result[s[i]] += 1
    return result


# print get_dict(s)
#
# print sorted(get_dict(s).items(), key=lambda x: x[1], reverse=True)


def get_rearranged(s):
    list_tuples = sorted(get_dict(s).items(), key=lambda x: x[1], reverse=True)
    list_arr = map(lambda x: list(x), list_tuples)
    result = ""
    first = True
    while len(list_arr) != 0:
        if first:
            result += list_arr[0][0]
            list_arr[0][1] -= 1
            if list_arr[0][1] == 0:
                list_arr.remove(list_arr[0])
            else:
                first = False
        else:
            result += list_arr[1][0]
            list_arr[1][1] -= 1
            if list_arr[1][1] == 0:
                list_arr.remove(list_arr[1])
            first = True
    return result


# print get_rearranged(s)


def get_indexes(empty_i, count):
    print range(empty_i, empty_i + count * 2, 2)


def get_rearrange2(s):
    list_tuples = sorted(get_dict(s).items(), key=lambda x: x[1], reverse=True)
    list_arr = map(lambda x: list(x), list_tuples)
    even_empty = 0
    odd_empty = 1
    even = True
    for arr in list_arr:
        if even:
            print get_indexes(even_empty, arr[1])
            even_empty = even_empty + arr[1] * 2 + 1
            even = False
        else:
            print get_indexes(odd_empty, arr[1])
            odd_empty = odd_empty + arr[1] * 2 + 1
            even = True


# get_rearrange2(s)


def get_max_occurence(length):
    if length % 2 == 0:
        return length / 2
    return length / 2 + 1


# print get_max_occurence(6)
# print get_max_occurence(5)



# s = "aaaaacccdc"


def permutate(s):
    l = list(s)
    mutated = True
    if len(s) > 1:
        while mutated:
            mutated = False
            for j in range(len(l) - 2):
                if l[j] == l[j + 1] and l[j + 1] != l[j + 2]:
                    l[j + 1], l[j + 2] = l[j + 2], l[j + 1]
                    mutated = True
                elif l[j] != l[j + 1] and l[j + 1] == l[j + 2]:
                    l[j + 1], l[j] = l[j], l[j + 1]
                    mutated = True
        if l[-1] == l[-2]:
            return None
    return "".join(l)


def permutate2(s):
    l = list(s)
    mutated = True
    if len(s) > 1:
        while mutated:
            mutated = False
            for j in range(len(l) - 2):
                if l[j] == l[j + 1]:
                    l[j + 2], l[j + 1] = l[j + 1], l[j + 2]
                    mutated = True
        if l[-1] == l[-2]:
            return None
    return "".join(l)


def perm(s):
    l = list(s)
    for i in range(len(l)):
        for j in range(len(l) - 2 - i):
            if l[j] == l[j + 1]:
                l[j + 2], l[j + 1] = l[j + 1], l[j + 2]
    return "".join(l)


def shortBubbleSort(s):
    alist = list(s)
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(1, passnum):
            if alist[i - 1] == alist[i] and alist[i] != alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum = passnum - 1
    return "".join(alist)


s = "aaaaacccdccccddddddddddddd"


# print shortBubbleSort(list(s))


def p(s):
    l = list(s)
    stack = []
    result = []
    while len(l) != 0:
        buf = l.pop(0)
        if len(stack) != 0 and stack[-1] == buf:
            stack.append(buf)
        elif len(stack) != 0 and stack[-1] != buf:
            result.append(stack.pop())
            result.append(buf)
    return "".join(result)


# print p(s)

def reverse(s):
    l = list(s)
    for i in range(len(s) // 2):
        l[i], l[-i - 1] = l[-i - 1], l[i]
    return "".join(l)


print reverse("123456")
