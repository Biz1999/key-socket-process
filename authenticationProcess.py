import json
from decodeMessage import decodeMessageToObject

def main():
    message = b"{\"initialCode\": 10000000, \"n\": 10000}"
    
    clientData = decodeMessageToObject(message)

    if (validateData(clientData)):
        print("sucesso")

def validateData(data):
    initialCode = data["initialCode"]
    n = data["n"]

    if initialCode < 10000000: 
        return False
    
    if n < 5000  or n > 15000:
        return False
    
    return True

main()