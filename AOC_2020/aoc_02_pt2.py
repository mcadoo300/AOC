input_file = open("input_02.txt", "r")
lines = input_file.readlines()
valid = 0
for line in lines:
    line = line.split(":")
    param = line[0].strip()
    password = line[1].strip()
    param = param.split(" ")
    char = param[1]
    rng = param[0]
    rng = rng.split("-")
    first = int(rng[0]) - 1
    last = int(rng[1]) - 1
    count = 0
    if 0 <= first < len(password):
        if password[first] == char:
            count += 1
    if 0 <= last < len(password):
        if password[last] == char:
            count += 1
    if count == 1:
        valid += 1


print(valid)
