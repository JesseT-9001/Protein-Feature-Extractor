from CustomLogger import CustomLogger
from Handlers.DataHandler import DataHandler
from Handlers.ProcessedProteinDataHandler import ProcessedProteinDataHandler
from numpy import array, ndarray, ndenumerate, zeros

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
    def covert_sequences_to_count_vector(self, attributes_values: ndarray):
        sequence_vector = zeros([self.file.shape[0], attributes_values.size])
        groups = []
        folds = []
        names = []
        sequences = []
        for index, data_dict in self.file.iterrows():
            sequence = data_dict['Sequence']
            sequence_counted_dict = count_sequence(sequence=sequence)
            for index_, character in ndenumerate(attributes_values):
                if character not in sequence_counted_dict:
                    continue
                sequence_vector[index, index_[0]] = sequence_counted_dict[character]


            for key, value in data_dict.items():
                if key == 'Group':
                    groups.append(value)
                elif key == 'Fold':
                    folds.append(value)
                elif key == 'Name':
                    names.append(value)
                elif key == 'Sequence':
                    sequences.append(sequence_vector[index])

        groups = array(groups)
        folds = array(folds)
        names = array(names)
        sequences = array(sequences)
        ppd_handler = ProcessedProteinDataHandler(
            groups=groups,
            folds=folds,
            names=names,
            sequences=sequences,
            attributes=attributes_values)

        return ppd_handler

