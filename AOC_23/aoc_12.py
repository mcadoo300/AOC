import copy
import math
input_file = open('input_12.txt','r')
lines = input_file.readlines()


for line in lines:
    line = line.strip()
    line = line.split(' ')
    q_mark = [False for _ in line[0]]
    for c in range(len(line[0])):
        if line[0][c] == "?":
            q_mark[c] = True
    sizes_of_gaps = []
    st = 0
    end = 0
    for i in range(len(q_mark)):
        if q_mark[i]:
            end +=1
            if i == len(q_mark)-1:
                sizes_of_gaps.append(end-st)
        else:
            if st != end:
                sizes_of_gaps.append(end-st)
            st=end
