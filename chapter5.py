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

smallest_so_far = 1000
for the_num in [200, 31,42,5,1,73]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far)

print('smallest is', smallest_so_far)

# Counting in a loop
zork = 0
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)

# Summing in a loop
zork = 0
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)