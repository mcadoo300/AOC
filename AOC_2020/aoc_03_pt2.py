input_file = open("input_03.txt", "r")

lines = input_file.readlines()
trees = 0
x_cord = 0
deltas = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
total = 1
for x, y in deltas:
    for row in range(y, len(lines), y):
        line = lines[row]
        x_cord += x
        x_cord %= len(line.strip())
        if line[x_cord] == "#":
            trees += 1
    total *= trees
    x_cord = 0
    trees = 0
print(total)
