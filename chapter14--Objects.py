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