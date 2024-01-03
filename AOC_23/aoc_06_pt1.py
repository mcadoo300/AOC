input_file = open('input_06.txt','r')
lines = input_file.readlines()
import math

line = lines[0].split(':')[1].strip()

times = []
line = line.split(' ')
for intg in line:
    if len(intg) > 0:
        times.append(int(intg))
line = lines[1].split(':')[1].strip()
line = line.split(' ')
records = []
for intg in line:
    if len(intg) > 0:
        records.append(int(intg))
winning_nums = []
for i in range(len(times)):
    x_1 = ((times[i] + math.sqrt((times[i]**2)-(4*records[i])))/2)
    x_2 = ((times[i] - math.sqrt((times[i]**2)-(4*records[i])))/2)
    if int(x_1)==x_1 and x_2 == int(x_2):
        winning_nums.append(math.ceil(max(x_1,x_2))-math.ceil(min(x_1,x_2))-1)
    else:
        winning_nums.append(math.ceil(max(x_1,x_2))-math.ceil(min(x_1,x_2)))
    print(winning_nums)
total = 1
for num in winning_nums:
    total*=num
print(total)
