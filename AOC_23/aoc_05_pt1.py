input_file = open('input_05.txt','r')
lines = input_file.readlines()

new_section = ["seed-to-soil map:","soil-to-fertilizer map:","fertilizer-to-water map:",
               "water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:"]

previous_numbers = lines[0]
lines = lines[1:]

seeds = []
previous_numbers = previous_numbers.split(':')[1].strip()
previous_numbers = previous_numbers.split(' ')
change_check = [True for _ in range(len(previous_numbers))]
for line in lines:
    line = line.strip()
    if line in new_section:
        new_section.pop(0)
        change_check = [True for _ in range(len(previous_numbers))]
    elif line != '':
        new_numbers = line.split(' ')
        for prev_num in range(len((previous_numbers))):
            if change_check[prev_num]:
                if int(new_numbers[1]) <= int(previous_numbers[prev_num]) < int(new_numbers[1]) + int(new_numbers[2]):
                    previous_numbers[prev_num]= int(previous_numbers[prev_num]) - int(new_numbers[1]) + int(new_numbers[0])
                    change_check[prev_num] = False

print(min(previous_numbers))
