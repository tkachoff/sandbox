def common_begining(strings):
    def common(str1, str2):
        for i in range(len(str1)):
            try:
                if str1[i] != str2[i]:
                    return str1[:i]
            except IndexError:
                return str1[:i]
        return str1

    return reduce(common, strings)


arr = ["asdf", "asdv", "asdfsg", "fgd", "asdfhdgdghfgdbnfgnfgnfhgn", "asfdfbbbdb"]

res = common_begining(arr)
print res






def common2(str1, str2):
    arr = [ord(a) ^ ord(b) for a, b in zip(str1, str2)]
    if len(arr) == 0:
        return ""
    for i in range(len(str1)):
        if arr[i] != 0:
            return str1[:i]
    return str1


