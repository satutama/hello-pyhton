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