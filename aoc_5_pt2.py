input_file = open('input_5.txt','r')
lines = input_file.readlines()

new_section = ["seed-to-soil map:","soil-to-fertilizer map:","fertilizer-to-water map:",
               "water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:"]

previous_numbers = lines[0]
lines = lines[1:]

seeds = []
previous_nums = previous_numbers.split(':')[1].strip()
previous_numbers = previous_nums.split(' ')

int_number = [int(num) for num in previous_numbers]
seed_numbers = []
for p in range(0,len(int_number),2):
    seed_numbers.append([int_number[p],int_number[p+1]])

seed_to_soil = []
soil_to_fert = []
fert_to_water = []
water_to_light = []
light_to_temp = []
temp_to_hum = []
hum_to_loc = []


number_set = []


map_set = [seed_to_soil,soil_to_fert,fert_to_water,water_to_light,light_to_temp,temp_to_hum,hum_to_loc]
map_num = 0
for line in lines:
    line = line.strip()
    if line in new_section:
        if len(number_set) > 0:
            map_set[map_num]=number_set
            map_num+=1
            number_set = []
    elif line != '':
        number_set.append([int(int_val) for int_val in line.split(' ')])
map_set[map_num]=number_set


changed_check = [True for _ in range(len(seed_numbers))]
for mapT in map_set:
    for map in range(len(mapT)):
        for seed in range(len(seed_numbers)):
            if changed_check[seed]:
                if mapT[map][1] <= seed_numbers[seed][0] < mapT[map][1] + mapT[map][2]:
                    if seed_numbers[seed][0] + seed_numbers[seed][1] < mapT[map][1] + mapT[map][2]:
                        dest = mapT[map][0] + (mapT[map][1] - seed_numbers[seed][0])
                        seed_numbers[seed] = [dest,seed_numbers[seed][1]]
                        changed_check[seed]=False
                    else:
                        dest = mapT[map][0] + (mapT[map][1] - seed_numbers[seed][0])
                        rnge = (mapT[map][1] + mapT[map][2]) - seed_numbers[seed][0]
                        seed_numbers[seed][1]-=rnge
                elif mapT[map][1] < seed_numbers[seed][0] + seed_numbers[seed][1] and seed_numbers[seed] < mapT[map][1]:
                    if seed_numbers[seed][0] + seed_numbers[seed][1] < mapT[map][1] + mapT[map][2]:
                        dest = seed_numbers[seed][1] - (mapT[map][1] - seed_numbers[seed][0])
                        rnge -= (seed_numbers[seed][1] + seed_numbers[seed][0]) - mapT[map][1]
                        seed_numbers[seed][1]-=rnge
                    else:
                        dest = mapT[map][0] + (mapT[map][1]-seed_numbers[seed][0])
                        rnge = mapT[map][1] + mapT[map][2] - seed_numbers[seed][0]
                        seed_numbers[seed][1]-=rnge
print([num[0] for num in seed_numbers])
