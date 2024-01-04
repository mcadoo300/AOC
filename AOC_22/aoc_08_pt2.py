file = open('input_08.txt')
lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()


directions = [[0,1],[0,-1],[1,0],[-1,0]]

def distanceVis(r,c):
    print(f" row: {r}  col: {c}")

    vis = 1
    for dir in directions:
        new_r = r 
        new_c = c
        while 0 <= new_r+dir[0] < len(lines) and 0 <= new_c + dir[1] < len(lines[0]):
            new_r+= dir[0]
            new_c += dir[1]
            if lines[r][c] <= lines[new_r][new_c]:
                print(f"equal or larger   dir: {dir}")
                new_val = abs(new_r - r) + abs(new_c - c)
                print(f"new val: {new_val}")
                print(f"prev vis: {vis}")
                vis *= (new_val)
                break
            elif new_r == 0 or new_r == len(lines) -1:
                print(abs(new_r-r) + abs(new_c - c))
                vis *= (abs(new_r - r) + abs(new_c - c))
                break
            elif new_c == 0 or new_c == len(lines[0])-1:
                print(abs(new_r-r) + abs(new_c - c)) 
                vis *= (abs(new_r - r) + abs(new_c - c))
                break
        print(f"new vis: {vis}")
    return vis

ans = 0
for row in range(1,len(lines)-1):
    for col in range(1,len(lines[0])-1):
        print(ans)
        ans = max(ans,distanceVis(row,col))
        print(ans)
        print(f"row: {row} col: {col}")
print(ans)

