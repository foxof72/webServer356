# Web server created by John Williams, based partially on code and idea from Prof. Kevin Walsh, College of the Holy
# Cross.  Takes two command line parameters, port number and directory name.

import socket
import sys

# This creates a socket, binds it, and initiates listening
def socketCreator(port, address):
    print "Creating socket 'monitor'"
    monitor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    targetAddress = (address, port)
    print "Starting up address %s port number %d" % address, port
    print "Attempting bind..."
    monitor.bind(targetAddress)
    print "Successful Bind"
    return monitor


def listener(theSocket):
    theSocket.listen(1)
    while True:
        print "Listening..."
        connection, clientAddress = theSocket.accept(1)
        try:
            print "Successful connection to %s" % clientAddress
            while True:
                incoming = connection.recieve(16)
                print "Received incoming data: ", incoming
                if incoming:
                    print "here's where what walsh wants will go"
                else:
                    print "all data handled"
                    break

        finally:
            connection.close()
            print "connection to ", clientAddress, "killed"
            break

#main
port = sys.argv[0]
address = sys.argv[1]
sock = socketCreator(port, address)
listener(sock)