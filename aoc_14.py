import copy
import math
input_file = open('input_14.txt','r')
lines = input_file.readlines()
lines= [line.strip() for line in lines]

def Transpose(lines):
    new_array = []
    for i in range(len(lines[0])):
        new_row = []
        for j in range(len(lines)):
            new_row.append(lines[j][i])
        new_array.append(new_row)
    return new_array



def Get_Blocks(col):
    indices = [-1]
    for i in range(len(col)):
        if col[i] == "#":
            indices.append(i)
    return indices


def Move_Circles(lines):
    lines = Transpose(lines)
    for x in range(len(lines)):
        block_pos = Get_Blocks(lines[x])
        
        if len(block_pos) == 1:
            rock_count = lines[x].count("O")
            for p in range(len(lines[x])):
                if p < rock_count:
                    lines[x][p] = "O"
                else:
                    lines[x][p] = "."
        else:
            for y in range(len(block_pos)):
                if y == len(block_pos)-1:
                    rock_count = lines[x].count("O")
                    for p in range(len(lines[block_pos[y]+1:])):
                        if p < rock_count:
                            lines[x][p] = "O"
                        else:
                            lines[x][p] = "."
                else:
                    rock_count = lines[x][block_pos[y]+1:block_pos[y+1]].count("O")
                    for p in range(block_pos[y]+1,block_pos[y+1]):
                        if p < rock_count:
                            lines[x][p] = "O"
                        else:
                            lines[x][p] = "."
    return lines
                
for _ in lines:
    print(_)
lines = Move_Circles(lines)
for _ in lines:
    print(_)

"""block = [[] for _ in range(len(lines[0]))]
for i in range(len(lines[0])):
    for j in range(len(lines)):
        if lines[j][i] == "#":
            block[i].append(j)"""

def Get_Circles_Below(row,block):
    if len(block) == 1:
        count = 0
        for i in range(block[0],len(lines)):
                if lines[i][row] == "O":
                    count += 1
        return [count]
    else:
        count = [0 for _ in range(len(block))]
        i = 0
        start = block[i]
        stop = block[ i + 1]
        while i < len(count):
                if i == len(count) -1:
                    for j in range(start,len(lines)):
                        if lines[j][row] == "O":
                            count[i] += 1
                    i +=1
                else:
                    for j in range(start,stop):
                        if lines[j][row] == "O":
                            count[i] += 1
                    i += 1
                    start = block[i]
                    if i < len(block)-1:
                        stop = block[ i + 1]
        return count
    
def Get_Circles_Above(row,first_block):
    count = 0
    for i in range(0,first_block):
        if lines[i][row] == "O":
            count += 1
    return count







# 10-b- i for i in range(count)
"""ans = 0
for i in range(len(block)):
    if len(block[i]) > 0:
        ct = Get_Circles_Below(i,block[i])
        for c in range(len(ct)):
            for j in range(ct[c]):
                ans += ((len(lines)) - block[i][c] - j-1)
        ct = Get_Circles_Above(i,block[i][0])
        for j in range(ct):
            ans += ((len(lines)) - j)
    else:
        ct = Get_Circles_Above(i,len(lines))
        for j in range(ct):
            ans += ((len(lines))- j)

print(ans)"""