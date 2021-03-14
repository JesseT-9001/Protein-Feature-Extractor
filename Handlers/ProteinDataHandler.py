"""
**************************
Protein Data Handler Class
**************************
"""
import CustomLogger
import Handlers.Processor as Processor
import Handlers.DataHandler as DataHandler
import numpy as np


#: Local logger
logger = CustomLogger.CustomLogger(filename=__name__)


def count_sequence(sequence: str):
    """
    I count the number of times a character is seen in a sequence.

    Args:
        sequence (str): Protein sequence.

    Returns:
        dict: Dictionary with the keys being a character found in the given
        sequence and the value being the number of time it was seen.
    """
    logger.flow("Counting sequence")

    # Initializes empty dictionary.
    count = {}

    # Loops through sequence
    for character in sequence:

        # If the character is in the dictionary add 1 to it's count.
        if character in count:
            count[character] += 1

        # Else add the character to the dictionary and initializing it's count
        # to 1.
        else:
            count[character] = 1

    return count


class ProteinDataHandler(DataHandler.DataHandler):
    """
    I'm used to read in csv data pertaining to protein data.

    Inherits from :doc:`datahandler`
    """
    def __init__(self, filename: str) -> None:
        """Constructor Method."""
        logger.flow("Created a protein data handler.")
        super().__init__(filename)

    def covert_sequences_to_count_vector(
            self, attributes_values: np.ndarray
    ) -> Processor.Processor:
        """
        I convert a sequence to a count vector based on attributes given.

        Args:
            attributes_values (numpy.ndarray): List of attributes to use to
            convert file to.

        Returns:
            Processor.Processor: A processor object containing processed data.
        """
        logger.flow("Converting sequences into vector of attribute appearance.")

        # Localize needed variables.
        data = self.data

        # Creates new file to hold processed table.
        processed_file = data.drop(columns='Sequence')

        # Add length column to dataframe.
        processed_file["Length"] = 0.0

        # Add attributes column to dataframe.
        processed_file[attributes_values] = 0.0

        # Moving method call to local variable for loop.
        location = processed_file.loc

        # Convert attribute_value ndarry to list.
        attributes_values_list = attributes_values.tolist()

        # Loop through dataframe rows.
        for index, data_dict in data.iterrows():

            # Get sequence from dataframe.
            sequence = data_dict['Sequence']

            # Count the number of times a character appears in the sequence.
            sequence_counted_dict = count_sequence(sequence=sequence)

            total_length = 0

            # Loop through given attribute list.
            for character in attributes_values_list:

                # If the attribute is not in count dictionary, then skip loop.
                if character not in sequence_counted_dict:
                    continue

                # Write attribute count to associated spot in dataframe.
                location[index, character] = sequence_counted_dict[character]

                # Count the total number of character seen.
                total_length += sequence_counted_dict[character]

            # Added total lenght value to correct location.
            location[index, "Length"] = total_length

        return Processor.Processor(file=processed_file)


