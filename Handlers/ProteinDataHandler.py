"""
**************************
Protein Data Handler Class
**************************
"""

from CustomLogger import CustomLogger
from Handlers.DataHandler import DataHandler
from Handlers.Processor import Processor

logger = CustomLogger(filename=__name__)


def count_sequence(sequence):
    count = {}
    for character in sequence:
        if character in count:
            count[character] += 1
        else:
            count[character] = 1

    return count


class ProteinDataHandler(DataHandler):
    def covert_sequences_to_count_vector(self, attributes_values):
        processed_file = self.data.drop(columns='Sequence')
        processed_file["Length"] = 0.0
        processed_file[attributes_values] = 0.0

        location = processed_file.loc
        attributes_values_list = attributes_values.tolist()
        for index, data_dict in self.data.iterrows():
            sequence = data_dict['Sequence']
            sequence_counted_dict = count_sequence(sequence=sequence)
            for character in attributes_values_list:
                if character not in sequence_counted_dict:
                    continue

                location[index, character] = sequence_counted_dict[character]
            location[index, "Length"] = location[index, "A":].sum()

        return Processor(file=processed_file)


