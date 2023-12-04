with open('day3.txt', 'r') as f:
    data = f.read().split('\n')

def is_digit(char):
    if ord(char) >= ord('0'):
        if ord(char) <= ord('9'):
            return True
    return False

def clamp(value, min, max):
    if value > max:
        return max
    if value < min:
        return min
    return value

def is_adjacent(data, y, x_start, x_end):
    y_range_start = clamp(y-1, 0, len(data))
    y_range_end = clamp(y+2, 0, len(data))
    x_range_start = clamp(x_start-1, 0, len(data[0]))
    x_range_end = clamp(x_end+1, 0, len(data[0]))
    for i in range(y_range_start, y_range_end):
        for j in range(x_range_start, x_range_end):
            if not is_digit(data[i][j]):
                if data[i][j] != '.':
                    if data[i][j] == '*':
                        number = int(data[y][x_start:x_end])
                        if not (f'{i},{j}' in potential_gears.keys()):
                            potential_gears[f'{i},{j}'] = [1, number]
                        else:
                            potential_gears[f'{i},{j}'][0] += 1
                            potential_gears[f'{i},{j}'][1] *= number
                    return True
    return False

in_number = False
number = ''
number_start = None
parts_sum = 0
potential_gears = {}
for i in range(len(data)):
    for j in range(len(data[i])):
        if not in_number:
            if is_digit(data[i][j]):
                number_start = j
                in_number = True
                number = data[i][j]
            continue
        if in_number:
            if is_digit(data[i][j]):
                number += data[i][j]
            else:
                in_number = False
                if is_adjacent(data, i, number_start, j):
                    parts_sum += int(number)
                number = ''
    if in_number:
        in_number = False
        if is_adjacent(data, i, number_start, j):
            parts_sum += int(number)
    number = ''

gear_ratio_sum = 0
for key, value in potential_gears.items():
    if value[0] == 2:
        gear_ratio_sum += value[1]

print(parts_sum)
print(gear_ratio_sum)
