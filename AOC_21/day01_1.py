file = open("./input01.txt")
lines = file.readlines()

previous = 0
current = 0
ans =-1
for line in lines:
    line = line.strip()
    line = int(line)
    if line > previous:
        ans+=1
    previous = line
print(ans)
