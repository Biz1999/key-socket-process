from Socket import Socket
from Logger import Logger
from decodeMessage import encodeMessageToBinary

def main():
    # TODO revisar logs para deixar na main
    initialCode, n = readInput()

    message = {"initialCode": initialCode, "n": n}

    encodedMessage = encodeMessageToBinary(message)

    createConnection(encodedMessage)

def readInput():
    initialCode = int(input("Insira o código inicial: "))
    n = int(input("Insira o valor de 'n': "))
    return initialCode, n

def createConnection(encodedMessage: bin) -> None:
    clientSocket = Socket(8000)

    clientSocket.connect()

    try:
        clientSocket.send(encodedMessage)
        messageReceived = clientSocket.recv()
        print('SERVER >> ', messageReceived)
    except:
        print('Erro na conexão...')
        clientSocket.close()
main()
