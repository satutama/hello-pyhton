# Reading Files

fhand = open('mbox.txt') # open(fileName, mode) mode by default is 'r' (read). Other node us 'w'(Write)
print(fhand)

# Newline character
stuff = 'Hello\nWorld'
print(stuff)
#newline is 1 character not 2

# File Handle as a sequence
# each line in the file is a string in the sequence
# sequence is an ordered set
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)