# Web server created by John Williams, based partially on code and idea from Prof. Kevin Walsh, College of the Holy
# Cross.  Takes two command line parameters, port number and directory name.

import socket
import sys

# This creates a socket, binds it, and initiates listening
def socketCreator (port, address):
    print "Creating socket 'monitor'"
    monitor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    targetAddress = (address, port)
    print "Starting up address %s port number %d" % address, port
    print "Attempting bind..."
    monitor.bind(targetAddress)
    print "Successful Bind"
    return monitor


def listener (socket):
    while True:
