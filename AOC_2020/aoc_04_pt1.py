input_file = open("input_04.txt", "r")

lines = input_file.readlines()

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

total_valid = 0
is_valid = False
for row in range(len(lines)):
    line = lines[row].strip()
    if line == "":
        if is_valid:
            total_valid += 1
        is_valid = False
    else:
        seen_fld = []
        line = line.strip(" ")
        for seg in line:
            seg = seg.split(":")
            if seg[0] not in seen_fld:
                seen_fld.append(seg[0])
        if len(fields)-1 == len(seen_fld):
            if "cid" not in seen_fld:
                is_valid = True
        elif len(fields) == len(seen_fld):
            is_valid = True
print(total_valid)
