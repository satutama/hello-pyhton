# Pyhton dictionaries

# What is a Collection
    # we can put more than one value in it and carry them all around in one convenient package
    # we have a bunch of values in a single 'variable'
    # we do this by having more than one place 'in' the variable
    # we have ways of finding the different places in the variable 

# List is a linear collection of values that stay in order
# Lists index their entries based on the position in the list
# Dictionary is a 'bag'of values, each with its own label
# Dictionaries are like bag - no order. So we index the thintgs we put in dictionary with a 'lookup tag'
# Dictionaries are like lists except that they use keys intead of numbers to look up values

# Dictionaries are python's most powerful data collection
# Dictionaries allow us to do fast database-like opration in Python
# Dictionaries have different names in different languages
    # Associative Arrays - Perl/PHP
    # Properties or Map or HashMap - Java
    # Property Bag  C# / .Net

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse) # {'money': 12, 'candy': 3, 'tissues': 75}
print(purse['candy']) # 3
purse['candy'] = purse['candy'] + 2
print(purse) # {'money': 12, 'candy': 5, 'tissues': 75}

# Dictionary Literals (Constants)
    # use curly braces and have a list of key: value pairs
    # you can make an empty dictionary using empty curly braces

jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
ooo = {} 

# Dictionary tracebacks
    # it is an error to reference a key which is not in the dictionary
    # we can use the in operator to see if a key is in the dictionary

    # >>> ccc = dict()
    # >>> print(ccc['csev']) 
    # Traceback (most recent call last):
    #   File "<stdin>", ine 1 in <module>
    #   KeyError: 'csev'
    # >>> 'csev' in ccc
    # False
    
# Most common name
counts = dict()
names = ['satty','gwyn','kana','mory','satty','satty','satty','gwyn','kana','mory']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts) 

# The get method for dictionaries
if name in counts:
    x = counts[name]
else:
    x = 0

# four lines above is equal as one line below
x = counts.get(name, 0) # 0 is default

# Simplified counting with get()
counts = dict()
names = ['satty','gwyn','kana','mory','satty','satty','satty','gwyn','kana','mory']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# Counting words in text
counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words:', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts:', counts)

# Definite loops and dictionaries
for key in counts:
    print(key, counts[key])

# Retrieving lists of keys and values
    # You can get a list of keys, values, or items(both) from a dictionary
    # list(counts), counts.keys() and counts.values()