'''
Python Objects

    Object Oriented
        . A program is made up of many cooperating objects
        . Instead of being the "whole program"- each object is a little "island" withing the program and cooperatively working with oter objects
        . A program is made up of one or more objects working together - objects make use of each other's capability

    Object
        . An object is a bit of self-contained Code and Data
        . A key aspect of the Object approach is to break the problem into smaller understandable parts (divide and conquer)
        . Objects have boundaries that allow is to ignore un-needed detail
        . We have been using objects all along: String Objects, Integer Objects, Dictionary Objects, List Objects...

    Definitions
        . Class - a template - Dog
        . Method or Message - A defined capability of a class - bark()
        . Field or attribute - A bit of data in a class - length
        . Object or Instance - A particular instance of a class - Lassie
'''

# Sample code
class PartyAnimal:                  # this is the template for making PartyAnimal objects
    x = 0                           # each party animal has a bit of data

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()                  # construct a PartyAnimal object and store in an

an.party()                          # short version of this syntax => PartyAnimal.party(an)
an.party()
an.party()

'''
Playing with dir() and type()

    A Nerdy way to find capabilities

    >>> x = list()
    >>> type(x)    
    <class 'list'>
    >>> dir(x)
    ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
    'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    >>>

        . the dir() command lists capabilities
        . Ignore the ones with underscores - these are used by Python itself
        . The rest are real operations that the object can perform
        . It is like type() - it tells us something *about* a variable

    Try dir() with a String

    >>> y = "hello string"
    >>> dir(y)
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
      'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    >>>

    print(type(an))  --> <class '__main__.PartyAnimal'>
    print(dir(an))   --> ['__class__', ... , 'party', 'x']
'''