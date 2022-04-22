import logging

class Logger:

  def __init__(self):

        # create logger
    self.logger = logging.getLogger()
    self.logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    self.ch = logging.StreamHandler()
    self.ch.setLevel(logging.DEBUG)

    # create formatter
    self.formatter = logging.Formatter("%(asctime)s - %(levelname)s : %(message)s",
                                  "%Y-%m-%d %H:%M:%S")

    # add formatter to ch
    self.ch.setFormatter(self.formatter)

    # add ch to logger
    self.logger.addHandler(self.ch)


  def info(self, message: str) -> None:
    self.logger.info(message)

  def error(self, message: str) -> None:
    self.logger.error(message)
