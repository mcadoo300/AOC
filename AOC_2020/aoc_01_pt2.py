input_file = open('input_01.txt','r')
lines = input_file.readlines()

lines = [int(line.strip()) for line in lines]
lines = sorted(lines)

left = 0
right = len(lines)-1
sum = lines[left]+lines[right]
not_done = True
middle = -1
while not_done:
    diff = 2020-sum
    if diff in lines[left:right]:
        print(lines[left]*lines[right]*diff)
        not_done=False
    else:
        if diff > lines[right]:
            left+=1
        else:
            right-=1
        sum = lines[left]+lines[right]
    if left==right:
        not_done=False
