file = open('input_10.txt')
lines = file.readlines()


cycle_check = [20,60,100,140,180,220]

cycle = 1 
ans = 0
val = 1
for line in lines:
    line = line.strip()
    line = line.split(' ')
    if line[0] == "addx":
        cycle+=1
        if cycle in cycle_check:
            ans += (val*cycle)
        val += int(line[1])
        cycle +=1 
        if cycle in cycle_check:
            ans += (val*cycle)
    else:
        cycle+=1 
        if cycle in cycle_check:
            ans += (val*cycle)
    
print(ans)
