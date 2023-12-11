import copy
import math
input_file = open('input_10.txt','r')
lines = input_file.readlines()
for line in lines:
    line = line.strip()

# default top down, left to right
pipe_connections = [["|",[1,0]],["-",[0,1]],["L",[1,1]],["J",[1,-1]],["F",[1,-1]],["7",[1,1]]]
start = None
for row in range(len(lines)):
    for i in range(len(lines[row])):
        if lines[row][i] == "S":
            print(row)
            start = [row,i]
            print(start)
            break
    if start is not None:
        break

def Get_Possible_Adj(pipe):
    if pipe == "|":
        return [[-1,0],[1,0]]
    elif pipe == "-":
        return[[0,-1],[0,1]]
    elif pipe == "L":
        return[[-1,0],[0,1]]
    elif pipe == "J":
        return [[-1,0],[0,-1]]
    elif pipe == "F":
        return [[0,1],[1,0]]
    elif pipe == "7":
        return [[0,-1],[1,0]]
    else:
        return [[0],[0]]

    """elif pipe == "S":
        [[1,0],[0,1],[-1,0],[0,-1]]"""
    

def Is_Valid_Connection(direction,pipe2):
    if pipe2 == "S":
        return True
    op_dir = [d*-1 for d in direction]
    if op_dir in Get_Possible_Adj(pipe2):
        return True
    return False



not_found = True
ans = 1
pipe_line = [start,"S"]
for dir in [[1,0],[0,1],[-1,0],[0,-1]]:
    row = pipe_line[0][0] + dir[0]
    col = pipe_line[0][1] + dir[1]
    if 0 <= row < len(lines) and 0<= col < len(lines[0])-1:
        if lines[row][col] != ".":
            if Is_Valid_Connection(dir,lines[row][col]):
                pipe_line[1] = lines[row][col]
                pipe_line[0] = [row,col]
    if pipe_line[0] != start:
        break
prev_pipes = [start, pipe_line[0]]
while not_found:
    if pipe_line[1] == "S":
        not_found = False
    else:
        for move in Get_Possible_Adj(pipe_line[1]):
            row = pipe_line[0][0] + move[0]
            col = pipe_line[0][1] + move[1]
            if 0 <= row < len(lines) and 0<= col < len(lines[0])-1:
                if Is_Valid_Connection(move,lines[row][col]) and [row,col] not in prev_pipes:
                    pipe_line[1] = lines[row][col]
                    pipe_line[0] = [row,col]
                    prev_pipes.append(pipe_line[0])
                    break
    ans += 1
    if ans == 3:
        prev_pipes = prev_pipes[1:]
    if pipe_line[1] == "S":
        not_found = False
print(math.ceil(ans/2))