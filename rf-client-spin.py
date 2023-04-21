#!/usr/bin/env python3
"""PyBluez simple example rfcomm-client.py

Simple demonstration of a client application that uses RFCOMM sockets intended
for use with rfcomm-server.

Author: Albert Huang <albert@csail.mit.edu>
$Id: rfcomm-client.py 424 2006-08-24 03:35:54Z albert $
"""

import sys

import bluetooth

if __name__== "__main__":
    addr = None
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    service_matches = None
    sock = None
    if len(sys.argv) < 2:
        print("No device specified. Searching all nearby bluetooth devices for\n the SampleServer service...")
    else:
        addr = sys.argv[1]
        print("Searching for SampleServer on {}...".format(addr))

    while True:
        #Test connection
        try:
            sock.getpeername()
            connected = True
        except:
            connected = False
            sock = None
        if service_matches == None:
            service_matches = bluetooth.find_service(uuid=uuid, address=addr)
            if len(service_matches) == 0:
                service_matches = None
        elif sock == None:
            first_match = service_matches[0]
            port = first_match["port"]
            name = first_match["name"]
            host = first_match["host"]
            try:
                sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                sock.connect((host, port))
            except:
                pass
        else:
            data = "Spin"
            if not data:
                break
            try:
                sock.send(data)
            except:
                pass

    sock.close()

# search for the SampleServer service



