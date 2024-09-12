file = open("./input09.txt").readlines()

numbers = [[] for _ in range(len(file))]

for k in range(len(file)):
    line = file[k].strip()

    new_row = [0 for _ in range(len(file[0].strip()))]
    for i in range(len(line)):
        new_row[i] = int(line[i])
    numbers[k] = new_row

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ans = 0
mr = len(new_row)
mc = len(numbers)
for col in range(len(new_row)):
    for row in range(len(numbers)):
        is_low = True
        for d in dirs:
            if 0 <= col + d[1] < mr and 0 <= row + d[0] < mc:
                if numbers[row + d[0]][col + d[1]] <= numbers[row][col]:
                    if row == 0 and col == 1:
                        print(d)
                        print(numbers)
                        print(numbers[row + d[0]][col + d[1]])
                    is_low = False
        if is_low:
            ans += 1
            ans += numbers[row][col]

print(ans)
