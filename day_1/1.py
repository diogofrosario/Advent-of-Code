import sys
value = 0
file =  open('input.txt').read().strip() 
f = file.strip()
for line in f.split('\n'):
    numbers = ''.join([char for char in line if char.isdigit()])
    score = int(numbers[0] + numbers[-1])
    value += score

print(value)