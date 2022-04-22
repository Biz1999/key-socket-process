import logging

class Logger:

  def __init__(self):
    self.logger = logging.getLogger("my_logger")
    self.logger.setLevel(logging.DEBUG)
    
    if not self.logger.handlers:
      self.ch = logging.StreamHandler()
      self.ch.setLevel(logging.DEBUG)

      self.formatter = logging.Formatter("%(asctime)s.%(msecs)03d - %(levelname)s : %(message)s","%Y-%m-%d %H:%M:%S")

      self.ch.setFormatter(self.formatter)

      self.logger.addHandler(self.ch)


  def info(self, message: str) -> None:
    self.logger.info(message)

  def error(self, message: str) -> None:
    self.logger.error(message)
