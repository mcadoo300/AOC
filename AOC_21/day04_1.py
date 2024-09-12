file = open("./input04.txt")

lines = file.readlines()

numbers = lines[0].strip().split(',')
boards = []
board = [] 
for line in lines[2:]:
    if line == '\n':
        boards.append([board,[]])
        board = []
    else:
        boardrow = [ x for x in line.strip().split(' ') if x !='']
        for _ in boardrow:
            board.append(_)
boards.append([board,[]])
print(boards)
print(numbers)
rl = 5

def CalcWin(brd,nst):
    score=0
    nst = [(x[0]*5)+x[1] for x in nst]
    for r in range(len(brd)):
        if int(r) not in nst:
            score+= int(brd[r])
    return score

stop = True
numi=0
while stop:
    num = numbers[numi]
    for bo, ns in boards:
        if num in bo:
            ind = bo.index(num)
            row = ind // rl
            col = (ind)%rl
            ns.append([row,col])
            rows = [x[0] for x in ns]
            cols = [x[1] for x in ns]
            for r in rows:
                if rows.count(r) ==5:
                    #calc win
                    print(CalcWin(bo,ns))
                    print(CalcWin(bo,ns)*int(num))
                    print(bo)
                    print(num)
                    print(ns)
                    stop = False
            for c in cols:
                if cols.count(c) == 5:
                    #calc win
                    print(CalcWin(bo,ns))
                    stop = False
                    print(CalcWin(bo,ns)*int(num))
    numi+=1
