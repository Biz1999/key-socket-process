import json

def decodeMessageToObject(message):
    decodedMessage = message.decode("utf-8")

    decodedMessageObject = json.loads(decodedMessage)
    
    return decodedMessageObject

def encodeMessageToBinary(clientData): return json.dumps(clientData).encode("utf-8")

def encodeResponseToBinary(message: any): return str(message).encode("utf-8")