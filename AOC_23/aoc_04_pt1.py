input_file = open('input_4.txt','r')
lines = input_file.readlines()

total = 0
copies = [1 for _ in range(len(lines))]
card = 1
for line in lines:
    line = line[line.index(":")+1:].strip()
    i=0
    print(line)
    winning_numbers = []
    your_numbers = []
    while line[i] != '|':
        i = line.index(' ')
        winning_numbers.append(int(line[:i]))
        line = line[i+1:].strip()
        i = line.index(' ')
        i+=1
        print(line)
        print(winning_numbers)
    winning_numbers.append(int(line[:line.index('|')-1].strip()))
    i+=1
    line = line[i+1:].strip()
    while len(line) > 0:
        if line.count(' ')==0:
            your_numbers.append(int(line))
            line = ""
            print(your_numbers)
        else:
            i = line.index(' ')
            your_numbers.append(int(line[:i]))
            line = line[i+1:].strip()
            i+=1
            print(line)
            print(your_numbers)
    match_count =0
    for num in winning_numbers:
        if num in your_numbers:
            match_count+=1
    if match_count > 0:
        for c in range(1,match_count+1):
            copies[card+c-1]+=1*copies[card-1]
    card += 1
print(sum(copies))