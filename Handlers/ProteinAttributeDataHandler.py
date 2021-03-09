from CustomLogger import CustomLogger
from Handlers.DataHandler import DataHandler
from numpy import array, char, where
import numpy as np

logger = CustomLogger(filename=__name__)


class ProteinAttributeDataHandler(DataHandler):
    def get_attribute_headers(self):
        columns = self.file.columns
        return np.array([letter for letter in columns if len(letter) == 1])

    def get_attribute_values(self, value):
        return self.file.loc[value-1, "Attributes"], self.file.loc[value-1, "A":]
