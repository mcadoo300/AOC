import os
import copy
input_file = open('input_19.txt','r')
lines = input_file.readlines()
lines= [line.strip() for line in lines]

rules = []
parts = []

r = True
for line in lines:
    line = line.strip()
    if len(line) == 0:
        r = False
    elif r:
        line = line.split ("{")
        new_rule = [line[0]]
        line = line[1].split(",")
        conditions = []
        for rl in line[:-1]:
            cons = rl.split(":")
            c = cons[0][0]
            d = cons[0][1]
            val = int(cons[0][2:])
            new_dest = cons[1]
            conditions.append([c,d,val,new_dest])
        conditions.append(line[-1][:-1])
        new_rule.append(conditions)
        rules.append(new_rule)
    else:
        line = line[1:-1]
        line = line.split(",")
        part = []
        for p in line:
            label = p[0]
            val = int(p[2:])
            part.append([label,val])
        parts.append(part)


fetch = {"x":0,"m":1,"a":2,"s":3}


def Get_rule_pos(id):
    for i in range(len(rules)):
        if rules[i][0] == id:
            return i
    return -1


def Process_Part_Rule(p,r):
    for _ in r[:-1]:
        val = fetch.get(_[0])
        if _[1] == "<":
            if p[val][1] < _[2]:
                return _[3]
        else:
            if p[val][1] > _[2]:
                return _[3]
    return r[-1]

ans = 0
for part in parts:
    k =Get_rule_pos("in")
    cont = True
    while cont:
        for r in rules[k][1:]:
            new_rule = Process_Part_Rule(part,r)
            if new_rule == "A":
                cont = False
                ans += sum([p[1] for p in part])
            elif new_rule == "R":
                cont = False
            else:
                k = Get_rule_pos(new_rule)
print(ans)