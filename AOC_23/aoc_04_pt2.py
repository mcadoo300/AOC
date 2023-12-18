input_file = open('input_04.txt','r')
lines = input_file.readlines()
#Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
copies=[1 for _ in range(len(lines))]
for l in range(len(lines)):
    line = lines[l].split(":")[1].strip()
    winning_cards, your_cards = line.split("|")
    winning_cards = winning_cards.strip().split(' ')
    your_cards = your_cards.strip().split(' ')
    winning_count = 0
    for c in your_cards:
        if c != '':
            if c in winning_cards:
                winning_count+=1
    for _ in range(1,winning_count+1):
        copies[l+_]+=(1*copies[l])
print(sum(copies))
