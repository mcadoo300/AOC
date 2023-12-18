input_file = open('input_03.txt','r')
lines = input_file.readlines()

directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
gears = {}
ans = 0
for l in range(len(lines)):
    line = lines[l].strip()
    k=0
    while k <(len(line)):
        i =0
        add = False
        gear_pos = []
        while k+i < len(line) and line[k+i].isdigit():
            for d in directions:
                row = l+d[0]
                col = k+i+d[1]
                if 0 <= row < len(lines) and 0<= col < len(line):
                    if lines[row][col].isdigit() is False:
                        if lines[row][col] == "*":
                            add = True
                            gear_pos.append((row,col))
            i+=1
        if add:
            val = int(lines[l][k:k+i])
            for gear in gear_pos:
                if gears.get(gear) is None:
                    gears.update({gear:[val]})
                else:
                    prev_set = gears.get(gear)
                    if val not in prev_set:
                        prev_set.append(val)
                    gears.update({gear:prev_set})
        k+=max(1,i)
for g,s in gears.items():
    if len(s)==2:
        ans += (s[0]*s[1])
print(ans)

