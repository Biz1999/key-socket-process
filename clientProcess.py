from Socket import Socket
from decodeMessage import encodeMessageToBinary

def main():
    initialCode, n = readInput()

    message = {"initialCode": initialCode, "n": n}

    encodedMessage = encodeMessageToBinary(message)

    createConnection(encodedMessage)

def readInput():
    initialCode = int(input("Insira o código inicial: "))
    n = int(input("Insira o valor de 'n': "))
    return initialCode, n

def createConnection(encodedMessage: bin) -> None:
    clientSocket = Socket(12345)

    clientSocket.connect()

    while True:
        try:
            clientSocket.send(encodedMessage)
            messageReceived = clientSocket.recv()
            print('SERVER >> ', messageReceived)
        except:
            print('Fechando conexão...')
            clientSocket.close()
            break
main()
