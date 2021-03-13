from CustomLogger import CustomLogger
from pandas import read_csv

logger = CustomLogger(filename=__name__)


class DataHandler:
    __slots__ = ["__file"]

    def __init__(self, filename):
        logger.flow(message="Created a data handler.")
        self.__file = read_csv(filename)

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, value):
        self.__file = value

    def __str__(self):
        return self.__file.to_string()

    def __repr__(self):
        return self.__file
