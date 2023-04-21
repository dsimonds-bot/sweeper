# Package Import
import pandas as pd
import numpy as np
import util
import assets
import data_import

# Function Definitions
def assets_build(dataframe: pd.DataFrame):

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
    
def direct_assets_build(dataframe: pd.DataFrame):

    # Make the boxplots
    assets.make_boxplots(
        dataframe.select_dtypes(include = np.number)
    )

    # Make the histograms
    assets.make_histograms(
        dataframe.select_dtypes(include = np.number)
    )

    # Create the column-wise describe storage
    storage = util.column_describe_storage(
        dataframe.select_dtypes(include = np.number)
    )

    for column_names in list(storage.keys()):
        assets.dataframe_image(storage[column_names])

    # Making aggregate dataframe images
    assets.dataframe_image(dataframe.describe())