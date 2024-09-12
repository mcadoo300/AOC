file = open("./input03.txt")

lines = [_.strip() for _ in file.readlines()]

bc = [0 for _ in range(len(lines[0]))]
scrubber = lines
other =[]
r=0
while len(scrubber) > 1:
    for line in scrubber:
        if int(line[r]) > 0:
            bc[r]+=1
        else:
            bc[r]-=1
    if bc[r]>=0:
        bc[r]=1
    else:
        bc[r]=0
    scrubber = [ x for x in scrubber if int(x[r])!=bc[r]]
    r+=1

s = len(bc)-1
g=0
e=0
print(scrubber)
for ga in scrubber[0]:
    if int(ga) ==1:
        g+=(2**s)
    else:
        e+=(2**s)
    s-=1
print(g)
print(841*3384)
