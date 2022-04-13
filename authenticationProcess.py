import json
from decodeMessage import decodeMessageToObject

def main():
    message = b"{\"initialCode\": 10000000, \"n\": 10000}"
    
    clientData = decodeMessageToObject(message)

    if (validateData(clientData)):
        print("sucesso")

def validateData(data):
    initialCode = data["initialCode"]
    n = data["n"]

    if initialCode < 10000000: 
        return False
    
    if n < 5000  or n > 15000:
        return False
    
    return True

main()


# import socket               # Import socket module
# s = socket.socket()         # Create a socket object
# Host = '0.0.0.0' # Get local machine name
# port = 12345                # Reserve a port for your service.


# print ('Server started!')
# print ('Waiting for clients...')

# s.bind((Host, port))        # Bind to the port
# s.listen(5)                 # Now wait for client connection.
# c, addr = s.accept()     # Establish connection with client.
# print('Got connection from', addr)
# while True:
#   msg = c.recv(1024)
#   print(addr, ' >> ', msg.decode("utf-8"))
#   msg = input('SERVER >> ').encode("utf-8")
#   c.send(msg)
#   #c.close()                # Close the connection