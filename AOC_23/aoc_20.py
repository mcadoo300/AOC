import os
import copy
input_file = open('input_20.txt','r')
lines = input_file.readlines()
lines= [line.strip() for line in lines]

modules = [[] for _ in range(len(lines))]
lookup = {}
def Get_Destinations(dest):
    return [seg.strip() for seg in dest.split(",")]


def Flipflop(index,pulse):
    if pulse == "low":
        if modules[index][1] is False:
            modules[index][1] = True
            return True, "high" , modules[index][-1]
        else:
            modules[index][1] = False
            return True, "low" , modules[index][-1]
    else:
        return False, "none" , modules[index][-1]


def Conjunction(index,pulse,input):
    modules[index][1].update({input:pulse})
    if "low" in modules[index][1].values():
        return "high" , modules[index][-1]
    else:
        return "low" , modules[index][-1]


for l in range(len(lines)):
    line = [seg.strip() for seg in lines[l].split("->")]
    # prefix , label, destination
    if line[0] != "broadcaster":
        if line[0][0] == "%":
            modules[l] = [line[0][0], False, line[0][1:] , Get_Destinations(line[1])]
        else:
            modules[l] = [line[0][0], {}, line[0][1:] , Get_Destinations(line[1])]
        lookup.update({line[0][1:]:l})
    else:
        modules[l] = [-1, line[0] , Get_Destinations(line[1])]
        lookup.update({line[0]:l})
    

original = []
for _ in modules[lookup.get("broadcaster")][-1]:
    original.append(["broadcaster" , _, "low"])

for mod in modules:
    for d in mod[-1]:
        #if d != "output":
        index = lookup.get(d)
        if index is not None:
            if modules[index][0] == "&":
                Conjunction(index,"low",mod[2])

low = 0
high = 0

not_done = True
k =0
while not_done:
    signal_q = copy.deepcopy(original)
    low += len(signal_q) +1
    prev_insert = 0
    low_sig_count =0 
    while len(signal_q) > 0:
        src, dest, plse = signal_q.pop(0)
        next_index = lookup.get(dest)
        prev_insert = max(0, prev_insert-1)
        if modules[next_index][0] == "%":
            cont , pls, dests = Flipflop(next_index,plse)
            if cont:
                for i in range(len(dests)):
                    if pls == "low":
                        low +=1
                    else:
                        high +=1
                    if lookup.get(dests[i]) is not None:
                        signal_q.insert(prev_insert+i,[dest, dests[i],pls])
                    else:
                        if pls == "low":
                            low_sig_count+=1
                prev_insert = len(dests)

        else:
            pls, dests = Conjunction(next_index,plse,src)
            for i in range(len(dests)):
                if pls == "low":
                    low +=1
                else:
                    high +=1
                if lookup.get(dests[i]) is not None:
                    signal_q.insert(prev_insert+i,[dest, dests[i],pls])
                else:
                    if pls == "low":
                        low_sig_count+=1
            prev_insert = len(dests)
    k += 1
    if low_sig_count == 1:
        not_done = False
print(k)