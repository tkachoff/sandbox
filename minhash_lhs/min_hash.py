import random
import mmh3 as mmh3
from datasketch import MinHash


def hash(size):
    seed = random.randint(0, size) + 32

    def result_f(s):
        result = 1
        for char in s:
            result = (seed * result + ord(char)) & 0xFFFFFFFF
        return result
        # return mmh3.hash(s, seed=size)

    return result_f


def get_hash_functions(n):
    return [hash(i) for i in range(125, n + 999)]


lf = get_hash_functions(100)

s1 = "So, from now on, when a new device is added to your Google account, or, in other words, when a new device accesses your account, you will receive a push notification on your current Android device, asking"
s2 = "So, from now on, when a new device is added to your Google account, or, in other words, when a new device accesses your account, you will receive a push notification on your current Android device, asking"
# s2 = "Artsiom is great tester"
s3 = "Artsiom is programmer"


def min_hash(hash_f, s):
    p = [hash_f(x) for x in s.split()]
    return min(p)


d = {}


def get_min_hashes(s, list_hf):
    return [hash(s) for hash in list_hf]


d[s1] = get_min_hashes(s1, lf)
d[s2] = get_min_hashes(s2, lf)
d[s3] = get_min_hashes(s3, lf)

intersec_set12 = set.intersection(set(d[s1]), set(d[s2]))
intersec_set23 = set.intersection(set(d[s3]), set(d[s2]))

print len(intersec_set12) / float(len(d[s1]))
print len(intersec_set23) / float(len(d[s1]))

m1, m2 = MinHash(), MinHash()
for word in s1.split():
    m1.update(word.encode("utf8"))
for word in s2.split():
    m2.update(word.encode("utf8"))

print("Estimated Jaccard for data1 and data2 is", m1.jaccard(m2))



set1 = set(s1.split())
set2 = set(s2.split())

actual_jaccard = float(len(set1.intersection(set2)))/float(len(set1.union(set2)))
print("Actual Jaccard for data1 and data2 is", actual_jaccard)
