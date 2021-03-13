from CustomLogger import CustomLogger
from pandas import DataFrame
from typing import Union
from numpy import uint8, uint16, uint32, uint64

import numpy as np

logger = CustomLogger(filename=__name__)
any_uint = Union[uint8, uint16, uint32, uint64]


class Processor:
    __slots__ = ["__file"]

    def __init__(self, file):
        logger.flow(message="Created a Processor.")
        self.__file = file

    @property
    def file(self):
        return self.__file

    def apply_attribute(self, attribute_name, attribute):
        temp = self.__file.loc[0:, :"A"].copy().drop(columns="A")
        attribute_applied = self.__file.loc[0:, "A":] * attribute
        temp[attribute_name] = attribute_applied.sum(axis=1)
        temp[attribute_applied.columns] = self.__file.loc[0:, "A":]
        self.__file = temp

    def normalize_via_length(self):
        headers = self.__get_attribute_header()
        loc = self.__file.loc
        length_values = loc[0:, "Length"]
        for attribute in headers:
            loc[0:, attribute] = loc[0:, attribute] / length_values

    def __get_attribute_header(self):
        columns = self.file.columns
        return np.array([letter for letter in columns if len(letter) == 1])

    def save_processed_data(self, path):
        self.__file.to_csv(path)
