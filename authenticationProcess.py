import json
from decodeMessage import *
from Logger import Logger
from Socket import Socket

logger = Logger()

def main():

    server = Socket(8000)
    server.initializeServer()

    while True:
        connection, address = server.bindClient()

        message = connection.recv(512)

        logger.info(f"Conexão recebida de {address}...")

        clientData = decodeMessageToObject(message)

        logger.info(f"Validando objeto={clientData}...")

        checkRequestData(server, address, clientData)

        connection.close()

def checkRequestData(server: Socket, address: tuple, clientData) -> None:
    if (validateData(clientData)):
        logger.info(f"Objeto={clientData}, de {address} validado.")

        encodedMessage = encodeMessageToBinary(clientData)

        logger.info(f"Criando chave para {address}")

        createKeyResponse = createConnection(encodedMessage)

        logger.info(f"Chave criada para {address}. -> [key: {createKeyResponse}]")

        server.connection.send(encodeResponseToBinary(createKeyResponse))

    else:
        logger.error(f"Objeto={clientData}, de {address} com valores incorretos.")
        server.connection.send(encodeResponseToBinary("valores incorretos"))
        server.connection.close()

def validateData(data):
    initialCode = data["initialCode"]
    n = data["n"]

    if initialCode < 10000000:
        return False

    if n < 5000 or n > 15000:
        return False

    return True


def createConnection(encodedMessage: bin) -> str:
    clientSocket = Socket(8080)

    clientSocket.connect()

    try:
        clientSocket.send(encodedMessage)
        messageReceived = clientSocket.recv()
        clientSocket.close()

        logger.info(f"Fechando conexão com sucesso!")

        return messageReceived
    except:
        logger.error(f"Erro na conexão com servidor.")
        clientSocket.close()


main()
