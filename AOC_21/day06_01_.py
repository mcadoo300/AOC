inp = open("./test.txt").readline().strip().split(",")
print(inp)
op = 0
for n in inp:
    steps = 18 - int(n)
    new_fsh = steps // 7
    op += 1+ (new_fsh)
print(op)
