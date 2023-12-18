input_file = open('input_01.txt','r')
lines = input_file.readlines()

ans = 0
for line in lines:
    line = line.strip()
    num = ""
    for k in line:
        if k.isdigit():
            num +=k
            break
    for k in line[::-1]:
        if k.isdigit():
            num +=k
            break
    ans += int(num)
print(ans)
