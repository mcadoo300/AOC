import copy
input_file = open('input_8.txt','r')
lines = input_file.readlines()

left_right = lines.pop(0).strip()

lines.pop(0)
map_keys = []
map_left = []
map_right = []
for line in lines:
    line = line.strip()
    map_keys.append(line[:3])
    map_left.append(line[7:10])
    map_right.append(line[12:15])
print(left_right)
print(map_keys)
print(map_left)
print(map_right)

steps = 0
not_found = True
current_loc = [x for x in map_keys if x[2] == 'A']
trip_counter = [[x,0] for x in current_loc]
for loc in range(len(current_loc)):
    c_loc = current_loc[loc]
    not_found = True
    steps = 0
    while not_found:
        for i in range(len(left_right)):
            direction = left_right[i]
            if direction == 'L':
                next_loc = map_left[map_keys.index(c_loc)]
                c_loc = next_loc
            else:
                next_loc = map_right[map_keys.index(c_loc)]
                c_loc = next_loc
            steps += 1
            if c_loc[2] == 'Z':
                trip_counter[loc][1] = steps
                not_found = False
print(trip_counter)
max_steps = max(trip_counter,key= lambda x: x[1])[1]
print(max_steps)
not_done = True
while not_done:
    for num in [x[1] for x in trip_counter]:
        if (max_steps/num) == int(max_steps/num):
            not_done = False
        else:
            not_done = True
            break
    max_steps+=1
print(max_steps)