# Web server created by John Williams, based partially on code and idea from Prof. Kevin Walsh, College of the Holy
# Cross.  Takes two command line parameters, port number and directory name.

import socket
import sys
import time

# This creates a socket, binds it, and initiates listening
def socketCreator(address, port):
    print "Creating socket 'monitor'"
    monitor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    targetAddress = ('radius.holycross.edu', 8072)
    print "Starting up on %s at port %s" % targetAddress
    print "Attempting bind..."
    monitor.bind(targetAddress)
    print "Successful Bind"
    return monitor

# this function parses the incoming request and reacts to it
def parser(incoming):
    if 'hello' in incoming and '?' not in incoming:
        print "hello! The time is ", time.time()
        print "good bye!"
    if 'hello' in incoming and '?' in incoming:
        left, right = incoming.split('?')
        name, extra = right.split(' ')
        print "hello %s, welcome to the server!  It is currently ", time.time() % extra
        print "good bye!"
    else:
        print "incorrect call."
def listener(theSocket):
    theSocket.listen(1)
    while True:
        print "Listening..."
        connection, clientAddress = theSocket.accept()
        try:
            print "Successful connection to %s" % clientAddress
            while True:
                incoming = connection.recieve(16)
                print "Received incoming data: ", incoming
                parser(incoming)

        finally:
            connection.close()
            print "connection to ", clientAddress, "killed"
            break

#main
port = sys.argv[1]
address = sys.argv[2]
sock = socketCreator(port, address)
listener(sock)