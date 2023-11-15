'''
# Regular Expressions
    In computing, a regular expression, also refered as "regex" or "regexp",
    provides a concise and flexible means for matching strings of text,
    such as particular characters, words, or patterns of characters.
    A regex is written in a formal language that can be interpreted by a regular expression processor.
    Basiccally, a really clever "Wild Card" expressions for matching and parsing strings

# Regex Quick Guide
    ^         Matches the beginning of a line
    $         Matches the end of the line
    .         Matches any character
    \s        Matches whitespace
    \S        Matches any non-whitespace character
    *         Repeats a character zero or more times
    *?        Repeats a character zero or more times (non-greedy)
    +         Repeats a character one or more times
    +?        Repeats a character one or more times (non-greedy)
    [aeiou]   Matches a single character in the listed set
    [^XYZ]    Matches a single character not in the listed set
    [a-z0-9]  The set of characters can include a range
    (         Indicates where string extraction is to start
    )         Indicates where string extraction is to end

# Before you can use regular expressions in your program, you must import the library using "import re"
# You can use re.search() to see if a string matches a regex, similar to using the find() method for strings
# You can use re.findall() to extract portions of a string that match your regex, similar to a combination of find() and slicing: var[5:10]

'''
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

'''
    # Example  
        # X-Sieve: CMU.Sieve 2.3
        # X-DSPAM-Result: Innocent
        # ^X.*:
        
        # X-Plane is behind schedule: two weeks ---> If we dont want this to match then answer is below
        # ^X-\S+:

# Matching and Extracting
    # re.search() returns a True/False depending on whether the string matches the regular expression
    # if we actually want the matching strings to be extracted, we use re.findall()

    >>> import re
    >>> x = 'My 2 favorite numbers are 19 and 42'
    >>> y = re.findall('[0-9]+', x)    --> [0-9]+ is one or more digits 
    >>> print(y)
    ['2', '19', '42']
    >>> y = re.findall('[AEIOU]+',x) 
    >>> print(y)
    []

# Warning: Greedy Matching
    # The repeat characters (* and +) push outward in both directions (greedy) to match the largest possible string

    >>> import re
    >>> x = 'From: Using the : character'
    >>> y = re.findall('^F.+:', x)   
    >>> print(y)
    ['From: Using the :']
    >>>

    # Greedy means everytime there's a choice, it picks the longer one
    # In this case returning 'From: Using the :' iso 'From:'

    # ^F is first character in the match is an F
    # .+ is one or more characters
    # : is last character in the match is a :

# Non-Greedy Matching
    # The repeat characters (* and +) push outward in both directions (greedy) to match the largest possible string

    >>> import re
    >>> x = 'From: Using the : character'
    >>> y = re.findall('^F.+?:', x)   
    >>> print(y)
    ['From:']
    >>>

    # ^F is first character in the match is an F
    # .+? is one or more characters but not greedy
    # : is last character in the match is a :

# Fine-Tuning string extraction
    # You can refine the match for re.findall() and separately determine which portion of the match is to be extracted by using parentheses
    
    >>> x = 'From satria.u.s@fontys.nl Sat Jan  5 09:13:16 2008'
    >>> y = re.findall('\\S+@\\S+', x) or y = re.findall(r'\S+@\S+', x)
    >>> print(y)
    ['satria.u.s@fontys.nl']

    # \S+ is at least one non-whitespace character
    # \ is the escape character in python string literals
    # use double \\ to use \ or use a "raw string" with an r in front of the string

    # Another example
    >>> x = 'From satria.u.s@fontys.nl Sat Jan  5 09:13:16 2008'
    >>> y = re.findall(r'^From (\S+@\S+)', x)
    >>> print(y)
    ['satria.u.s@fontys.nl']

    # find string start with From
    # parentheses say start extraction and end extraction
    # that's why it returns only the email, not including the From


# String Parsing examples
    # Extracting a host name - using find and string slicing
        >>> data = 'From satria.u.s@fontys.nl Sat Jan  5 09:13:16 2008'
        >>> atpos = data.find('@')
        >>> print(atpos)
        15
        >>> sppos = data.find(' ', atpos)
        >>> print(sppos)
        25
        >>> host = data[atpos+1 : sppos] 
        >>> print(host)
        fontys.nl
    
    # Double split pattern
        >>> data = 'From satria.u.s@fontys.nl Sat Jan  5 09:13:16 2008'  
        >>> words = data.split()         
        >>> email = words[1]              -> satria.u.s@fontys.nl
        >>> pieces = email.split('@')     -> ['satria.u.s', 'fontys.nl']
        >>> print(pieces[1])
        fontys.nl

    # Regex version
        >>> import re
        >>> data = 'From satria.u.s@fontys.nl Sat Jan  5 09:13:16 2008' 
        >>> y = re.findall('@([^ ]*)', data) 
        >>> print(y)
        ['fontys.nl']

        # @([^ ]*)  --> @ means look through the string until you find an @ sign
        #           --> [^ ] match non-blank character
        #           --> * match many of them
        #           --> (....) start and end of extraction

    # Even Cooler Regex version
        >>> import re
        >>> data = 'From satria.u.s@fontys.nl Sat Jan  5 09:13:16 2008' 
        >>> y = re.findall('^From .*@([^ ]*)', data) 
        >>> print(y)
        ['fontys.nl']

        # @([^ ]*)  --> ^From is Starting at the beginning of the line, look for the string 'From'
        #           --> @ means look through the string until you find an @ sign
        #           --> [^ ] match non-blank character
        #           --> * match many of them
        #           --> (....) start and end of extraction

# Escape character
    # If you want a special regular expression character to just behave normally ( most of the time) you prefix it with '\'
    # for example if you want to find a dollar sign - \$
'''