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

# Definite loops
numbers = [5,4,3,2,1]
for i in numbers:
    print(i)
print('Blastoff!')


# Loop Idioms
largest_so_far = -1
for the_num in [9, 31,42,5,1,73]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far)

print('Largest is', largest_so_far)