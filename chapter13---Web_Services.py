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
'''