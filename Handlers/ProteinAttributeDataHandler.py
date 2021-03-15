import CustomLogger
import Handlers.DataHandler as DataHandler
import numpy as np

#: Local logger
logger = CustomLogger.CustomLogger(filename=__name__)


class ProteinAttributeDataHandler(DataHandler.DataHandler):
    """
    I'm used to read in csv data pertaining to protein attribute data.

    Inherits from :doc:`datahandler`.
    """
    def __init__(self, filename: str) -> None:
        """Constructor Method."""
        logger.flow("Created a protein attribute data handler.")
        super().__init__(filename)

    def get_attribute_headers(self) -> np.ndarray:
        """
        I get the attribute headers from the given data.

        Returns:
            numpy.ndarry: An array of attributes.
        """
        logger.flow("getting attribute headers")
        columns = self.data.columns
        return np.array([letter for letter in columns if len(letter) == 1])

    def get_attribute_values(self, value: int) -> tuple:
        """
        I get the attribute name and list of associated values associated with
        the given value - 1.

        Args:
            value (int): Row number associated with desired attribute.

        Returns:
            tuple: Attribute name and attributes
        """
        logger.sanity_check("value type is " + str(type(value)))
        logger.flow("getting attribute name and values ")
        location = self.data.loc
        return location[value - 1, "Attributes"], location[value - 1, "A":]
