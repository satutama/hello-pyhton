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

Application Program Interface (API)
    The API itself is largely abstract in that it specifies an interface and controls the behavior of the objects specified in that interface.
    The software that provides the functionality described by an API is said to be an "implementation" of the API.
    An API is typically defined in terms of the programming language used to build an application.

'''