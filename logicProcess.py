from sympy import isprime
from decodeMessage import decodeMessageToObject

def main():
    message = b"{\"initialCode\": 6, \"n\": 2}"
    
    clientData = decodeMessageToObject(message)
    initialCode = clientData["initialCode"]
    n = clientData["n"]

    print("rodando...")
    minimumPrime = checkMinimumPrimeNumber(initialCode, n)
    maximumPrime = checkMaximumPrimeNumber(initialCode, n)
    
    newKey = generateKey(minimumPrime, maximumPrime)

    print("Nova key:", newKey)

    



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