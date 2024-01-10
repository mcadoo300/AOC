import copy
file = open('input_12.txt','r')
map1 = file.readlines()


dirs = [[0,1],[0,-1],[1,0],[-1,0]]



start_row = 0
start_col = 0

for l in range(len(map1)):
    map1[l] = map1[l].strip()
    if "S" in map1[l]:
        start_row = l 
        start_col = map1[l].index("S")

paths = [[[start_row,start_col]]]
visited = [[True for _ in range(len(map1[0]))] for b in range(len(map1))]
not_found = True
while not_found:
    cur_path = paths.pop(0)
    for d in dirs:
        np = [cur_path[-1][0] + d[0],cur_path[-1][1] + d[1]]
        print(map1[np[0]][np[1]]) 
        if visited[np[0]][np[1]]:
            visited[np[0]][np[1]] = False
            if 0 <= np[0] < len(map1) and 0 <= np[1] < len(map1[0]):
                if len(cur_path)==1 or ord(map1[np[0]][np[1]]) <= ord(map1[cur_path[-1][0]][cur_path[-1][1]]) +1:
                    new_path = copy.deepcopy(cur_path)
                    new_path.append([np[0],np[1]])
                    paths.append(new_path)
                if map1[np[0]][np[1]] == "E":
                    print(len(cur_path)+1)
                    if ord("z") <= ord(map1[cur_path[-1][0]][cur_path[-1][1]]) +1:
                        print("end")
                        print(len(cur_path)+1)
                        not_found = False
    paths = sorted(paths,key=lambda x: len(x))
