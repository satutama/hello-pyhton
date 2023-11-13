# Regular Expressions
    # In computing, a regular expression, also refered as "regex" or "regexp",
    # provides a concise and flexible means for matching strings of text,
    # such as particular characters, words, or patterns of characters.
    # A regex is written in a formal language that can be interpreted by a regular expression processor.
    # Basiccally, a really clever "Wild Card" expressions for matching and parsing strings

# Regex Quick Guide
    # ^         Matches the beginning of a line
    # $         Matches the end of the line
    # .         Matches any character
    # \s        Matches whitespace
    # \S        Matches any non-whitespace character
    # *         Repeats a character zero or more times
    # *?        Repeats a character zero or more times (non-greedy)
    # +         Repeats a character one or more times
    # +?        Repeats a character one or more times (non-greedy)
    # [aeiou]   Matches a single character in the listed set
    # [^XYZ]    Matches a single character not in the listed set
    # [a-z0-9]  The set of characters can include a range
    # (         Indicates where string extraction is to start
    # )         Indicates where string extraction is to end

# Before you can use regular expressions in your program, you must import the library using "import re"
# You can use re.search() to see if a string matches a regex, similar to using the find() method for strings
# You can use re.findall() to extract portions of a string that match your regex, similar to a combination of find() and slicing: var[5:10]

# Using re.search() like find()
    # 2 examples below are the same, but the latter use re module
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if line.find('from:') >=0:
        print(line)

import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('from:', line):
        print(line)

# Using re.search() like startswith()
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('from:'):
        print(line)

import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^from:', line):
        print(line)

# Example  
    # X-Sieve: CMU.Sieve 2.3
    # X-DSPAM-Result: Innocent
    # ^X.*:
    
    # X-Plane is behind schedule: two weeks ---> If we dont want this to match then answer is below
    # ^X-\S+:
