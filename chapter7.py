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
for line in xfile:
    print(line)

# counting lines in a file
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
# print(count)

# reading the *whole* file
fhand = open('mbox.txt')
inp = fhand.read()
# print(len(inp))
# print(inp[:20])

# searching through file
fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('from:'):
        print(line)