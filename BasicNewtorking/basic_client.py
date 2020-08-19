# This is the client.py file
# Import the socket module
import socket

# Create a socket object
s = socket.socket()

# Get the local machine hostname and reserve a 
# port on the service
host = socket.gethostname()
port = 6789
print("Hostname for the client is:", host)

s.connect((host, port))
print(s.recv(2048))

# Close the socket when done
s.close()
