def isValidSegment(seg, value):
    if seg == "byr":
        if len(value) != 4:
            return False
        return 1920 <= int(value) <= 2002
    elif seg == "iyr":
        if len(value) != 4:
            return False

        return 2010 <= int(value) <= 2020
    elif seg == "eyr":
        if len(value) != 4:
            return False
        return 2020 <= int(value) <= 2030
    elif seg == "hgt":
        if value[-2:] == "cm":
            return 150 <= int(value[:-2]) <= 193
        elif value[-2:] == "in":
            return 59 <= int(value[:-2]) <= 76
        else:
            return False
    elif seg == "hcl":
        if value[0] == "#":
            if len(value) == 7:
                for c in value[1:]:
                    if c.isdigit() is False and c.islower() is False:
                        return False
                return True
            else:
                return False
        else:
            return False
    elif seg == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif seg == "pid":
        if len(value) == 9:
            for c in value:
                if c.isdigit() is False:
                    return False
            return True
    else:
        return True


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
        print(seen_fld)
        seen_fld = []
    else:
        line = line.split(" ")
        for seg in line:
            seg = seg.split(":")
            if seg[0] != "cid" and seg[0] not in seen_fld:
                if isValidSegment(seg[0], seg[1]):
                    seen_fld.append(seg[0])
        if len(fields) == len(seen_fld):
            is_valid = True
if is_valid:
    total_valid += 1
print(total_valid)
