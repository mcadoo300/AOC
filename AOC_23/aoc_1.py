import math
import pdb
digits_list = ['1','2','3','4','5','6','7','8','9','0']
spelled_digits = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
input_file = open('input_1.txt','r')
lines = input_file.readlines()

total_sum = 0
char1 = ''
char2 = ''
for line in lines:
    print(line)
    for i in range(len(line)):
        if line[i] in digits_list:
            if char1 == '':
                print(line[i])
                char1 = line[i]
            else:
                print(line[i])
                char2 = line[i]
        else:
            possible_digits = [line[i:min(len(line)-1,i+3)],
                               line[i:min(len(line)-1,i+4)],
                               line[i:min(len(line)-1,i+5)]]
            print(possible_digits)
            for j in range(len(possible_digits)):
                if possible_digits[j] in spelled_digits:
                    if char1 == '':
                        print(spelled_digits[possible_digits[j]])
                        char1 = str(spelled_digits[possible_digits[j]])
                    else:
                        print(spelled_digits[possible_digits[j]])
                        char2 = str(spelled_digits[possible_digits[j]])

    if char1 == '' and char2 != '':
        char1= char2
    if char2 == '' and char1 != '':
        char2= char1
    calibration = int(char1+char2)
    char1=''
    char2=''
    total_sum+=calibration
print(total_sum)