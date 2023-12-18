input_file = open('input_03.txt','r')
lines = input_file.readlines()

directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]

ans = 0
for l in range(len(lines)):
    line = lines[l].strip()
    k=0
    while k <(len(line)):
        i =0
        add = False
        while k+i < len(line) and line[k+i].isdigit():
            for d in directions:
                row = l+d[0]
                col = k+i+d[1]
                if 0 <= row < len(lines) and 0<= col < len(line):
                    if lines[row][col].isdigit() is False:
                        if lines[row][col] != ".":
                            add = True
            i+=1
        if add:
            ans += int(lines[l][k:k+i])
        k+=max(1,i)
print(ans)

