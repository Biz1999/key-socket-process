from Socket import Socket
from Logger import Logger
from decodeMessage import encodeMessageToBinary

logger = Logger()

def main():
    initialCode, n = readInput()

    message = {"initialCode": initialCode, "n": n}

    encodedMessage = encodeMessageToBinary(message)

    logger.info(f"Enviando objeto para validação e criação. [Objeto: {message}]...")

    response = createConnection(encodedMessage)

    logger.info(f"Conexão finalizada. Resposta: {response}")

def readInput():
    while True:
        try:
            initialCode = int(input("Insira o código inicial: "))
            n = int(input("Insira o valor de 'n': "))
            return initialCode, n
        except:
            logger.error("Insira novamente os valores")


def createConnection(encodedMessage: bin) -> str:
    clientSocket = Socket(8000)

    clientSocket.connect()

    try:
        clientSocket.send(encodedMessage)
        response = clientSocket.recv()
        clientSocket.close()
        return response
    except:
        logger.error("f")
        clientSocket.close()
main()
