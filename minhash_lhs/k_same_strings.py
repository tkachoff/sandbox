s1 = "I like this world and pencil"
s2 = "I dont like that pencil and world"


def get_jaccard(s1, s2):
    set_one = set(s1.split())
    set_two = set(s2.split())
    c = set.intersection(set_one, set_two)
    u = set.union(set_one, set_two)
    return len(c) / float(len(u))


print get_jaccard(s1, s2)



