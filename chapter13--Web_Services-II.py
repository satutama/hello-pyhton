'''
JavaScript Object Notation (JSON)
    Not that XML is bad, XML is better for rich and hierarchical documents.
    Whereas JSON is best for just pulling data out of a system and moving it between 2 sytems without so much fuss.
    JSON was derived from JavaScript literal syntax.

'''

# Python process JSON example
import json
data = '''{
"name": "Sat",
"phone": {
    "type": "intl",
    "number": "+12 3456 789 987"
},
"email": {
    "hide": "yes"
}
}'''

info = json.loads(data) 
# load as json from string
# because it's a curly brace, info is a dictionary

print('Name:', info["name"])
print('Hide:', info["email"]["hide"])