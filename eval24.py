import itertools
symbols = ["+","-","*","/"]
symbols_plus = ["+","*","/"]
symbols_minus = ["-","*","/"]


brackets = ["(",")"]
integers = [1, 2, 3, 4]



pm = map(lambda x: ["-"] + list(x), list(itertools.permutations(symbols_plus)))
pp = map(lambda x: ["+"] + list(x), list(itertools.permutations(symbols_minus)))

perm_symbols = pp + pm
print perm_symbols

result = []
for sym_arr in perm_symbols:
    for repm_int in itertools.permutations(integers):
        perm = ""
        for i in range(4):
            perm += sym_arr[i] + str(repm_int[i])
        result.append(perm)

print result

def get_permut(integers):
    symbols_plus = ["+", "*", "/"]
    symbols_minus = ["-", "*", "/"]
    # brackets = ["(", ")"]
    # integers = [1, 2, 3, 4]
    pm = map(lambda x: ["-"] + list(x),
             list(itertools.permutations(symbols_plus)))
    pp = map(lambda x: ["+"] + list(x),
             list(itertools.permutations(symbols_minus)))
    perm_symbols = pp + pm
    # print perm_symbols
    result = []
    for sym_arr in perm_symbols:
        for repm_int in itertools.permutations(integers):
            perm = ""
            for i in range(4):
                perm += sym_arr[i] + str(repm_int[i])
            result.append(perm)
    return result


def get_statement(integers, target):
    perms = get_permut(integers)
    for i in perms:
        exec "x=" + i
        if x == target:
            return i + " = " + str(x)

get_statement([2,3,5,11], 24)