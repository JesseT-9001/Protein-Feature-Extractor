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
    module that called me.

    Args:
        filename (str): The name of the module or file used for this logger.
        level (numpy.uint8): The level of logging wanted

    Note:
        * 0: NOTSET - Doesn't log anything.
        * 1: CRITICAL - logs only critical log calls.
        * 2: ERROR - logs error log calls and everything before it.
        * 3: INFO - logs info log calls and everything before it.
        * 4: DEBUG - logs debug log calls and everything before it.

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

        Returns:
            numpy.uint8: Unsigned 8 bit Integer.
        """
        return self.__level

    @property
    def logger(self) -> logging.Logger:
        """
        I'm used to access the logger object.

        Returns:
            logging.Logger: Logger object.
        """
        return self.__logger

    def flow(self, message: str) -> None:
        """
        I'm used to capture the flow of your application. Eg. 'Starting
        connection'.

        Args:
            message (str): The string wanting to be logged.

        Returns:
            NoneType: Nothing
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

        Args:
            message (str): The string wanting to be logged.

        Returns:
            NoneType: Nothing
        """
        # Check if current logging level passes threshold.
        if self.__level > 3:

            # Sends message to the informational portion of the local logger.
            self.__logger.debug(message)
