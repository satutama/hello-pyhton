#Conditional execution & Comparison operators

x = 5
if x == 5:
    print('Equals 5')
if x > 4:
    print('Greater than 4')
if x >= 5:
    print('Greater than or equal 5')
if x < 6:
    print('Less than 6')
if x <= 5:
    print('Less than or equal 5')
if x != 6:
    print('Not equal 6')


# Increase indent after an if statement or for statement (after :)
# Maintain indent to indicate scope of the block
# Reduce indent back to indicate the end of bloc
# Blank lines are ignored - they do not affect indentation
# Comments on  a line by themselves are ignored with regard to indentation

# Nested Decisions
z = 42
if z > 1:
    print('More than one')
    if z < 100:
        print('Less than 100')
print('Nested decisions done')

# Two-way decisions
y = 4
if y > 2:
    print('More than one')
else :
    print('Less than 100')
print('Two way decisions done')

# Multiway
y = 4
if y < 2:
    print('More than one')
elif y < 10:
    print('Less than 10')
else :
    print('Less than 100')
print('multiway done')

# Try/Except structure
astr= 'Hello Sat'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)