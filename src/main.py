# Package Import
import pandas as pd
import util
import assets
import data_import

def assets_build(dataframe: pd.DataFrame, save_components = False):

    # Make dataframe attributes
    dataframe_structure = data_import.loading_dock(dataframe);

    # Make the boxplots
    assets.make_boxplots(dataframe_structure.num());

    # Make the histograms
    assets.make_histograms(dataframe_structure.num());

    # Create the column-wise describe storage
    storage = util.column_describe_storage(dataframe_structure.num());

    for column_names in list(storage.keys()):
        assets.dataframe_image(storage[column_names]);

    # Making aggregate dataframe images
    assets.dataframe_image(dataframe.describe());