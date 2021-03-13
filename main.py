from CustomLogger import CustomLogger
from Handlers.ProteinDataHandler import ProteinDataHandler
from Handlers.ProteinAttributeDataHandler import ProteinAttributeDataHandler
from os import path

import CustomLogger as CustomLogger

logger = CustomLogger.CustomLogger(filename=__name__)

data_folder = "data"
protein_data = "g_data.csv"
protein_attributes = "List of attributes and their values.csv"
features_folder = "features"


def main():
    logger.flow(message="Started Main.")

    p_data = ProteinDataHandler(filename=path.join(data_folder, protein_data))

    filename = path.join(data_folder, protein_attributes)
    p_attributes = ProteinAttributeDataHandler(filename=filename)

    attributes_values = p_attributes.get_attribute_headers()
    pp_data = p_data.covert_sequences_to_count_vector(
        attributes_values=attributes_values)

    pp_data.normalize_via_length()

    for i in range(1, 56):
        attribute_name, attribute = p_attributes.get_attribute_values(i)
        pp_data.apply_attribute(attribute_name=attribute_name, attribute=attribute)

    pp_data.save_processed_data(path=path.join(features_folder, "features_extracted.csv"))


if __name__ == '__main__':
    main()
