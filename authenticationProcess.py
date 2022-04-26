import json
import concurrent.futures
from decodeMessage import *
from Logger import Logger
from Socket import Socket
from threading import Thread 

logger = Logger()

def main():

    server = Socket(8000)
    server.initializeServer()


    # while True:
    #     connection, adress = server.bindClient()
    #     initializeThread(server, connection, adress)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            connection, adress = server.bindClient()
            executor.submit(initializeThread, server, connection, adress)

def initializeThread(server, connection, address):

    message = connection.recv(512)

    logger.info(f"Conexão recebida de {address}...")

    clientData = decodeMessageToObject(message)

    logger.info(f"Validando objeto={clientData}...")

    checkRequestData(server, address, connection, clientData)


def checkRequestData(server: Socket, address: tuple, connection, clientData) -> None:
    if (validateData(clientData)):
        logger.info(f"Objeto={clientData}, de {address} validado.")

        encodedMessage = encodeMessageToBinary(clientData)

        logger.info(f"Criando chave para {address}")

        createKeyResponse = createConnection(encodedMessage)

        logger.info(f"Chave criada para {address}. -> [key: {createKeyResponse}]")

        connection.send(encodeResponseToBinary(createKeyResponse))
        connection.close()

    else:
        logger.error(f"Objeto={clientData}, de {address} com valores incorretos.")
        connection.send(encodeResponseToBinary("valores incorretos"))
        connection.close()

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
