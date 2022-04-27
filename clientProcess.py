import concurrent.futures
from asyncio import create_task
from Socket import Socket
from Logger import Logger
from decodeMessage import encodeMessageToBinary
from threading import Thread
from time import time
from random import randint

logger = Logger()

def startKeyCreation(initialCode, n):

    message = {"initialCode": initialCode, "n": n}

    encodedMessage = encodeMessageToBinary(message)

    logger.info(f"Enviando objeto para validação e criação. [Objeto: {message}]...")

    startTime = time()

    response = createConnection(encodedMessage)

    runtime = ("%.3f" % (time() - startTime))

    logger.info(f"[Runtime:{runtime}s] Conexão finalizada. Resposta: {response}")


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

