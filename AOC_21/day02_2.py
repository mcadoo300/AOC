file = open("./input02.txt")

lines = [_.strip() for _ in file.readlines()]

h=0
d=0
x=0
for line in lines:
    line = line.split(" ")
    if line[0]=="forward":
        h+=int(line[1])
        x+=int(line[1])*d
    elif line[0]=="up":
        d-=int(line[1])
    else:
        d+=int(line[1])
print(h*x)
