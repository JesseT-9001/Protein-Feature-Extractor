from CustomLogger import CustomLogger
from Handlers.ProteinDataHandler import ProteinDataHandler
from Handlers.ProteinAttributeDataHandler import ProteinAttributeDataHandler
from os import path

logger = CustomLogger(filename=__name__)

data_folder = "data"
protein_data = "g_data.csv"
protein_attributes = "List of attributes and their values.csv"
features_folder = "features"


def main():
    logger.info(item="Started Main")

    p_data = ProteinDataHandler(filename=path.join(data_folder, protein_data))

    filename = path.join(data_folder, protein_attributes)
    p_attributes = ProteinAttributeDataHandler(filename=filename)

    logger.info(item="called")

    attributes_values = p_attributes.get_all_header()
    pp_data = p_data.covert_sequences_to_count_vector(
        attributes_values=attributes_values)


    pp_data.save_proceed_data(path=path.join(features_folder, "sequence_appearance.csv"))


if __name__ == '__main__':
    main()
