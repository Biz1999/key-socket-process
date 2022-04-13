import socket
from decodeMessage import encodeMessageToBinary


def main():
    initialCode, n = readInput()
    
    message = {"initialCode": initialCode, "n": n}
    
    clientSocket = socket.socket()         
    host = socket.gethostname() 
    port = 12345                

    print('Connecting to ', host, port)
    clientSocket.connect((host, port))

    while True:
        clientSocket.send(encodeMessageToBinary(message))
        msg = clientSocket.recv(1024)
        print('SERVER >> ', msg.decode("utf-8"))
        #s.close                     # Close the socket when done


def readInput():
    initialCode = int(input("Insira o código inicial: "))
    n = int(input("Insira o valor de 'n': "))
    return initialCode, n

main()