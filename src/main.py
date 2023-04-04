# Package Import
import pandas as pd
import os

import utilities
import visuals

def main(dataframe: pd.DataFrame, save_components = False):

    # Make a new assets dir
    utilities.mk_assets_dir()

    # Make dataframe attributes
    df_attributes = utilities.dataframe_attributes(dataframe)

    # Make the boxplots
    visuals.make_boxplots(df_attributes['_numeric'])

    # Make the histograms
    visuals.make_histograms(df_attributes['_numeric'])

    # Create the column-wise describe storage
    storage = utilities.column_describe_storage(df_attributes['_numeric'])

    # Save visuals of dataframes
    os.mkdir('assets/dataframes')

    for column_names in list(storage.keys()):
        visuals.dataframe_image(storage[column_names], image_name = column_names)

    visuals.dataframe_image(df_attributes['_numeric'].describe(), image_name = 'aggregate')