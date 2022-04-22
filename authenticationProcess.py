import json
from decodeMessage import *
from Socket import Socket


def main():

    server = Socket(12345)
    server.initializeServer()

    while True:
        server.bindClient()

        message = server.connection.recv(1024)

        clientData = decodeMessageToObject(message)

        checkRequestData(server, clientData)

def checkRequestData(server: Socket, clientData) -> None:
    if (validateData(clientData)):
            server.connection.send(encodeResponseToBinary("sucesso"))
    else:
        print("valores incorretos")
        server.connection.send(
            encodeResponseToBinary("valores incorretos"))
        server.connection.close()

def validateData(data):
    initialCode = data["initialCode"]
    n = data["n"]

    if initialCode < 10000000:
        return False

    if n < 5000 or n > 15000:
        return False

    return True


main()
