file = open("./input03.txt")

lines = [_.strip() for _ in file.readlines()]

gamma = [0 for _ in range(len(lines[0]))]

for line in lines:
    for i in range(len(line)):
        if int(line[i]) > 0:
            gamma[i]+=1
        else:
            gamma[i]-=1

for g in range(len(gamma)):
    if gamma[g]>0:
        gamma[g]=1
    else:
        gamma[g]=0

s = len(gamma)-1
g=0
e=0
for ga in gamma:
    if ga ==1:
        g+=(2**s)
    else:
        e+=(2**s)
    s-=1
print(g*e)

