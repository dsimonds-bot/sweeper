# Package Import
import pandas as pd
import numpy as np
import os
import shutil

# Globals
branding_dict = {
    'gold' : '#946B2D',
    'dark-blue' : '#0E1A40',
    'grey' : '#5D5D5D',
    'light-blue' : '#222F5B'
}

# Function definitions
def dataframe_info_table(dataframe: pd.DataFrame) -> pd.DataFrame:
    
    """
    This function creates a dataframe info table, essentially the same as pd.Dataframe().info()
    However, the difference is the NaN values are converted to a %
    
    Parameters:
    ----------
    dataframe : pd.DataFrame
        The dataframe to produce info for
        
    Returns:
    -------
    dataframe_info : pd.DataFrame
        The summary dataframe containing:
            - Columns
            - dtype
            - nunique() values
            - NaN % of feature
    """
    
    # Creating the info dataframe
    dataframe_info = pd.DataFrame(
        data = {
            'dtypes' : dataframe.dtypes,
            'nunique' : dataframe.nunique(),
            'NaN' : round(100*(dataframe.isna().sum()/len(dataframe)),3)
        }
    ).sort_values(
        by = 'NaN',
        ascending = False
    )
    
    return dataframe_info

def mk_assets_dir():

    """
    This function makes a dir called assets in the cwd,
    and then builds the necessary subdir
    """
    if os.path.exists('assets') and os.path.isdir('assets'):
        shutil.rmtree(os.path.join(os.getcwd(), 'assets'))

    os.mkdir(os.path.join(os.getcwd(), 'assets'))
    
    for dir_names in ['boxplots', 'histograms', 'value-counts', 'dataframes']:
        
        path = os.path.join(os.getcwd(), 'assets')
        os.mkdir(os.path.join(path, dir_names))
    

def rm_dir(dirname: str):
    
    """
    This function takes a dir name in the current working directory and deletes it.
    It will also take care of all of the files saved within that directory.
    
    Parameters:
    ----------
    dirname : str
        The name of the directory we are removing
    """
    
    shutil.rmtree(os.path.join(os.getcwd(), dirname))

def easter_egg():
    class Dave:
        is_goobie = True

    if Dave.is_goobie:
        print("mehoy minoy")

def column_describe_storage(dataframe: pd.DataFrame) -> dict:

    """
    This function takes a pandas dataframe, and loops through each column.
    Within each loop, this function then stores the column name along with a simple
    pd.DataFrame.describe() method dataframe within the dictionary. 

    Parameters:
    ----------
    dataframe : pd.DataFrame
        A pandas dataframe to loop through and store results for

    Returns:
    -------
    column_describe_dict : dict
        A dictionary with each key : value pair corresponding to the 
        column name and .describe() method on that column    
    """

    # Create the storage dictionary
    column_describe_dict = {}

    # Start the loop
    for numeric_column_names in list(dataframe.columns):

        # Create the key value pair
        column_describe_dict[numeric_column_names] = pd.DataFrame(
            data = {
                numeric_column_names : dataframe[numeric_column_names].describe()
            })

    return column_describe_dict