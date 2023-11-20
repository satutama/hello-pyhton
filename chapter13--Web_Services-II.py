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


# More complex version
import json
input = '''[
{   "id": "1",
    "x": "2",
    "name": "Sat"
},
{   "id": "2",
    "x": "3",
    "name": "Chan"
}
]'''

info = json.loads(input) 
for item in info:
    print('Name:', item["name"])
    print('Id:', item["id"])
    print('Attribute:', item["x"])


'''
Service Oriented Approach
    . Most non-trivial web applications use services
    . They use services from other applications (credit card charge, Hotel reservation system)
    . Services publish the "rules" applications must follow to make use of the service (API)

'''