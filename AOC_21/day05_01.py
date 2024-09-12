file = open("./input05.txt")

lines = [_.strip() for _ in file.readlines()]

marked_locations = {}

for line in lines:
    line = line.split("->")
    start_pos = line[0].strip().split(",")
    end_pos = line[1].strip().split(",")
    if start_pos[0] == end_pos[0]:
        diff = int(start_pos[1]) - int(end_pos[1])
        if diff > 0:
            for i in range(diff + 1):
                pos = str(int(end_pos[1]) + i)
                if (start_pos[0], pos) in marked_locations:
                    marked_locations[(start_pos[0], pos)] += 1
                else:
                    marked_locations[(start_pos[0], pos)] = 1
        else:
            for i in range(abs(diff) + 1):
                pos = str(int(start_pos[1]) + i)
                if (start_pos[0], pos) in marked_locations:
                    marked_locations[(start_pos[0], pos)] += 1
                else:
                    marked_locations[(start_pos[0], pos)] = 1
    elif start_pos[1] == end_pos[1]:
        diff = int(start_pos[0]) - int(end_pos[0])
        if diff > 0:
            for i in range(diff + 1):
                pos = str(int(end_pos[0]) + i)
                if (pos, start_pos[1]) in marked_locations:
                    marked_locations[(pos, start_pos[1])] += 1
                else:
                    marked_locations[(pos, start_pos[1])] = 1
        else:
            for i in range(abs(diff) + 1):
                pos = str(int(start_pos[0]) + i)
                if (pos, start_pos[1]) in marked_locations:
                    marked_locations[(pos, start_pos[1])] += 1
                else:
                    marked_locations[(pos, start_pos[1])] = 1

count = 0
print(marked_locations)
for a in marked_locations:
    if marked_locations[a] > 1:
        print(a)
        count += 1
print(count)
