# Package Import
import pandas as pd
import os
import utilities
import visuals
import data_import

def main(dataframe: pd.DataFrame, save_components = False):

    # Check the status of the assets dir
    if os.path.exists('assets') and os.path.isdir('assets'):
        utilities.rm_dir('assets')

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
    
    # Make dataframe images
    for column_names in list(storage.keys()):
        visuals.dataframe_image(storage[column_names], image_name = column_names)

    # Making aggregate dataframe images
    visuals.dataframe_image(df_attributes['_numeric'].describe(), image_name = 'aggregate')
    
    # Saving results or not
    if save_components == False:
        utilities.rm_dir('assets')
  
main(data_import.rawData, save_components=True)