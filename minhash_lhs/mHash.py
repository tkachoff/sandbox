import random

class MinHash(object):

    def __init__(self, hash_object, randoms):
        self.hash_object = hash_object
        self.list_randoms = randoms
        self.min_hashes = []

    @staticmethod
    def generate_randoms():
        list_randoms = []
        for i in range(200):
            list_randoms.append(random.randint(1000000000000000000,
                                               9999999999999999999))
        return list_randoms

    def update(self, b):
        hashes = [self.hash_object(x) for x in b]
        for i in range(200):
            o_hashes = [x ^ self.list_randoms[i] for x in hashes]
            self.min_hashes.append(min(o_hashes))

    def jaccard(self, min_hash):
        return len(set(self.min_hashes).intersection(set(min_hash.min_hashes))) / float(len(set(self.min_hashes).union(set(min_hash.min_hashes))))

# mh = MinHash(hash_object=hash)
# print "-----"
#
# _mersenne_prime = (1 << 61) - 1
# _max_hash = (1 << 32) - 1
# _hash_range = (1 << 32)
#
#
# print _mersenne_prime
# print _max_hash
# print _hash_range

randoms = MinHash.generate_randoms()

mh1 = MinHash(hash_object=hash, randoms=randoms)
mh2 = MinHash(hash_object=hash, randoms=randoms)

s1 = "So, from now on, when a new device is added to your Google account, or, in other words, when a new device accesses your account, you will receive a push notification on your current Android device, asking"
s2 = "So, from now on, when a new device is added to your Google account, or, in other words, when a new device accesses your account, you will receive a push notification on your current Android device, asking"


mh1.update(s1.split())
mh2.update(s2.split())

print mh1.jaccard(mh2)
