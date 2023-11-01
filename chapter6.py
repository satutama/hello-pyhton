# Strings in Python

fruit = 'banana'
characterLength = len(fruit) # 6
letter = fruit[1] # a
# you will get python error if index beyond the end of a string

# Looping through strings - while
index = 0
while index < characterLength:
    letter = fruit[index]
    print(letter)
    index = index + 1

# Looping through strings - for
for letter in fruit:
    print(letter)
# more elegant, iteration variable is completely taken care of by the for loop

# Looping and counting
countLetterA = 0
for letter in fruit:
    if letter == 'a':
        countLetterA = countLetterA + 1
# countLetterA is 3

# Slicing strings
s = 'Monty Python'
print(s[0:4]) # Mont
print(s[6:7]) # P
print(s[6:20]) # Python
print(s[:2]) # Mo
print(s[8:]) # thon
print(s[:]) # Monty Python
# s[start from, up to but not including]
# if the second number is beyonf the end of the string, it stops at the end
# if we omit the first, it is assumed to be the begining of the string
# if we omit the second, it is assumed to be the end of the string

# Using in as a logical operator
fruit = 'banana'
'n' in fruit # True
'm' in fruit # False
'nan' in fruit # True
if 'n' in fruit:
    print('found it')
# checking one string is in another string