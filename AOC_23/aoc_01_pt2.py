input_file = open('input_01.txt','r')
lines = input_file.readlines()
typed_digits = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,
                "seven":7,"eight":"8","nine":9}

ans = 0
for line in lines:
    line = line.strip()
    num = ""
    for k in range(len(line)):
        if line[k].isdigit():
            num +=line[k]
            break
        else:
            for i in range(3,7):
                if k + i <= len(line):
                    if typed_digits.get(line[k:k+i]) is not None:
                        num += str(typed_digits.get(line[k:k+i]))
                        break
        if len(num) == 1:
            break
    for k in range(len(line)-1,-1,-1):
        if line[k].isdigit():
            num +=line[k]
            break
        else:
            for i in range(3,7):
                if k + i <= len(line):
                    if typed_digits.get(line[k:k+i]) is not None:
                        num += str(typed_digits.get(line[k:k+i]))
                        break
        if len(num)==2:
            break
    ans += int(num)
print(ans)
