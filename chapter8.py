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