file =  open('day_2/input.txt').read().strip() 
f = file.strip()

max = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

value = 0

for line in f.split('\n'):
    counts = {
        'red': 0,
        'green': 0,
        'blue': 0,
        }
    game = line.split(': ')[1]
    game_id = int(line.split(': ')[0][5:])

    for set in game.split('; '):
        for draw in set.split(', '):
            count, color = draw.split(' ')
            counts[color] += int(count)

    values = []
    for color, count in counts.items():
        if count > max[color]:
            values.append(count > max[color])

    if True in values:
        value += game_id
            
print(value)