import re

txt_digit = {
    'one': 1,
    'oneight': 8,
    'two': 2,
    'three': 3,
    'threeight': 8,
    'four': 4,
    'five': 5,
    'fiveight': 8,
    'six': 6,
    'seven': 7,
    'sevenine': 9,
    'eight': 8,
    'eightwo': 2,
    'eighthree': 3,
    'nine': 9,
    'nineight': 8
    
}

def calc_line(line):
    digits = re.findall(r'(\d{1}|one|oneight|two|three|threeight|four|five|fiveight|six|seven|sevenine|eight|eightwo|eighthree|nine|nineight)',line)
    
    if digits[0].isnumeric():
        a = int(digits[0]) * 10
    else:
        a = int(txt_digit[digits[0]]) * 10

    if digits[-1].isnumeric():
        b = int(digits[-1])
    else:
        b = int(txt_digit[digits[-1]])


    return a+b
    

test_str = 'eightwothree'
print(f'Test str = {calc_line(test_str)}')


data = open('day1/data.txt','r')
audit = open('day1/audit.txt','w')
lines = data.readlines()

total = 0

for line in lines:
     x = calc_line(line)
     audit.writelines(f'{x}\n')
     total = total+x

print(f'Answer = {total}')