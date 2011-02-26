#!/usr/bin/python
#############################################################################
#  The MIT License
#  
#  Copyright (c) 2011 dtcubed 
#  
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#  
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#  
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#############################################################################
# NOTE: Major portions of the original basis for this server code were
#       obtained through public examples of TCP Server code from:
#       http://docs.python.com for Python 2.7.1. Those portions would
#       not be encumbered by any type of Copyright by "dtcubed". As time
#       goes on, it is anticipated that more customization will occur
#       in relation to this TCP Server code.
#
# TODO: Ensure that this TCP Server code is being driven over encrypted
#       communications paths before "going live" with real use. Look into
#       something like OpenSSL or TCPWrappers.
#############################################################################
import json
import os
import socket
import threading
import time
import SocketServer
from sys import argv, exit

#####
# NOTE: Play around with this handler for awhile, but consider the "streams"
# example handler if and when it becomes apparent that 1024 is not enough.
# Thinking of a file upload message type here.
#####

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.currentThread()
        response = "%s: %s" % (cur_thread.getName(), data)
        self.request.send(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    #####
    # Open the JSON config file passed in as the 1st argument and read the contents
    # into a Python dictionary object named "config".
    #####
    #config_file = file(argv[1], 'r')
    #config = json.load(config_file)
    #config_file.close()

    HOST, PORT = "localhost", 13131

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    #####
    # NOTE: Comments from original Python docs example.
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    #####
    server_thread = threading.Thread(target=server.serve_forever)
    #####
    # NOTE: Comments from original Python docs example.
    # Exit the server thread when the main thread terminates
    #####
    server_thread.setDaemon(True)
    server_thread.start()
    print "Server loop running in thread:", server_thread.getName()

    #####
    # Forever loop.
    #####
    my_counter = 0
    while True:
        my_counter += 1
        if ((my_counter % 100) == 0):
            print "Still True"
            my_counter = 0
        time.sleep(1)
    
    #####
    # server.shutdown()
    #####

#############################################################################
#############################################################################
#############################################################################
