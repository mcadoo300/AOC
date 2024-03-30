input_file = open("input_04.txt", "r")

lines = input_file.readlines()

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

total_valid = 0
is_valid = False
seen_fld = []

for row in range(len(lines)):
    line = lines[row].strip()
    if line == "":
        if is_valid:
            total_valid += 1
        is_valid = False
        seen_fld = []
    else:
        line = line.split(" ")
        for seg in line:
            seg = seg.split(":")
            if seg[0] != 'cid' and seg[0] not in seen_fld:
                seen_fld.append(seg[0])
        if len(fields) == len(seen_fld):
            is_valid = True
if is_valid:
    total_valid+=1
print(total_valid)
