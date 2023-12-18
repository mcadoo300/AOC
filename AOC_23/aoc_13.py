import copy
import math
input_file = open('input_13.txt','r')
lines = input_file.readlines()

lines = [line.strip() for line in lines]

def Check_Horizontal(lines):
    for i in range(1,len(lines)):
        if lines[i-1] != lines[i]:
            if Off_By_One(lines[i-1],lines[i]):
                if Smudge_Mirror(lines[i-1],lines[i]):
                    mirror = True
                    forward = i+1
                    backward = i-2
                    while forward < len(lines) and backward >= 0:
                        if lines[forward] == lines[backward]:
                            forward += 1
                            backward -= 1
                        else:
                            mirror = False
                            break
                    if mirror:
                        return [i-1,i]
        else:
            mirror = True
            smudge_fixed = 0
            forward = i+1
            backward = i-2
            while forward < len(lines) and backward >= 0:
                if lines[forward] == lines[backward]:
                    forward += 1
                    backward -= 1
                elif Off_By_One(lines[forward],lines[backward]):
                    if Smudge_Mirror(lines[forward],lines[backward]):
                        smudge_fixed += 1
                        forward += 1
                        backward -= 1
                    else:
                        mirror = False
                        break
                else:
                    mirror = False
                    break
                if smudge_fixed > 1:
                    mirror = False
                    break
            if smudge_fixed == 1 and mirror:
                return [i-1,i]
    return [-1,-1]

def Transpose(lines):
    new_array = []
    for i in range(len(lines[0])):
        new_row = []
        for j in range(len(lines)):
            new_row.append(lines[j][i])
        new_array.append(new_row)
    return new_array


def Off_By_One(r1,r2):
    if r1.count("#") == r2.count("#") -1 or r1.count("#") == r2.count("#") +1:
        return True

def Smudge_Mirror(r1,r2):
    off_by_one = 0
    for i in range(len(r1)-1):
        if r1[i] != r2[i]:
            off_by_one += 1
            if off_by_one > 1:
                return False
    return True


maps = []
prev=0
for i in range(len(lines)):
    if lines[i] == "":
        maps.append(lines[prev:i])
        prev = i+1
    if i == len(lines)-1:
        maps.append(lines[prev:])
ans = 0  
for map in maps:
    if Check_Horizontal(map) == [-1,-1]:
        map = Transpose(map)
        mirror = Check_Horizontal(map)
        ans += mirror[1]
    else:
        mirror = Check_Horizontal(map)
        ans += mirror[1]*100
print(ans)