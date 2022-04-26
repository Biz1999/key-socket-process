from socket import *
from Logger import Logger

logger = Logger()
class Socket:

  def __init__(self, port):
    self.server = socket(AF_INET, SOCK_STREAM)
    self.server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    self.port = port
    self.host = "0.0.0.0"

  def initializeServer(self):

    logger.info(f'{self.host}:{self.port}')
    logger.info('Esperando por clientes...')   # Establish connection with client.

    self.server.bind((self.host, self.port))
    self.server.listen(100)
  
  def bindClient(self) -> socket and tuple:
    self.connection, self.address = self.server.accept()

    return self.connection, self.address

  def connect(self):
    hostName = gethostname()
    logger.info(f'Conectando a porta {self.port}...')
    self.server.connect((hostName, self.port))

  def send(self, message) -> None:
    self.server.send(message)

  def recv(self) -> str:
    return self.server.recv(512).decode("utf-8")

  def close(self) -> None:
    return self.server.close()
