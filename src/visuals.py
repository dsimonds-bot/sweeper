# Package Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns
style.use('ggplot')

from utilities import dataframe_attributes

# Function definitions
def make_boxplots(dataframe: pd.DataFrame):
    
    """
    This function takes a user inputted dataframe, working directory,
    and creates a visual boxplot for each numeric column in the dataframe.
    
    Parameters:
    ----------
    dataframe : pd.DataFrame
        The dataframe to make the box plots off of
        
    """
    
    # Create the attributes of the dataframe
    dataframe_attribute_dict = dataframe_attributes(dataframe)
    
    # Create list of numeric columns
    dataframe_numeric_columns = list(dataframe_attribute_dict['_numeric'].columns)
    
    # Loop through the columns and make a boxplot asset for them
    for numeric_column_names in dataframe_numeric_columns:
        
        # Create the figure
        fig, ax = plt.subplots(figsize = (12,7))
        
        # Create the boxplot
        ax.boxplot(
            x = dataframe[numeric_column_names].values,
        )
        
        # MLS
        ax.set_title(f'Boxplot for {numeric_column_names}')
        ax.set_ylabel(numeric_column_names)
        ax.set_xlabel('')
        
        # Saving to working directory
        boxplot_figure_filename = f'{numeric_column_names}-boxplot.png'
        plt.savefig(boxplot_figure_filename)
        plt.close()
        
        