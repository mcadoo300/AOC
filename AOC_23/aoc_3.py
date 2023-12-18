
input_file = open('input_3.txt','r')
lines = input_file.readlines()
total_sum = 0
digits = [[] for _ in range(len(lines))]
symbols = [[] for _ in range(len(lines))]
row = 0
j=0
for line in lines:
    for i in range(len(line)):
        if i >= j:
            if line[i].isdigit():
                j = i
                digit = ""
                while line[j].isdigit():
                    digit += line[j]
                    j += 1
                digits[row].append([int(line[i:j]), [pos for pos in range(max(i-1,0),min(j+1,len(line)-1))]])

            elif line[i] == "*":
                symbols[row].append(i)
    row += 1
    j=0

for row in range(len(symbols)):
    if len(symbols[row]) > 0:
        add = False
        adjacent_count = 0
        gear_parts = []
        for star in symbols[row]:
            for r in range(max(0,row-1),min(len(lines),row+2)):
                for digit in digits[r]:
                    if star in digit[1]:
                        adjacent_count+=1
                        gear_parts.append(digit[0])
            if len(gear_parts)==2:
                total_sum += (gear_parts[0]*gear_parts[1])
                add = False
                adjacent_count = 0
            gear_parts = []
print(total_sum)