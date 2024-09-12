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
rl = 5

def CalcWin(brd,nst):
    score=0
    print("nst")
    print(nst)
    for r in range(len(brd)):
        if int(brd[r]) not in nst:
            score+= int(brd[r])
    return score

stop = True
numi=0
invalid_num=[]
while stop:
    num = numbers[numi]
    invalid_num.append(int(num))
    btr = []
    for k in range(len(boards)):
        bo = boards[k][0]
        ns = boards[k][1]
        if num in bo:
            ind = bo.index(num)
            print("num %s \n ind: %s" % (num, ind))
            row = ind // rl
            print( "row %s)" % row)
            col = (ind)%rl
            print( "col %s" % col)
            ns.append([row,col,num])
            rows = [x[0] for x in ns]
            cols = [x[1] for x in ns]
            for r in rows:
                if rows.count(r) ==5:
                    #calc win
                    if len(boards)==1:
                        stop = False
                        print(ns)
                        print(CalcWin(bo,invalid_num)*int(num))
                    else:
                        if [bo,ns] in boards and k not in btr:
                            btr.append(k)
            for c in cols:
                if cols.count(c) == 5: 
                    #calc win
                    if len(boards)==1:
                        stop = False
                        print(CalcWin(bo,invalid_num)*int(num))
                    else:
                        if [bo,ns] in boards and k not in btr:
                            btr.append(k)
    for ltr in range(len(btr)):
        boards.remove(boards[btr[ltr]-ltr])
    btr=[]
    numi+=1
