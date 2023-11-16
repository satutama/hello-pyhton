'''
# Networking with Python
    # checkout transport control protocol for (TCP) details
     
# TCP connections / Sockets

In computer networking, an internet socket or network socket is an endpoint
of a bidirectional inter-process communication flow across an internet
Protocol-based computer network, such as the Internet.

Browser <-- Internet --> Web server

    # TCP Port Numbers
        - A port is an application-specific or process-specific software communications endpoint
        - it allows multiple networked applications to coexist on the same server
        - There is a list of well-known TCP port numbers

        Common TCP Ports
        . Telnet (23) - login
        . SSH (22) - Secure login
        . HTTP (80)
        . HTTPS (443) - secure

        
# Sockets in Python
    Python has built-in support for TCP sockets

    import socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect( ('data.pr4e.org', 80) )

    data.pr4e.org = Host, 80 = Port

# Application Protocol
    . Since TCP (and python) gives us reliable socket, what do we want to do with the socket?
    . Application Protocols
        - Mail
        - World Wide Web
    
    HTTP (HyperText Transfer Protocol) is the set of rules to allow browsers
    to retrieve web docs from servers over the internet

# typical URL 
    http://www.satutama.com/page1.htm
    http://             -> Protocol
    www.satutama.com    -> host
    page1.htm           -> document


'''

# Write a web browser

# An HTTP request in Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)     # receive 512 characters at a time
    if (len(data) < 1):         # if we get 0 characters then connection close
        break
    print(data.decode())        # we have to decode before we print
mysock.close()

'''
# Text Processing

    Representing Simple Strings
        - Each character is represented by a number between 0 - 256 stored in 8 bits of memory
        - 8 bits of memory is a 'byte' of memory (1 Terabytes is 8 Terabits)
        - the ord() function tells us the numberic value of a simpe ASCII character
    
        >>> print(ord('H')) 
        72
        >>> print(ord('e')) 
        101
        >>> print(ord('\n'))  
        10
        >>>

    Multi-Byte Characters
        . To represent the wide range of characters computers must handle how we represent characters with more than one byte
            - UTF-16 -- Fixed length - Two bytes
            - UTF-32 -- Fixed length - Four bytes
            - UTF-8  -- 1-4 bytes
                . Upwards compatible with ASCII (1byte)\
                . Automatic detection between ASCII and UTF-8
                . UTF-8 is recommended practice for encoding data to be exchanged between systems

    Pyhton3 and Unicode
        - Internally, all strings are unicode
        - Working with string variables in Python programs and reading data from files usually "just works"
        - When we talk to a network resource using sockets or talk to a database we have to encode and decode data (usually to UTF-8)

    Python Strings to byte
        . When we talk to an external resource like a network socket we sends bytes, so we need to encode python 3 strings into a given character encoding
        . When we read data from an external resource, we must decode it based on the character set so it properly represented in Python 3 as a string.

                              encode()               send()
                                -->                   -->    
             String Unicode            Bytes UTF-8          Socket (Network)
                                <--                   <--    
                              decode()               recv()

'''

# Using urllib in Python
    # Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
