a = [1, 34, 76, 45, 97, 56, 79, 356, 579, 454, 578, 467, 786]
a = sorted(a)


def bin_search(iterable, target):
    start = 0
    end = len(iterable)

    while end - start != 1:
        guess = (end + start) / 2
        if iterable[guess] == target:
            return guess
        elif iterable[guess] < target:
            start = guess
        else:
            end = guess

    return start, end


class BinSearchArray(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        index = self.bin_search_position(item)
        self.container.insert(index, item)

    def bin_search_position(self, target):
        start = 0
        end = len(self.container)
        if start != end:
            while end - start != 1:
                guess = (end + start) / 2
                if self.container[guess] == target:
                    return guess
                elif self.container[guess] < target:
                    start = guess + 1
                else:
                    end = guess - 1
        return start


# print a
# print bin_search(a, 0)

search = BinSearchArray()
search.add(3)
search.add(1)
search.add(2)

print search.container