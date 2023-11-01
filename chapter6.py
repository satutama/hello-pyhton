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