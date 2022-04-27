import concurrent.futures
from time import time, sleep
from random import randint
from Logger import Logger
from clientProcess import startKeyCreation


logger: Logger = Logger()

def main():
  print("*******COMUNICAÇÃO ENTRE PROCESSOS*******")

  while True:
    print("\n1 - Processo individual")
    print("2 - Processo com múltiplos clientes")
    print("Outro - Sair")
    choice = int(input("Escolha: "))

    if(choice == 1):
      executeIndividualProcess()
      sleep(1)
    elif(choice == 2):
      executeMultiThreadProcesses()
      sleep(1)
    else:
      break


def executeIndividualProcess():

  print("\nProcesso individual")

  initialCode, n = readInitialInput()

  startTime = time()

  startKeyCreation(initialCode, n)

  runtime = ("%.3f" % (time() - startTime))

  logger.info(f"Processo individual - {runtime}s")


def readInitialInput():
  while True:
    try:
      initialCode = int(input("Insira o código inicial: "))
      n = int(input("Insira o valor de 'n': "))
      return initialCode, n
    except:
      logger.error("Insira novamente os valores")

def executeMultiThreadProcesses():
  print("\nProcesso Múltiplos clientes simultâneos")

  endCode, clients = readClientsInput()
  clientsData = []

  for _ in range(clients):
    initialCode = randint(0, endCode)
    n = randint(5000, 15000)
    clientsData.append({"initialCode": initialCode, "n": n})

  countdown()
  startTime = time()

  with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(clients):
      initialCode = clientsData[i]["initialCode"]
      n = clientsData[i]["n"]
      executor.submit(startKeyCreation, initialCode, n)

  runtime = ("%.3f" % (time() - startTime))

  logger.info(f"Tempo percorrido para {clients} cliente{'' if clients == 1 else 's'} - {runtime}s")



def readClientsInput():
  while True:
    try:
      print("Os valores de n ficaram como 5000 < n < 15000")
      print("O valor gerado randomicamente pode ser menor que 10 milhões")
      endCode = int(input("Insira um valor final para o código inicial(v<500000000): "))
      clients = int(input("Número de clientes simultâneos(<100): "))

      if (endCode > 500000000 or clients > 100):
        raise ValueError()
      
      return endCode, clients
    except:
      logger.error("Insira novamente os valores")

def countdown():
  seconds = 3
  while seconds:
    print(f"{seconds}...")
    sleep(1)
    seconds -= 1

  print()

if __name__ == '__main__':
  main()
