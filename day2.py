with open('day2.txt', 'r') as f:
  data = f.read()
  
data = data.split('\n')
for i in range(len(data)):
  data[i] = data[i][data[i].find(':')+2:]
  data[i] = data[i].split('; ')
  for j in range(len(data[i])):
    data[i][j] = data[i][j].split(', ')

for i in range(len(data)):
  for j in range(len(data[i])):
    roll = {
      'red': 0,
      'green': 0,
      'blue': 0
    }
    for color in data[i][j]:
      for key in roll.keys():
        if key in color:
          number = int(color[:color.find(' ')])
          roll[key] = number
    data[i][j] = roll

allowed_red = 12
allowed_green = 13
allowed_blue = 14
game_sum = 0

for i in range(len(data)):
  possible = True
  for roll in data[i]:
    if roll['red'] > allowed_red:
      possible = False
    if roll['green'] > allowed_green:
      possible = False
    if roll['blue'] > allowed_blue:
      possible = False
  if possible:
    game_sum += i+1

power_sum = 0
for i in range(len(data)):
  red = 0
  green = 0
  blue = 0
  for roll in data[i]:
    red = max(red, roll['red'])
    green = max(green, roll['green'])
    blue = max(blue, roll['blue'])
  power_sum += red * green * blue

print(game_sum)
print(power_sum)
