import re

data =  open('day_2/input.txt').readlines()

pattern = r'\d{1,2} green|\d{1,2} red|\d{1,2} blue'

max_red = 12
max_green = 13
max_blue = 14

value = 0

processed_data = list(map(lambda x: re.findall(pattern, x), data))

def sum_ids():
    value = 0 
    for i, game in enumerate(processed_data):
        nums_and_colors = [(int(x.split()[0]), x.split()[1]) for x in game]
        poss_or_imposs = set(list(map(lambda draw: True \
                        if 'red' == draw[1] and draw[0] <= max_red or \
                        'green' == draw[1] and draw[0] <= max_green or \
                        'blue' == draw[1] and draw[0] <= max_blue else False, nums_and_colors)))
        if False not in poss_or_imposs:
            value += (i+1)
    return value

            
# sum_ids()

power = 0
for i, game in enumerate(processed_data):
    max_draws = {}
    nums_and_colors = [(int(x.split()[0]), x.split()[1]) for x in game]
    for draw in nums_and_colors:
        match draw[1]:
            case 'red':
                try: 
                    max_draws['red'] = max(draw[0], max_draws['red'])
                except:
                    max_draws['red'] = draw[0]
            case 'green': 
                try: 
                    max_draws['green'] = max(draw[0], max_draws['green'])
                except:
                    max_draws['green'] = draw[0]
            case 'blue':
                try: 
                    max_draws['blue'] = max(draw[0], max_draws['blue'])
                except:
                    max_draws['blue'] = draw[0]
    power += max_draws['red'] * max_draws['green'] * max_draws['blue']
print(power)