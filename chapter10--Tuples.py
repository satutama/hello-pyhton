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
