import copy
import math
input_file = open('input_11.txt','r')
lines = input_file.readlines()
dub_rows = []
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    if lines[i].count("#") == 0:
        dub_rows.append(i)
dub_cols = []
galaxies = []
for i in range(len(lines[0])):
    add_to_list = True
    for j in range(len(lines)):
        if lines[j][i] == "#":
            add_to_list = False
            galaxies.append([j,i])
    if add_to_list:
        dub_cols.append(i)

def Get_min_distance(p1,p2):
    distance = abs(p1[0] - p2[0])+ abs(p1[1] - p2[1])
    for dub in dub_rows:
        if min(p1[0],p2[0]) < dub < max(p1[0],p2[0]):
            distance+=1
    for dub in dub_cols:
        if min(p1[1],p2[1]) < dub < max(p1[1],p2[1]):
            distance+=1
    return distance

pairs = []
distances = []
for i in range(len(galaxies)):
    for j in range(len(galaxies)):
        if j!=i and [j,i] not in pairs:
            pairs.append([i,j])
            distances.append(Get_min_distance(galaxies[i],galaxies[j]))
print(sum(distances))
print(len(pairs))
    
