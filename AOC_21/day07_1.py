file = open("./test.txt").readline().strip()

values = [int(_) for _ in file.split(",")]

delta = 0
aligned = []
output = 0
while 0 != len(values):
    for k in range(len(values)):
        for j in range(len(values)):
            if j != k and abs(values[k] - values[j]) == delta:
                output += abs(values[k] - values[j])
                aligned.append(values[k])
                aligned.append(values[j])
    for _ in aligned:
        print(values)
        print(_)
        values.remove(_)
    delta += 1
print(output)
