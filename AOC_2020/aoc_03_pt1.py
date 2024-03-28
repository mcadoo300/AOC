input_file = open("input_03.txt", "r")

lines = input_file.readlines()
trees = 0
x_cord = 0
for line in lines[1:]:
    line = line.strip()
    x_cord += 3
    x_cord %= len(line)
    if line[x_cord] == "#":
        trees += 1
print(trees)
