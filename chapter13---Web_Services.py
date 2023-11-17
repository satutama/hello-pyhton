'''
Data on the web
    . There are 2 commonly used formats: XML and JSON to represent data going between aplication and across networks
    . When we take the data from internal representation (python dictionary for example) and send it to the 'Wire', it's called serialization
    . When we receive the data from the wire, we need to deserialize it (from XML or JSON), it's called deserialization

XML - eXtensible Markup Language
    . Primary purpose is to help information systems share structured data
    . It started as a simplified subset of the standard Generalized Markup Language (SGML), and is designed to be relatively human-legible

    XML Terminology
        . Tags indicate the beginning and ending of elements
        . Attributes - Keyword/value pairs on the opening tag of XML
        . Serialize/Deserialize - convert data in one program into a common format that can be stored and/or transmitted between systems in a programming language-independent manner

    XML Basics
        . Start Tags - the difference from HTML is we get to name the tags anything we want (<person>)
        . End Tag - </person>
        . Text Content
        . Attribute
        . Self closing tag <email/>
        . Simple element (or Node) - <name>....</name>
        . Complex element - Element that has childs element
    
    XML Schema
        . Description of the legal format of an XML document
        . Expressed in terms of constraints on the structure and content of documents
        . Often used to specify a "contract" between systems - "My system will only accept XML that conforms to this particular Schema."
        . If a particular piece of XML meets the specification of the schema - it is said to validate
        . XML document and XML schema contract needs to be validated (check XML-validation image)
        . There's a number of different XML Schema languages, what we're going to focus on is XML Schema from W3C - (XSD)

    XSD XML Schema (W3C Spec)
        . We will focus on the World Wide Web Consortium (W3C) version
        . often called "W3C schema" because "Schema" is considered generic
        . More commonly it is called XSD because the file names end in .xsd

        XSD structure - *check XSD-details.jpg
            . xs:element           
            . xs:sequence           
            . xs:complexType

'''

# XML inside python example
    # data should usually come from outside
import xml.etree.ElementTree as ET
data = '''<person>
    <name>Sat</name>
    <phone type="intl">
        +31 234 56 778
     </phone>
     <email hide="yes"/>
    </person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

print("\n") # line break

#Another example
import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Sat</name>
        </user>
        <user x="8">
            <id>007</id>
            <name>Bond</name>
        </user>
    </users>
    </stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute:', item.get("x"))
