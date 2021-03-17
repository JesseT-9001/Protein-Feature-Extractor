from os import path

import CustomLogger
from Handlers.ProteinAttributeDataHandler import ProteinAttributeDataHandler
from Handlers.ProteinDataHandler import ProteinDataHandler

logger = CustomLogger.CustomLogger(filename=__name__)

data_folder = "data"
protein_data = "g_data.csv"
protein_attributes = "List of attributes and their values.csv"
features_folder = "features"

# Select property you would like to extract
PROPERTIES_TO_EXTRACT = 2


def main():
    logger.flow(message="Started Main.")

    p_data = ProteinDataHandler(filename=path.join(data_folder, protein_data))

    filename = path.join(data_folder, protein_attributes)
    p_attributes = ProteinAttributeDataHandler(filename=filename)

    attributes_values = p_attributes.get_attribute_headers()
    pp_data = p_data.covert_to_count_vector(
        attributes_values=attributes_values)

    pp_data.normalize_via_length()

    if PROPERTIES_TO_EXTRACT:
        attribute_name, attribute = p_attributes.get_attribute_values(
            PROPERTIES_TO_EXTRACT
        )
        temp = pp_data.apply_attribute(attribute_name=attribute_name,
                                       attribute=attribute)
        temp.to_csv(path.join(features_folder, f"{attribute_name}.csv"))
        temp.loc[0:, :attribute_name].to_csv(path.join(features_folder, f"{attribute_name}_only.csv"))
    else:
        for i in range(1, 56):
            attribute_name, attribute = p_attributes.get_attribute_values(i)
            temp = pp_data.apply_attribute(attribute_name=attribute_name, attribute=attribute)
            temp.to_csv(path.join(features_folder, f"{attribute_name}.csv"))


if __name__ == '__main__':
    main()
