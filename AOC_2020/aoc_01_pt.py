input_file = open('input_01.txt','r')
lines = input_file.readlines()

lines = [int(line.strip()) for line in lines]
lines = sorted(lines)

left = 0
right = len(lines)-1
sum = lines[left]+lines[right]

while sum != 2020:
    if sum > 2020:
        right-=1
    else:
        left+=1
    sum = lines[left]+lines[right]
print(lines[left]*lines[right])
