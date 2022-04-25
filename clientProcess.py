import concurrent.futures
from asyncio import create_task
from Socket import Socket
from Logger import Logger
from decodeMessage import encodeMessageToBinary
from threading import Thread
from time import time
from random import randint

CLIENTS = 20
INITIAL_CODE = 10000000
N = 5000

logger = Logger()

def main():
    startTime = 0

    if (CLIENTS == 1):
        initialCode, n = readInput()

        startTime = time()

        startKeyCreation(initialCode, n)
    else:

        startTime = time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for i in range(CLIENTS):
                initialCode = randint(10000000, 15000000)
                n = randint(5000, 15000)
                executor.submit(startKeyCreation, INITIAL_CODE, n)

    runtime = ("%.3f" % (time() - startTime))

    logger.info(f"Tempo percorrido para {CLIENTS} cliente{'' if CLIENTS == 1 else 's'} - {runtime}s")


def startKeyCreation(initialCode, n):

    message = {"initialCode": initialCode, "n": n}

    encodedMessage = encodeMessageToBinary(message)

    logger.info(f"Enviando objeto para validação e criação. [Objeto: {message}]...")

    startTime = time()

    response = createConnection(encodedMessage)

    runtime = ("%.3f" % (time() - startTime))

    logger.info(f"[Runtime:{runtime}s] Conexão finalizada. Resposta: {response}")

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
