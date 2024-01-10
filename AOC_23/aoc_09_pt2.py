import copy
input_file = open('input_09.txt','r')
lines = input_file.readlines()
ans = 0
for i in range(len(lines)):
    numbers = lines[i].strip()
    numbers = [int(num) for num in numbers.split(' ')]
    new_numbers = numbers
    set_numbers = [numbers]
    while new_numbers.count(0) < len(new_numbers):
        next_set = [(new_numbers[i+1] - new_numbers[i] )for i in range(len(new_numbers)-1)]
        set_numbers.append(next_set)
        new_numbers = next_set
    print(set_numbers) 
    for j in range(len(set_numbers)-2,-1,-1):
        lower_set = set_numbers[j+1][-1]
        set_numbers[j].append(set_numbers[j][-1]+lower_set)
        if j == 0:
            ans += set_numbers[j][-1]
    print(ans)

