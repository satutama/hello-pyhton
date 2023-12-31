# List
# A list element can be any Python object
# A list can be empty

listInAnotherlist = [1,[11,5], 2]

# Lists and definite loops - best pals
friends = ['Satria', 'Kana', 'Gwynn']
for friend in friends:
    print('Happy new year', friend)
print('done')

# strings are immutable - cannot change the content of a string - we must make a new string to make any change
# lists are mutable - we can change an element of a list using the index operator

# fruit = 'Banana'
# fruit[0] = 'b' 
# above will result type error

lotto = [2,14,2,42,5,2]
lotto[2] = 28 
# lotto = [2,14,28,42,5,2]

# How long is a list
print(len(lotto))

# Using the range function
# range function returns a list of numbers that range from zero to one less than the parameter
# we can construc an index loop using for and an integer iterator
print(range(4)) #[0,1,2,3]
print(len(friends))
print(range(len(friends))) #[0,1,2]

for i in range(len(friends)):
    friend = friends[i]
    print('Happy new year', friend)
# the same thing as the first for above

# Concatenating lists using +
a = [1,2,3]
b = [4,5,6]
c = a + b # [1,2,3,4,5,6]

# Lists slicing
# c[1:3] > [2, 3]
# c[:4] -> [1, 2, 3, 4]

# Building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
# stuff = ['book', 99]

# List methods
dir(stuff)
# ['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# Check is something in a List
'book' in stuff # True
15 in stuff # False

# List can be sorted with sort()
# built in functions that take lists as parameter len, max, min, sum

# get average with list instead of sum and count var like chapter 5
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)

# Split functions
abc = 'With three words'
stuff = abc.split()
print(stuff) # ['With', 'three', 'words']
# split breaks a string into parts and produces a list of strings

# we can access a particular word or loop through all the words
for w in stuff:
    print(w)

# When you do not specify a delimiter, multiple spaces are treated like one delimiter
# you can specify what delimiter character to use in the splitting
line = 'first;second;third'
line.split() # ['first;second;third']
line.split(';') # ['first', 'second', 'third']