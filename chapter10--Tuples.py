# Tuples
    # tuples are another kind of sequence that functions much like a list
    # but.. tuples are 'immutable'
    # Unlike a list, once you create a tuple, you cannot alter its content - similar to a string

names = ('satty','gwyn','kana','mory')
print(names[2])
# names[2] = 'chantal'   ----> will return traceback: 'tubple' object does not support item Assignment

# Things not to do with tuples, sort, append, reverse

t = tuple()
dir(t) # ['count', 'index']

# Tuples are more efficient
    # python does not have to build tuple structures to be modifiable, they are simpler and more efficient in terms of memory use and performance than list
    # when we are making 'temporary variables' we prefer tuples over list

# Tuples and assignment
    # We can also put a tuple on the left-hand side of an assignment statement
    # We can omit the parentheses

(x,y) = (4, 'Gwyn')
print(y) # Gwyn
(a,b) = (99, 98)
print(a) # 99

# Tuples and dictionaries
    # The items() method in dictionaries returns a list of (key, value) tuples
d = dict()
d['satty'] = 2
d['Gwyn'] = 4

for (k,v) in d.items():
    print(k,v)

# Tuples are comparable
    # The compariosn operators work with tuples and other sequences.
    # If the first item is equal, pyhton goes on to the next element, and so on, until it finds elements that differ

# (0,1,2) < (5,1,2) --> True
# (0,1,20000) < (0,3,4) --> True
# ('Jones', 'Sally') < ('Jones', 'Sam') --> True
# ('Jones', 'Sally') > ('Adams', 'Sam') --> True

# Sorting lists of tuples
    # We can teake advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
    # First we sort the dictionary by the key using the items() method and sorted() function

    # >>> d = {'a': 10, 'b': 1, 'c': 22}
    # >>> d.items()
    # dict_items([('a', 10), ('b', 1), ('c', 22)])
    # >>> sorted(d.items()) 
    # [('a', 10), ('b', 1), ('c', 22)]

    # We can do this even more directly using the built-in funtion sorted
    # that takes a sequence as a parameter and returns a sorted sequence

    # >>> d = {'a': 10, 'b': 1, 'c': 22}
    # >>> t = sorted(d.items())
    # >>> t
    # [('a', 10), ('b', 1), ('c', 22)]
    # >>> for k,v in sorted(d.items()):
    # ...   print (k,v)
    # ...   
    # a 10
    # b 1
    # c 22

# Sort by values instead of key
    # if we could construct a list of tuples of the form(value, key) we could sort by value
    # We do this with a for loop that creates a list of tuples

    # >>> c = {'a': 10, 'c': 22, 'b': 1}
    # tmp = list()
    # >>> for k,v in c.items():
    # ...     tmp.append((v,k))
    # ...
    # >>> print(tmp)
    # [(10, 'a'), (22, 'c'), (1, 'b')]
    # >>> tmp = sorted(tmp, reverse=True)
    # >>> print(tmp)
    # [(22, 'c'), (10, 'a'), (1, 'b')]