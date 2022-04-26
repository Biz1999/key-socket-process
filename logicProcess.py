import concurrent.futures
from sympy import isprime
from Socket import Socket
from Logger import Logger
from decodeMessage import *

logger: Logger = Logger()

def main():
    server = Socket(8080)
    server.initializeServer()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            connection, adress = server.bindClient()
            executor.submit(initializeThread, server, connection, adress)
    # while True:
    #     connection, adress = server.bindClient()
    #     initializeThread(server, connection, adress)


def initializeThread(server, connection, adress):

    message = connection.recv(512)

    logger.info(f"Conexão recebida de {adress}...")

    clientData = decodeMessageToObject(message)

    logger.info(f"Gerando nova chave com objeto={clientData}...")

    key = createKey(clientData)

    logger.info(f"Chave gerada! -> [key:{key}] para {adress}")

    connection.send(encodeResponseToBinary(key))

    connection.close()

    logger.info(f"Conexão fechada de {adress}...")


def createKey(clientData) -> int:
    initialCode = clientData["initialCode"]
    n = clientData["n"]

    minimumPrime = checkMinimumPrimeNumber(initialCode, n)
    maximumPrime = checkMaximumPrimeNumber(initialCode, n)

    newKey = generateKey(minimumPrime, maximumPrime)

    return newKey

    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     minimumPrime = executor.submit(checkMinimumPrimeNumber, initialCode, n)
    #     maximumPrime = executor.submit(checkMaximumPrimeNumber, initialCode, n)
    #     minimumPrimeResult = minimumPrime.result()
    #     maximumPrimeResult = maximumPrime.result()
    #     # minimumPrime = checkMinimumPrimeNumber(initialCode, n)
    #     # maximumPrime = checkMaximumPrimeNumber(initialCode, n)

    #     newKey = generateKey(minimumPrimeResult, maximumPrimeResult)
        
    #     return newKey


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
