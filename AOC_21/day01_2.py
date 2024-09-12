file = open("./input01.txt")
lines = file.readlines()

previous = 0
current = 0
ans =0
for i in range(len(lines)):
    if i+3 < len(lines):
        if int(lines[i+3].strip()) > int(lines[i].strip()):
            ans+=1
print(ans)
