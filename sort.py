import random


def qsort(iterable, key=lambda x: x, reverse=False):
    if len(iterable) < 2:
        return iterable
    else:
        pivot_index = random.randint(0, len(iterable) - 1)
        pivot = iterable[pivot_index]
        lesser = [x for x in
                  iterable[:pivot_index] + iterable[pivot_index + 1:] if
                  key(x) <= pivot]
        greater = [x for x in
                   iterable[:pivot_index] + iterable[pivot_index + 1:]
                   if key(x) > pivot]
        if reverse:
            return qsort(greater, key=key, reverse=reverse) \
                   + [pivot] + qsort(lesser, reverse=reverse)
        else:
            return qsort(lesser, key=key, reverse=reverse) \
                   + [pivot] + qsort(greater, reverse=reverse)


if __name__ == "__main__":
    arr = [1, 5, 2, 2, 4, 135, 8, 100, 3, 1, 0, 0, 0]
    print qsort(arr, reverse=True)
    print (sorted(arr, reverse=True))
    # print random.randint(0, 2)
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print a[3:]
    print a[:3]
