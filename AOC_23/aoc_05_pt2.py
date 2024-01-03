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
            return [new_range], [[source[0],lower-1],[upper+1,source[1]]]
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


def Unionize(list1):
    lower_bounds = [[x[0],0] for x in list1]
    for lb in lower_bounds:
        for x in list1:
            if x[0] == lb[0]:
                lb[1] = max(x[1],lb[1])
    return lower_bounds




seeds = lines[0].strip()
seeds = seeds.split(":")[1]
seeds = seeds.split(' ')
while '' in seeds:
    seeds.remove('')
ranges = []
for i in range(0,len(seeds)-1,2):
    ranges.append([int(seeds[i]),int(seeds[i])+int(seeds[i+1])-1])

new_ranges = []
for line in lines[2:]:
    line = line.strip()
    if len(line) != 0:
        if line in new_section:
            for rng in new_ranges:
                if rng not in ranges:
                    ranges.append(rng)
            new_ranges = []
            ranges = Unionize(ranges)
        else:
            line = line.split(' ')
            new_base = int(line[0].strip())
            lower = int(line[1])
            upper = int(int(line[1]) + int(line[2]) - 1)
            num_ranges = len(ranges)
            for k in range(num_ranges):
                
                num_set = ranges.pop(0)
                base = lower
                new_set , num_set = Split_Intersection([lower,upper], num_set)
                if new_set is not None:
                    for nset in new_set:
                        nset[0] = (nset[0]-base) + new_base
                        nset[1] = (nset[1] - base) + new_base
                        if nset not in new_ranges:
                            new_ranges.append(nset)
                if num_set is not None:    
                    for st in num_set:
                        if st not in ranges:
                            ranges.append(st)
print(min(new_ranges,key=lambda x: x[0]))
print(min(ranges,key=lambda x: x[0]))
