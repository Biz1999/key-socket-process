from sympy import isprime
from datetime import datetime
from Socket import Socket
from Logger import Logger
from decodeMessage import *

logger: Logger = Logger()

def main():
    server = Socket(12345)
    server.initializeServer()

    while True:
        connection = server.bindClient()

        message = server.connection.recv(1024)

        clientData = decodeMessageToObject(message)

        key = createKey(clientData)

        server.connection.send(encodeResponseToBinary(key))

        server.connection.close()


def createKey(clientData) -> int:
    initialCode = clientData["initialCode"]
    n = clientData["n"]

    logger.info(f"Gerando nova chave com objeto={clientData}...")

    minimumPrime = checkMinimumPrimeNumber(initialCode, n)
    maximumPrime = checkMaximumPrimeNumber(initialCode, n)

    newKey = generateKey(minimumPrime, maximumPrime)

    logger.info(f"Chave gerada! -> [key:{newKey}]")

    return newKey


def checkMinimumPrimeNumber(initialCode, n):
    primesCount = 0
    actualNumber = initialCode

    while(primesCount < n):
        if (actualNumber % 2 == 0):
            pass
        elif(isprime(actualNumber)):
            primesCount += 1
            
        actualNumber -= 1
    
    return actualNumber + 1


def checkMaximumPrimeNumber(initialCode, n):
    primesCount = 0
    actualNumber = initialCode

    while(primesCount < n):
        if (actualNumber % 2 == 0):
            pass
        elif(isprime(actualNumber)):
            primesCount += 1
            
        actualNumber += 1
    
    return actualNumber - 1


def generateKey(minimumPrime, maximumPrime): return minimumPrime * maximumPrime

main()
