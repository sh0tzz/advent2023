with open('day1.txt', 'r') as f:
  calibration_data = f.read().split()

def part1(data):
  sum = 0
  for line in data:
    value = ''
    for i in range(len(line)):
      ascii = ord(line[i])
      if (ascii >= ord('0') and ascii <= ord('9')):
        value += line[i]
        break
    for i in range(len(line)-1, -1, -1):
      ascii = ord(line[i])
      if (ascii >= ord('0') and ascii <= ord('9')):
        value += line[i]
        break
    sum += int(value)
  return sum
  
def part2(data):
  coded_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
  }
  for i in range(len(data)):
    for key in coded_digits.keys():
      if key in data[i]:
        data[i] = data[i].replace(key, f'{key}{coded_digits[key]}{key}')
  return part1(data)

print(part1(calibration_data))
print(part2(calibration_data))
