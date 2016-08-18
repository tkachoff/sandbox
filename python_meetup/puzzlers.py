# print (1) + (2,)


x = 0

def foo():
    global x
    x += 1
    return x

bar = {
    1: None,
    3: None,
    5: None
}

for x in range(len(bar)):
    print bar.get(x, foo())

print x