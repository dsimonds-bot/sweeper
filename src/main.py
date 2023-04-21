# Package Import
import pandas as pd
import numpy as np
import util
import assets
import data_import

# Function Definitions
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