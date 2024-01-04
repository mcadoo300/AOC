file = open('input_08.txt')
lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()


directions = [[0,1],[0,-1],[1,0],[-1,0]]

def checkVis(r,c):
    for dir in directions:
        new_r = r 
        new_c = c
        while 0 <= new_r+dir[0] < len(lines) and 0 <= new_c + dir[1] < len(lines[0]):
            new_r+= dir[0]
            new_c += dir[1]
            if lines[r][c] <= lines[new_r][new_c]:
                break
            elif new_r == 0 or new_r == len(lines) -1:
                return True
            elif new_c == 0 or new_c == len(lines[0])-1:
                return True
    return False

ans = 0
for row in range(1,len(lines)-1):
    for col in range(1,len(lines[0])-1):
        if checkVis(row,col):
            print(lines[row][col])
            print(f"row: {row}   col: {col}")
            ans+=1
print(ans)
print(ans + (len(lines)*2) + (len(lines[0])-2)*2)

