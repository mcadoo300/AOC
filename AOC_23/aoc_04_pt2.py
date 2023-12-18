input_file = open('input_4.txt','r')
lines = input_file.readlines()
total=0
for line in lines:
    line = line[line.index(':')+1:].strip()
    number_sets = line.split('|')
    winning_string = number_sets[0].strip()
    your_string = number_sets[1].strip()
    winning_numbers = winning_string.split()
    your_numbers = your_string.split()
    match_count = 0
    for num in winning_numbers:
        if num in your_numbers:
            match_count+=1
    if match_count >0:
        total+= 2**(match_count-1)
print(total)