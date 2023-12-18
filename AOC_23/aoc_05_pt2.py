input_file = open('input_05.txt','r')
lines = input_file.readlines()

new_section = ["seed-to-soil map:","soil-to-fertilizer map:","fertilizer-to-water map:",
               "water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:"]


def Split_Intersection(range1,source):
    lower = max(range1[0],source[0])
    upper = min(range1[1],source[1])
    if lower > upper:
        return None , [source]
    else:
        new_range = [lower,upper]
        if new_range == range1:
            return [new_range], [[source[2][0],lower-1],[upper+1,source[1]]]
        elif new_range == source:
            return [new_range], None
        else:
            if lower == range1[0]:
                range1[0]=upper+1
            else:
                source[0]=upper+1
            if upper == range1[1]:
                range1[1] = lower-1
            else:
                source[1] = lower-1
            return [new_range], [source]

seeds = lines[0].strip()
seeds = seeds.split(":")[1]
seeds = seeds.split(' ')
while '' in seeds:
    seeds.remove('')
print(seeds)
ranges = []
for i in range(0,len(seeds)-1,2):
    ranges.append([int(seeds[i]),int(seeds[i])+int(seeds[i+1])-1])

new_ranges = []
for line in lines[2:]:
    line = line.strip()
    if len(line) != 0:
        if line in new_section:
            for rng in new_ranges:
                ranges.append(rng)
            new_ranges = []
        else:
            line = line.split(' ')
            lower = int(line[1])
            upper = int(int(line[1]) + int(line[2]) - 1)
            num_ranges = len(ranges)
            for k in range(num_ranges):
                num_set = ranges.pop(0)
                print(lower)
                print(upper)
                print(num_set)
                new_set , num_set = Split_Intersection([lower,upper], num_set)
                print(num_set)
                print(new_set)
                if new_set is not None:
                    for nset in new_set:
                        new_ranges.append(nset)
                if num_set is not None:    
                    for st in num_set:
                        ranges.append(st)

print(new_ranges)
print(ranges)
