# This is server.py file
# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Get the hostname, reserve a port on the service
host  = socket.gethostname()
print("Hostname for the server is:", host)
port = 6789
# Bind to the port
s.bind((host, port))

# Wait for the client connection
s.listen(5)
print("Listening on the port for 5 seconds")

# Try to establish a connection
while True:
    # Establish the connection with client
    c, addr = s.accept()
    print("Got connection from", addr)
    c.send(b'Thank you for connecting')
    # Close the connection
    c.close
