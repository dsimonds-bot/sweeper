# Package Import
import pandas as pd
import os
import util
import assets
import data_import

def assets_build(dataframe: pd.DataFrame, save_components = False):

    # Make a new assets dir
    util.mk_assets_dir()

    # Make dataframe attributes
    dataframe_structure = data_import.loading_dock(dataframe)

    # Make the boxplots
    assets.make_boxplots(dataframe_structure.num())

    # Make the histograms
    assets.make_histograms(dataframe_structure.num())

    # Create the column-wise describe storage
    storage = util.column_describe_storage(dataframe_structure.num())

    for column_names in list(storage.keys()):
        assets.dataframe_image(storage[column_names], image_name = column_names)

    # Making aggregate dataframe images
    assets.dataframe_image(dataframe.describe(), image_name = 'aggregate')