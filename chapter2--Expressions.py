variableRule1= 'Must start with a letter or underscore _'
variableRule2= 'Must consist of letters, numbers, and underscores'
variableRule3= 'Case Sensitive'

print(type(variableRule1))

name = input('Who are you? ')
print('Welcome', name)

# Display US floor after user input
inp = input('Europe floor? ')
usf = int(inp) + 1

print('US floor', usf)