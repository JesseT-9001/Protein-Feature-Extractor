from logging import CRITICAL, DEBUG, ERROR, FileHandler, Formatter, getLogger, \
    INFO, NOTSET


class CustomLogger:
    def __init__(self, filename):
        self.__level = 3
        self.__logger = getLogger(filename)

        # Creates a files handler for log recording
        file_handler = FileHandler(filename='logs/' + filename + '.log',
                                   mode='w')

        # Formatting: Time:Level:Filename:Message
        formatting = '%(asctime)s : %(levelname)s : %(name)s : %(message)s'

        # Assigns formatting standards to formatter
        formatter = Formatter(formatting)

        # Sets the file handler format to specified format
        file_handler.setFormatter(formatter)

        self.__logger.addHandler(file_handler)
        self.__logger.setLevel(self.get_log_level())

    def get_log_level(self):
        levels = [
            CRITICAL, ERROR, INFO, DEBUG, NOTSET
        ]
        return levels[self.__level]

    def info(self, item):
        self.__logger.info(item)



