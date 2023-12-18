input_file = open('input_02.txt','r')
lines = input_file.readlines()
#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
ans = 0
min_check = {"red":12,"green":13,"blue":14}
for line in lines:
    line = line.split(":")
    g_id = line[0]
    g_id = g_id.split(' ')[1].strip()
    games = line[1].strip()
    games = games.split(";")
    max_games = {"red":0,"green":0,"blue":0}
    for game in games:
        game = game.strip()
        game = game.split(',')
        for g in game:
            g = g.strip()
            g = g.split(' ')
            count = g[0]
            color = g[1]
            max_games.update({color:max(max_games.get(color),int(count))})
    add = True
    for color, count in min_check.items():
        if max_games.get(color) > count:
            add = False
    if add:
        ans+= int(g_id)
print(ans)
