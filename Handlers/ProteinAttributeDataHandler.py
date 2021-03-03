from CustomLogger import CustomLogger
from Handlers.DataHandler import DataHandler
from numpy import array, char, where

logger = CustomLogger(filename=__name__)


class ProteinAttributeDataHandler(DataHandler):
    def get_all_header(self):
        start = ord('A')
        end = ord('Z')
        header_array = self.file.columns.values.tolist()
        return array([
            title
            for title in header_array
            if len(title) == 1 and start <= ord(title) <= end
        ])
