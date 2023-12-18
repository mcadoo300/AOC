import copy
import math
input_file = open('input_15.txt','r')
lines = input_file.readlines()
lines= lines[0].strip()
lines = lines.split(",")
boxes = [[] for _ in range(256)]
values = [[] for _ in range(256)]
for line in lines:
    hash_val = 0
    k =0
    while line[k] != "-" and line[k] != "=":
        hash_val += ord(line[k])
        hash_val *= 17
        hash_val = hash_val % 256
        k += 1
    if line[k] == "=":
        if line[:k] in boxes[hash_val]:
            values[hash_val][boxes[hash_val].index(line[:k])] = int(line[-1])
        else:
            boxes[hash_val].append(line[:k])
            values[hash_val].append(int(line[-1]))
    else:
        if line[:k] in boxes[hash_val]:
            if len(values[:boxes[hash_val].index(line[:k])]) > 0:
                new_vals = values[:boxes[hash_val].index(line[:k])]
            else:
                new_vals = []
            if len(values[hash_val][len(new_vals)+1:]) > 0:
                for val in values[hash_val][len(new_vals)+1:]:
                    new_vals.append(val)
                    values[hash_val] = new_vals
                    while [] in values[hash_val]:
                        values[hash_val].remove([])
            else:
                values[hash_val] = new_vals
                while [] in values[hash_val]:
                    values[hash_val].remove([])
            boxes[hash_val].remove(line[:k])
            
ans = 0
for i in range(len(values)):
    for k in range(len(values[i])):
        if isinstance(values[i][k], int):
            print(values[i][k])
            ans += (1+i)*(1+k)*(values[i][k])


print(ans)