file =  open('input.txt').read().strip() 
f = file.strip()

long_numbers  = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
value = 0

for line in f.split('\n'):
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        for d, val in enumerate(long_numbers):
            if line[i:].startswith(val):
                digits.append(str(d+1))
    value += int(digits[0] + digits[-1])

print(value)