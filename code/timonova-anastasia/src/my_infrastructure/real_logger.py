import logging

from my_infrastructure.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename='matrix.log', level=logging.INFO)

    def append_messages_in_logs_list(self, message):
        self.logs_list.append(message)
        logging.info(message)
