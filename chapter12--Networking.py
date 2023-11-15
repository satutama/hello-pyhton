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
