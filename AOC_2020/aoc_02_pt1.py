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
    rng = rng.split('-')
    lower = int(rng[0])
    upper = int(rng[1])
    if lower <= password.count(char) <=upper:
        valid+=1
print(valid)
