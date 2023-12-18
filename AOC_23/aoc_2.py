

max_color = {"red":12,"green":13,"blue":14}

input_file = open('input_2.txt','r')
lines = input_file.readlines()
total_sum = 0
min_colors = [["red",0],["green",0],["blue",0]]
for line in lines:
    print(line)
    line = line[line.index(' ') +1:]
    print(line)
    game_id = line[:line.index(':')]
    #total_sum.append(int(game_id))
    print("game id " + str(game_id))
    line = line[line.index(':') +1:]
    print(line)
    games = []
    while ';' in line:
        games.append(line[:line.index(';')])
        line = line[line.index(';')+1:]
        print(games)
    games.append(line)
    print(games)
    for game in games:
        game = game.strip()
        while len(game) > 0:
            count = int(game[:game.index(' ')])
            print(count)
            game = game[game.index(' ')+1:]
            if ',' in game:
                color = game[:game.index(',')]
                print(count)
                print(color)
                for color2 in min_colors:
                    if color2[0] == color:
                        color2[1] = max(color2[1],count)
                #print(max_color[color])
                """if count > max_color[color]:
                    print(total_sum)
                    total_sum[-1]=0"""
                game = game[game.index(',')+1:].strip()
            else:
                color = game.strip()
                print(count)
                print(color)
                for color2 in min_colors:
                    if color2[0] == color:
                        color2[1] = max(color2[1],count)
                #print(max_color[color])
                """if count > max_color[color]:
                    print(total_sum)
                    total_sum[-1]=0"""
                game = ''
    power =1 
    for color2 in min_colors:
        power*=color2[1]
        color2[1]=0
    total_sum+=power
print(total_sum)
    