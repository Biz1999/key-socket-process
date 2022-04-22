import socket

class Socket:

  def __init__(self, port):
    self.server = socket.socket()
    self.port = port
    self.host = "0.0.0.0"
  
  def __del__(self):
    print("Conexão fechada ;(")

  def initializeServer(self):

    print(f'{self.host}:{self.port}')
    print('Esperando por clientes...')   # Establish connection with client.

    self.server.bind((self.host, self.port))
    self.server.listen()
  
  def bindClient(self) -> socket.socket:
    self.connection, self.address = self.server.accept()

    return self.connection

  def connect(self):
    hostName = socket.gethostname()
    print('Connecting to ', hostName, self.port)
    self.server.connect((hostName, self.port))

  def send(self, message) -> None:
    self.server.send(message)

  def recv(self) -> str:
    return self.server.recv(1024).decode("utf-8")

  def close(self) -> None:
    return self.server.close()
