"""
*******************
Custom Logger Class
*******************
"""

import logging
import numpy as np
import os.path as path


class CustomLogger:
    """
    I am used to log information to specific files associated with the
    module that called me. I also keep a universal log of all logged
    information.

    :param str filename: the name of the module or file used for this logger.

    :cvar numpy.uint8 level: Class variable - Used to set the of logging to use.

    * 0: NOTSET - Doesn't log anything.
    * 1: CRITICAL - logs only critical log calls.
    * 2: ERROR - logs error log calls and everything before it.
    * 3: INFO - logs info log calls and everything before it.
    * 4: DEBUG - logs debug log calls and everything before it.

    :ivar logging.Logger __logger: Instance variable - Local logger `object`.
    :ivar logging.Logger __universal_logger: Instance variable - Universal
        logger `object`.

    :return: Nothing
    :rtype: NoneType
    """

    # Logger level 0: NOTSET, 1: CRITICAL, 2: ERROR, 3: INFO, 4: DEBUG.
    level: np.uint8 = np.uint8(4)

    #: Reserve space for writable attributes and limits addition attribute
    #: creation.
    __slots__ = ["__logger", "__universal_logger"]

    def __init__(self, filename: str) -> None:
        """Constructor Method."""

        # Logger creation based on desired file name.
        self.__logger = logging.getLogger(filename)

        # Universal logger creation.
        self.__universal_logger = logging.getLogger("Universal")

        # Creates a files handler for local file log recording.
        filename = path.join('logs', filename + '.log')
        file_handler = logging.FileHandler(filename=filename, mode='w')

        # Creates a files handler for universal log recording.
        kargs = {"filename": path.join('logs', 'Universal.log'), "mode": 'w'}
        universal_file_handler = logging.FileHandler(**kargs)

        # Formatting: Time:Level:Filename:Message
        formatting = '%(asctime)s : %(levelname)s : %(name)s : %(message)s'

        # Assigns formatting standards to formatter.
        formatter = logging.Formatter(formatting)

        # Sets the local file handler format to specified format.
        file_handler.setFormatter(formatter)

        # Sets the universal file handler format to specified format.
        universal_file_handler.setFormatter(formatter)

        # Adds local file handler to local logger.
        self.__logger.addHandler(file_handler)

        # Adds universal file handler to universal logger.
        self.__universal_logger.addHandler(universal_file_handler)

        # Sets log level for local logger.
        self.__logger.setLevel(self.get_log_level())

        # Sets log level for local logger.
        self.__universal_logger.setLevel(self.get_log_level())

    @property
    def logger(self) -> object:
        """
        I'm used to access the local logger object.

        :return: Local logger object.
        :rtype: object
        """
        return self.__logger

    @property
    def universal_logger(self) -> object:
        """
        I'm used to access the universal logger object.

        :return: Universal logger object
        :rtype: object
        """
        return self.__universal_logger

    def flow(self, message: str) -> None:
        """
        I'm used to capture the flow of your application. Eg. 'Starting
        connection'.

        :param str message: The string wanting to be logged.
        :return: Nothing
        :rtype: NoneType
        """
        # Sends message to the information section of local logger.
        self.__logger.info(message)

        # Sends message to the information section of universal logger.
        self.__universal_logger.info(message)

    def get_log_level(self) -> int:
        """
        I get the current log level object based on the class variable level.

        :return: Integer
        :rtype: int
        """
        levels = [
            logging.NOTSET,
            logging.CRITICAL,
            logging.ERROR,
            logging.INFO,
            logging.DEBUG,
        ]
        return levels[self.level.item()]

    def sanity_check(self, message: str) -> None:
        """
        I'm used to capture debugging information from your application. Eg.
        the current value of a specific variable at a specific point in the
        application state.

        :param str message: The string wanting to be logged.
        :return: Nothing
        :rtype: NoneType
        """
        # Sends message to the information section of local logger.
        self.__logger.debug(message)

        # Sends message to the information section of universal logger.
        self.__universal_logger.debug(message)
