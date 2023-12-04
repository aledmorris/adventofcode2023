import re

def calc_line(line):
     digits = re.findall(r'\d{1}',line)
     a = int(digits[0]) * 10
     b = int(digits[-1])
     return a+b

total = 0

data = open('day1/data.txt','r')
lines = data.readlines()

for line in lines:
     x = calc_line(line)
     total += x

print(f'Answer = {total}')