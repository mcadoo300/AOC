file = open("./input09.txt").readlines()

numbers = [[] for _ in range(len(file))]
new_row = []
for k in range(len(file)):
    line = file[k].strip()

    new_row = [[] for _ in range(len(file[0].strip()))]
    for i in range(len(line)):
        new_row[i] = [int(line[i]), True]
    numbers[k] = new_row

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ans = 0
mr = len(new_row)
mc = len(numbers)
basin_origin = []
for col in range(len(new_row)):
    for row in range(len(numbers)):
        is_low = True
        for d in dirs:
            if 0 <= col + d[1] < mr and 0 <= row + d[0] < mc:
                if numbers[row + d[0]][col + d[1]][0] <= numbers[row][col][0]:
                    is_low = False
        if is_low:
            basin_origin.append([row, col])

sizes = []
for bo in basin_origin:
    numbers[bo[0]][bo[1]][1] = False
    neighbors = [[bo[0], bo[1]]]
    size = 1
    while len(neighbors) > 0:
        n = neighbors.pop(0)
        for d in dirs:
            if (
                0 <= n[0] + d[0] < mc
                and 0 <= n[1] + d[1] < mr
                and numbers[n[0] + d[0]][n[1] + d[1]][0] != 9
                and numbers[n[0] + d[0]][n[1] + d[1]][1]
            ):
                numbers[n[0] + d[0]][n[1] + d[1]][1] = False
                neighbors.append([n[0] + d[0], n[1] + d[1]])
                size += 1
    sizes.append(size)
print(sizes)
print(sizes.sort(reverse=True))
ans = 1
for i in range(3):
    ans *= sizes[i]
print(ans)
