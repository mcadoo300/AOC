file = open('input_10.txt')
lines = file.readlines()


cycle_check = [40,80,120,160,200]


crt = [["#" for _ in range(40)] for r in range(6)]

rw = ""

cur_row = 0
cycle = 1 
val = 1
for line in lines:
    line = line.strip()
    line = line.split(' ')
    if line[0] == "addx":
        if val-1 <= ((cycle-1)%40) <= val+1:
            crt[cur_row][(cycle-1)%40] = "#"
        else:
            crt[cur_row][(cycle-1)%40] = "."
        cycle+=1
        if cycle in cycle_check:
            cur_row +=1

        if val-1 <= ((cycle-1)%40) <= val+1:
            crt[cur_row][(cycle-1)%40] = "#"
        else:
            crt[cur_row][(cycle-1)%40] = "."
        val += int(line[1])
        cycle +=1 
        if cycle in cycle_check:
            cur_row +=1
    else:
        if val-1 <= ((cycle-1)%40) <= val+1:
            crt[cur_row][(cycle-1)%40] = "#"
        else:
            crt[cur_row][(cycle-1)%40] = "."
        cycle+=1 
        if cycle in cycle_check:
            cur_row +=1 
for l in crt:
    rw=""
    for c in l:
        rw += c    
    print(rw)
