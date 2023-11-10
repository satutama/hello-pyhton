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

# String Library
greet = 'Hello Bob'
zap = greet.lower() # hello bob
dir(greet) # gives you list of methods for strings
# these function don't modify original, instead return a new string

# Searching a string
pos = fruit.find('na') # 2
aa = fruit.find('z') # -1

# Search and Replace
nstr = greet.replace('Bob', 'Jane') # Hello Jane
nstr = greet.replace('o', 'X') # HellX BXb

# Stripping Whitespace
greet = '   Hello Bob     '
greet.lstrip() # 'Hello Bob     '
greet.rstrip() # '    Hello Bob'
greet.strip() # 'Hello Bob'

# Prefixes
line = 'Please have a nice day'
line.startswith('Please') # True
line.startswith('p') # False

# Parsing and Extracting
data = 'From stephen.marquard@uct.ac.ca Sat jan 5'
atpos = data.find('@') # 21
sppos = data.find(' ', atpos) # 31
host = data[atpos + 1 : sppos] #uct.ac.za