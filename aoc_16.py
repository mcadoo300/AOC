import os
import math
input_file = open('input_16.txt','r')
lines = input_file.readlines()
lines= [line.strip() for line in lines]

visited_flags = [[False for _ in range(len(lines[0]))] for k in range(len(lines))]

mirror_direction = []


def Horizontal_Beam(map,row,col,dir):
    while (0 <= col < len(map[row])) and map[row][col] == ".":
        visited_flags[row][col] = True
        col += dir[1]
    if col < 0:
        return None
    elif col >= len(map[row]):
        return None
    return [row,col]

def Vertical_Beam(map,row,col,dir):
    while (0 <= row < len(map)) and (map[row][col] == "."):
        visited_flags[row][col] = True
        row += dir[0]
    if row < 0:
        return None
    elif row >= len(map):
        return None
    return [row,col]

def Is_mirror(char):
    if char == "|" or char == "-" or char == "\\" or char == "/":
        return True
    else:
        return False

def End_Beam(pos,dir):
    if Is_mirror(lines[pos[0]][pos[1]]):
        if visited_flags[pos[0]+dir[0]][pos[1]+dir[1]]:
            return True
    else:
        if visited_flags[pos[0]][pos[1]]:
            return True
    return False


def Next_Dir(char,dir):
    if Is_mirror(char):
        if char == "|":
            if dir == [1,0]:
                return [[1,0]]
            if dir == [-1,0]:
                return [[-1,0]]
            return [[1,0],[-1,0]]
        elif char == "-":
            if dir == [0,1]:
                return [[0,1]]
            if dir == [0,-1]:
                return [[0,-1]]
            return [[0,1],[0,-1]]
        elif char == "\\":
            if dir[0] == 0:
                return [[dir[1],0]]
            else:
                return [[0,dir[0]]]
        else:
            if dir[0] == 0:
                return [[-dir[1],0]]
            else:
                return [[0,-dir[0]]]


def Print_Trace():
    sum1 = 0
    for i in range(len(lines)):
        row = []
        for j in range(len(lines[i])):
            if visited_flags[i][j]:
                row.append("#")
                sum1 += 1
            else:
                row.append(".")
        #print(row)
    return sum1


possible_start = []
possible_dir = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if i == 0 or j == 0:
            if i == 0 and j == 0:
                possible_dir.append([0,1])
                possible_start.append([i,j])
                possible_dir.append([1,0])
                possible_start.append([i,j])
            else:
                if i == 0:
                    possible_dir.append([1,0])
                    possible_start.append([i,j])
                else:
                    possible_dir.append([0,1])
                    possible_start.append([i,j])
        elif i == (len(lines)-1) or (j == len(lines[i])-1):
            if i == (len(lines)-1) and (j == len(lines[i])-1):
                possible_dir.append([0,-1])
                possible_start.append([i,j])
                possible_dir.append([-1,0])
                possible_start.append([i,j])
            else:
                if i == (len(lines)-1):
                    possible_dir.append([-1,0])
                    possible_start.append([i,j])
                else:
                    possible_dir.append([0,-1])
                    possible_start.append([i,j])

max_eng = []
for y in range(4,len(possible_start)):
    visited_flags = [[False for _ in range(len(lines[0]))] for k in range(len(lines))]
    mirror_direction = []
    beam_pos = [possible_start[y]]
    beam_dir = [possible_dir[y]]
    while len(beam_pos) > 0:
        p = beam_pos.pop(0)
        d = beam_dir.pop(0)
        
        if [p,d] not in mirror_direction:
            mirror_direction.append([p,d])
            if d[0] == 0:
                new_p = Horizontal_Beam(lines,p[0],p[1],d)
                if new_p is not None:
                    visited_flags[new_p[0]][new_p[1]] = True
                    if Is_mirror(lines[new_p[0]][new_p[1]]):
                        new_dir = Next_Dir(lines[new_p[0]][new_p[1]],d)
                    for dir in new_dir:
                        if 0 <= new_p[0] + dir[0] < len(lines) and 0 <= new_p[1] + dir[1] < len(lines[0]):
                            beam_pos.append([new_p[0] + dir[0],new_p[1] + dir[1]])
                            beam_dir.append(dir)
            else:
                new_p = Vertical_Beam(lines,p[0],p[1],d)
                if new_p is not None:
                    visited_flags[new_p[0]][new_p[1]] = True
                    if Is_mirror(lines[new_p[0]][new_p[1]]):
                        new_dir = Next_Dir(lines[new_p[0]][new_p[1]],d)
                    for dir in new_dir:
                        if 0 <= new_p[0] + dir[0] < len(lines) and 0 <= new_p[1] + dir[1] < len(lines[0]):
                            beam_pos.append([new_p[0] + dir[0],new_p[1] + dir[1]])
                            beam_dir.append(dir)
            Print_Trace()
            #print('\n')
    max_eng.append(Print_Trace())

print(max(max_eng))
