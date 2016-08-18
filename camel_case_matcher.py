l = ["Hello", "World" "HelloMars", "HelloWorld", "HelloWorldMars", "HiHo"]

patterns = ["H", "He", "HeW", "HeWo", "HeWor", "HeWorM"]
# patterns = ["H", "HW", "Ho", "HeWorM", "He"]

d = {
    "HelloMars": ["Hello", "Mars"],
    "HelloWorld": ["Hello", "World"],
    "HelloWorldMars": ["Hello", "World", "Mars"],
    "HiHo": ["Hi", "Ho"]
}


def split_camel_case(word):
    result = []
    start = 0
    for i in range(1, len(word)):
        if word[i].isupper():
            result.append(word[start:i])
            start = i
    result.append(word[start:])
    return result


# for word in l:
#     print split_camel_case(word)

print '-----------'

pat = "HeWorM"


# print split_camel_case(pat)


def generate_splitetd_dict(l):
    result = {}
    for word in l:
        result[word] = split_camel_case(word)
    return result


# print generate_splitetd_dict(l)


def get_classes(p, l):
    pl = split_camel_case(p)
    spl_d = generate_splitetd_dict(l)
    for i in range(len(pl)):
        for k, v in spl_d.items():
            approved = False
            for w_i in range(i, len(v)):
                if v[w_i].startswith(pl[i]):
                    approved = True
            if not approved:
                del spl_d[k]
    return spl_d.keys()


for pattern in patterns:
    print pattern, get_classes(pattern, l)


def word_mut(word):
    result = []
    for i in range(len(word)):
        result.append(word[:i + 1])
    return result


def get_all_patterns(clazz):
    words = split_camel_case(clazz)
    result = []
    for word in words:
        result.append(word_mut(word))
    return result


print "---------"
print get_all_patterns("HelloWorldMars")
