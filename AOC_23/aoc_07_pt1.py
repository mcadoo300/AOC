import math
input_file = open('input_07.txt','r')
lines = input_file.readlines()

cards = ['A','K','Q','J','T', '9', '8','7','6','5','4','3','2']
cards = cards[::-1]
print(cards)

hands_dealt = []
for line in lines:
    line = line.strip()
    hands_dealt.append(line.split(' '))

def Count_Jokers(cards_dealt):
    count = 0
    for card in cards_dealt:
        if card == 'J':
            count += 1
    return count


def Check_five_kind(cards_dealt):
    for card in cards:
        if cards_dealt.count(card) ==5:
            return True
    return False

def Check_four_kind(cards_dealt):
    for card in cards:
        if cards_dealt.count(card) ==4:
            return True
    return False

def Check_three_kind(cards_dealt):
    for card in cards:
        if cards_dealt.count(card) ==3:
            return True
    return False

def Check_two_kind(cards_dealt):
    for card in cards:
        if cards_dealt.count(card) ==2:
            return True
    return False

def Get_high_card(cards_dealt):
    for card in cards[::-1]:
        if cards_dealt.count(card) > 0:
            return cards.index(card)
    return -1


def Check_two_pair(cards_dealt):
    pair = 0
    for card in cards:
        if cards_dealt.count(card) ==2:
            pair += 1
    if pair == 2:
        return True
    return False

five_kind = 18
four_kind = 17
full_house = 16
three_kind = 15
two_pair = 14
one_pair = 13


for hand in hands_dealt:
    if Check_five_kind(hand[0]):
        hand.append(five_kind)
    elif Check_four_kind(hand[0]):
        hand.append(four_kind)
    else:
        if Check_three_kind(hand[0]) and Check_two_kind(hand[0]):
            hand.append(full_house)
        elif Check_three_kind(hand[0]):
            hand.append(three_kind)
        elif Check_two_kind(hand[0]):
            if Check_two_pair(hand[0]):
                hand.append(two_pair)
            else:
                hand.append(one_pair)
        else:
            hand.append(-1)
            hand.append(Get_high_card(hand[0]))
#print(hands_dealt)


# cards, bid, hand_value
hands_dealt = sorted(hands_dealt, key =lambda x: x[2],reverse=True)
#print(hands_dealt)

winning_groups = []
def Convert_hand_to_ints(dealt_cards):
    int_values = []
    for card in dealt_cards:
        int_values.append(cards.index(card))
    return int_values

for i in range(18,-2,-1):
    group_i = []
    for hand in hands_dealt:
        if i == hand[2]:
            hand[0]=Convert_hand_to_ints(hand[0])
            group_i.append(hand)
    if len(group_i) > 0:
        winning_groups.append(group_i)
#print(winning_groups)

def Sort_Group_Col(group_j,col_num):
    group_j = sorted(group_j, key = lambda x: x[col_num],reverse=True)
    while   col_num < 5 and len(group_j) > 1 and group_j[0][0][col_num]  == group_j[1][0][col_num] :
        col_num += 1
        score_cap = group_j[0][0][col_num]
        i = 1
        while i < len(group_j) and group_j[i][0][col_num] == score_cap:
            i += 1
        group_j = sorted(group_j[:i], key = lambda x: sum(x[0][:col_num]),reverse=True)
        i=0
    if col_num == 5:
        pass
    group_j = group_j[0]
    return group_j


score_value = len(hands_dealt)
total = 0

for group_i in winning_groups:
    while len(group_i)> 1:
        rmvd_hands = Sort_Group_Col(group_i,0)
        best_hand = group_i.pop(group_i.index(rmvd_hands))
        total += (score_value*int(best_hand[1]))
        score_value-=1
    if len(group_i) > 0:
        rmvd_hands = Sort_Group_Col(group_i,0)
        best_hand = group_i.pop(group_i.index(rmvd_hands))
        total += (score_value*int(best_hand[1]))
        score_value-=1
print(total)