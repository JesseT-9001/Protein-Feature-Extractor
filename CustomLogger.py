"""
*******************
Custom Logger Class
*******************
"""

import logging
import numpy as np

# Sets root logging configuration.
logging.basicConfig(
    encoding='utf-8',
    filemode='w',
    filename='my_logs.log',
    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s',
    level=logging.DEBUG,
)


class CustomLogger:
    """
    I am used to log information to specific files associated with the
    module that called me. I also keep a universal log of all logged
    information.

    :param str filename: The name of the module or file used for this logger.
    :param numpy.uint8 level: The level of logging wanted

    * 0: NOTSET - Doesn't log anything.
    * 1: CRITICAL - logs only critical log calls.
    * 2: ERROR - logs error log calls and everything before it.
    * 3: INFO - logs info log calls and everything before it.
    * 4: DEBUG - logs debug log calls and everything before it.

    :ivar numpy.uint8 level: Used to set the of logging to use.
    :ivar logging.Logger logger: Local logger `object`.

    :return: Nothing
    :rtype: NoneType
    """

    #: Reserve space for writable attributes and limits addition attribute
    #: creation.
    __slots__ = ["__level", "__logger"]

    def __init__(self, filename: str, level: np.uint8 = np.uint8(4)) -> None:
        """Constructor Method."""

        # Sets local logger level
        self.__level = level

        # Sets local logger
        self.__logger = logging.getLogger(filename)

    @property
    def level(self) -> np.uint8:
        """
        I'm used to access the current logging level.

        :return: Unsigned 8 bit Integer
        :rtype: numpy.uint8
        """
        return self.__level

    @property
    def logger(self) -> logging.Logger:
        """
        I'm used to access the logger object.

        :return: Logger object.
        :rtype: object
        """
        return self.__logger

    def flow(self, message: str) -> None:
        """
        I'm used to capture the flow of your application. Eg. 'Starting
        connection'.

        :param str message: The string wanting to be logged.
        :return: Nothing
        :rtype: NoneType
        """
        # Check if current logging level passes threshold.
        if self.__level > 2:

            # Sends message to the informational portion of the local logger.
            self.__logger.info(message)

    def sanity_check(self, message: str) -> None:
        """
        I'm used to capture debugging information from your application. Eg.
        the current value of a specific variable at a specific point in the
        application state.

        :param str message: The string wanting to be logged.
        :return: Nothing
        :rtype: NoneType
        """
        # Check if current logging level passes threshold.
        if self.__level > 3:

            # Sends message to the informational portion of the local logger.
            self.__logger.debug(message)
