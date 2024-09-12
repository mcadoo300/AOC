file = open("./input08.txt").readlines()

outputs = {
    "cf": 1,
    "acf": 7,
    "bcdf": 4,
    "acdeg": 2,
    "acdfg": 3,
    "abdfg": 5,
    "abcefg": 0,
    "abdefg": 6,
    "abcdfg": 9,
    "abcdefg": 8,
}
wires = {
    "a": "a",
    "b": "b",
    "c": "c",
    "d": "d",
    "e": "e",
    "f": "f",
    "g": "g",
}
ans = 0
min_sz = 100


def get_a(mappings):
    one = [x for x in mappings if len(x) == 2][0]
    seven = [x for x in mappings if len(x) == 3][0]
    for c in seven:
        if c not in one:
            return c
    return "-1"


def get_d(mappings):
    four = [x for x in mappings if len(x) == 4][0]
    blah = [x for x in mappings if len(x) == 5]
    for f in four:
        add = True
        for b in blah:
            if f not in b:
                add = False
                break
        if add:
            return f
    return "-1"


def get_b(mappings, d):
    four = [x for x in mappings if len(x) == 4][0]
    one = [x for x in mappings if len(x) == 2][0]
    for f in four:
        if f != d and f not in one:
            return f
    return "-1"


def get_fg(mappings, d, b, a):
    blah = [x for x in mappings if len(x) == 5]
    real_g = ""
    for g in blah[0]:
        is_g = True
        if g == a or g == d:
            is_g = False
        for bl in blah:
            if g not in bl:
                is_g = False
                break
        if is_g:
            real_g = g
            break
    for bl in blah:
        if b in bl:
            for k in bl:
                if k not in [d, b, a, real_g]:
                    return k, real_g
    return "-1", "-1"


def get_e(mappings, c, d):
    eight = [x for x in mappings if len(x) == 7][0]
    nine = [x for x in mappings if len(x) == 6]
    for n in nine:
        if c in n and d in n:
            for e in eight:
                if e not in n:
                    return e
    return "-1"


def get_c(mappings, f):
    one = [x for x in mappings if len(x) == 2][0]
    for o in one:
        if o != f:
            return o
    return "-1"


for line in file:
    on = ""
    line = line.strip()
    line = line.split("|")
    op = line[1].strip().split(" ")
    line = line[0].strip().split(" ")
    new_mapping = {}
    for n in line:
        if n not in new_mapping.keys():
            new_mapping[n] = -1
    wires["a"] = get_a(new_mapping)
    wires["d"] = get_d(new_mapping)
    wires["b"] = get_b(new_mapping, wires["d"])
    wires["f"], wires["g"] = get_fg(new_mapping, wires["d"], wires["b"], wires["a"])
    wires["c"] = get_c(new_mapping, wires["f"])
    wires["e"] = get_e(new_mapping, wires["c"], wires["d"])
    for o in op:
        new_val = ""
        for k, v in wires.items():
            if v in o:
                new_val += k
        on += str(outputs[new_val])
    ans += int(on)
print(ans)
