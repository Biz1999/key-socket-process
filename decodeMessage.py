import json

def decodeMessageToObject(message):
    decodedMessage = message.decode("utf-8")

    decodedMessageObject = json.loads(decodedMessage)
    
    return decodedMessageObject