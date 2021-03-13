"""
******************
Data Handler Class
******************
"""

import CustomLogger
import pandas as pd

logger = CustomLogger.CustomLogger(filename=__name__)


class DataHandler:
    """
    I'm used to read csv data in.

    :param str filename: The filename, including the path to read from, used to
        pull desired data.

    :ivar pandas.DataFrame __data: Working data from the choosen.

    :return: Nothing
    :rtype: NoneType
    """

    #: Reserve space for writable attributes and limits addition attribute
    #: creation.
    __slots__ = ["__data"]

    def __init__(self, filename: str) -> None:
        """Constructor Method."""
        logger.flow("Created a data handler.")

        # Reads file into program.
        self.__data = pd.read_csv(filename)

    @property
    def data(self) -> pd.DataFrame:
        """
        I'm used to access the data that was read in.

        :return: Dataframe
        :rtype: pandas.DataFrame
        """
        logger.flow("Accessing data")
        return self.__data
