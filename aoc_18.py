import os
import copy
input_file = open('input_18.txt','r')
lines = input_file.readlines()
lines= [line.strip() for line in lines]


dirs = {"3":[-1,0],"1":[1,0], "2":[0,-1], "0":[0,1]}

points = [[0,0]]


to_hex = {"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}

def Process_hex(code):
    int_val = 0
    d = dirs.get(code[-2])
    code = code[2:-2]
    p = 0
    for c in code[::-1]:
        if c in to_hex.keys():
            int_val += to_hex.get(c) * (16**p)
        else:
            int_val += int(c) * (16**p)
        p+=1
    return d,int(int_val)




border = 0
for line in lines:
    line = line.split(' ')
    d,val = Process_hex(line[-1])
    border += val
    points.append([points[-1][0]+(val*d[0]), points[-1][1] + (val*d[1])])


vert_shift = abs(sorted(points,key=lambda x: x[0])[0][0])
hor_shift = abs(sorted(points,key=lambda x : x[1])[0][1])

area = 0
for i in range(len(points)-1):
    area += (0.5 * ((points[i][0]+vert_shift) + (points[i+1][0] + vert_shift)) * ((points[i][1]+hor_shift) - (points[i+1][1] + hor_shift)))
print(area+border/2+1)