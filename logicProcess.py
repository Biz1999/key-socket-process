from sympy import isprime
from datetime import datetime
from Socket import Socket
from Logger import Logger
from decodeMessage import *
from threading import Thread

logger: Logger = Logger()

def main():
    server = Socket(8080)
    server.initializeServer()

    while True:
        connection, adress = server.bindClient()

        #Thread(target=initializeThread, args=(server, adress)).start()
        initializeThread(server, adress)

def initializeThread(server, adress):

    message = server.connection.recv(512)

    logger.info(f"Conexão recebida de {adress}...")

    clientData = decodeMessageToObject(message)

    logger.info(f"Gerando nova chave com objeto={clientData}...")

    key = createKey(clientData)

    logger.info(f"Chave gerada! -> [key:{key}]")

    server.connection.send(encodeResponseToBinary(key))

    server.connection.close()

    logger.info(f"Conexão fechada de {adress}...")



def createKey(clientData) -> int:
    initialCode = clientData["initialCode"]
    n = clientData["n"]

    minimumPrime = checkMinimumPrimeNumber(initialCode, n)
    maximumPrime = checkMaximumPrimeNumber(initialCode, n)

    newKey = generateKey(minimumPrime, maximumPrime)
    
    return newKey


def checkMinimumPrimeNumber(initialCode, n):
    primesCount = 0
    actualNumber = initialCode

    while(primesCount < n):
        if(isprime(actualNumber)):
            primesCount += 1
            
        actualNumber -= 1
    
    return actualNumber + 1


def checkMaximumPrimeNumber(initialCode, n):
    primesCount = 0
    actualNumber = initialCode

    while(primesCount < n):
        if(isprime(actualNumber)):
            primesCount += 1
            
        actualNumber += 1
    
    return actualNumber - 1


def generateKey(minimumPrime, maximumPrime): return minimumPrime * maximumPrime

main()
