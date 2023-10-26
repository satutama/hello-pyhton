# Loops and Iterations

n = 5
while n > 0:
    print('Lather')
    print('Rinse')
    n = n - 1
print('Dry off!')

# breaking out of loop
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

# finishing an iteration with continue
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')