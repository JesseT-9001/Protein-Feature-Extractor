from CustomLogger import CustomLogger
from pandas import DataFrame

logger = CustomLogger(filename=__name__)


class ProcessedProteinDataHandler:
    __slots__ = [
        "__groups", "__folds", "__names", "__sequences", "__attributes"]

    def __init__(self, groups, folds, names, sequences, attributes):
        self.__groups = groups
        self.__folds = folds
        self.__names = names
        self.__sequences = sequences
        self.__attributes = attributes

    @property
    def groups(self):
        return self.__groups

    @property
    def folds(self):
        return self.__folds

    @property
    def names(self):
        return self.__names

    @property
    def sequences(self):
        return self.__sequences

    def save_proceed_data(self, path):
        dataframe = self.__to_dataframe()
        dataframe.to_csv(path)

    def __to_dataframe(self):
        data = []
        groups = self.__groups
        folds = self.__folds
        names = self.__names
        sequences = self.__sequences
        for i in range(self.__names.size):
            temp = [groups[i], folds[i], names[i]]
            for j in range(sequences[i].size):
                temp.append(sequences[i, j])
            data.append(temp)
        columns = ['Groups', 'Folds', 'Names']
        columns.extend(self.__attributes)
        return DataFrame(data=data, columns=columns)

