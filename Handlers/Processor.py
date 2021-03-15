import CustomLogger
import numpy as np
import pandas as pd
import typing

#: Local logger
logger = CustomLogger.CustomLogger(filename=__name__)

#: Typing that's a union of all the unsigned integers
any_uint = typing.Union[np.uint8, np.uint16, np.uint32, np.uint64]


class Processor:
    """
    I'm used to process a given dataframe.

    Args:
        file (pandas.DataFrame): Dataframe to work on.
    """
    #: Reserve space for writable attributes and limits addition attribute
    #: creation.
    __slots__ = ["__data"]

    def __init__(self, file: pd.DataFrame) -> None:
        """Constructor Method."""
        logger.flow(message="Created a Processor.")
        self.__data = file

    @property
    def data(self) -> pd.DataFrame:
        """
        I'm used to access the data that was read in.

        Returns:
            pandas.DataFrame: Dataframe
        """
        logger.flow(message="Accessing data")
        return self.__data

    def apply_attribute(
            self, attribute_name: str, attribute: pd.Series
    ) -> None:
        """
        I apply a given attribute series to the data currently held, sum the
        result, and adds it as a new column to the data.

        Args:
            attribute_name (str): Name of the attribute being applied.
            attribute (pandas.Series): Series of attribute to be applied.

        Returns:
            NoneType: Nothing
        """
        message = "attribute_name type is " + str(type(attribute_name))
        logger.sanity_check(message)
        logger.sanity_check("attribute type is " + str(type(attribute)))
        logger.flow(message="applying attribute")

        # localize function.
        location = self.__data.loc

        # Make a copy of current data from without attributes,
        temp = location[0:, :"A"].copy().drop(columns="A")

        # Apply attributes to current data none destructively.
        attribute_applied = location[0:, "A":] * attribute

        logger.sanity_check(message=f"Current Data:\n{self.__data}")
        logger.sanity_check(
            message=f"Data with attribute applied:\n{attribute_applied}"
        )

        # Add attribute as a column on temp dataframe.
        temp[attribute_name] = attribute_applied.sum(axis=1)

        # Add the rest of the old dataframe attributes back in.
        temp[attribute_applied.columns] = location[0:, "A":]

        # Save temp as new dataframe.
        self.__data = temp

    def normalize_via_length(self) -> None:
        """
        I normalize the data held by dividing each attribute by the length of
        the sequence.

        Returns:
            NoneType: Nothing
        """
        logger.flow(message="Normalizing data via length")

        # Get attribute headers from current dataframe.
        headers = self.__get_attribute_header()

        # localize method.
        loc = self.__data.loc

        # Grab loop column.
        length_values = loc[0:, "Length"]

        # loop through attribute column and divided each by it's length
        for attribute in headers:
            loc[0:, attribute] = loc[0:, attribute] / length_values

    def save_processed_data(self, path: str) -> None:
        """
        I save the data to a given path name.

        Args:
            path (str): The path name to save the data held.

        Returns:
            NoneType: Nothing
        """
        logger.sanity_check("path type is " + str(type(path)))
        logger.flow(message="Saving processed data")

        # Save dataframe to given path as a csv
        self.__data.to_csv(path)

    def __get_attribute_header(self) -> np.ndarray:
        """
        I get the header from the held data associated with the attributes.

        Returns:
            numpy.ndarray: Nothing
        """
        logger.flow(message="Getting attribute header")

        # localize dataframe all headers.
        columns = self.__data.columns

        # List comprehension to get a list of all column headers that
        # correspond to a single character.
        return np.array([letter for letter in columns if len(letter) == 1])
