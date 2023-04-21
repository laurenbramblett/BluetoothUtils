
"""PyBluez simple example rfcomm-server-spin.py

Simple demonstration of a server application that uses RFCOMM sockets on a Jackal.

Author: Lauren Bramblett
"""

import bluetooth
import signal

def handler(signum, frame):
    exit(0)
 
signal.signal(signal.SIGINT, handler)


if __name__=="__main__":
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", bluetooth.PORT_ANY))
    server_sock.listen(1)
    client_sock = None
    port = server_sock.getsockname()[1]
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid,
                            service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE],
                            # protocols=[bluetooth.OBEX_UUID]
                            )
    while True:
        try:
            client_sock.getpeername()
            connected = True
        except:
            print('Disconnected')  
            with open('data.txt','w') as f:
                f.write('Disconnected')
            connected = False
            print("Waiting for connection on RFCOMM channel", port)

            client_sock, client_info = server_sock.accept()
            print("Accepted connection from", client_info)

        if connected:
            try:
                data = client_sock.recv(1024)
                print("Received", data)
                with open('data.txt', 'w') as f:
                    f.write(data)
            except:
                pass
        else:
            pass

    client_sock.close()
    server_sock.close()
    print("All done.")
