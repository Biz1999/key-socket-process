def main():
    initialCode, n = readInput()
    
    message = {
        "initialCode": initialCode,
        "n": n
    }

    print(message)

def readInput():
    initialCode = int(input("Insira o código inicial: "))
    n = int(input("Insira o valor de 'n': "))
    return initialCode, n

main()