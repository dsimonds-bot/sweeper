# Package Import
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
from matplotlib.font_manager import FontProperties
style.use('ggplot')

from utilities import dataframe_attributes, branding_dict

# Function definitions
def make_boxplots(dataframe: pd.DataFrame):
    
    """
    This function takes a user inputted dataframe, working directory,
    and creates a visual boxplot for each numeric column in the dataframe.

    Please note this requires that the assets dir has already been made.
    
    Parameters:
    ----------
    dataframe : pd.DataFrame
        The dataframe to make the box plots off of
        
    """
    
    # Create the attributes of the dataframe
    dataframe_attribute_dict = dataframe_attributes(dataframe)
    
    # Create list of numeric columns
    dataframe_numeric_columns = list(dataframe_attribute_dict['_numeric'].columns)
    
    # Creating a spot to save the .png files
    os.mkdir('assets/boxplots')
    
    # Loop through the columns and make a boxplot asset for them
    for numeric_column_names in dataframe_numeric_columns:
        
        # Create the figure
        fig, ax = plt.subplots(figsize = (12,7));
        
        # Create the boxplot
        ax.boxplot(
            x = dataframe[numeric_column_names].values,
        );
        
        # MLS
        ax.set_title(f'Boxplot for {numeric_column_names}');
        ax.set_ylabel(numeric_column_names);
        ax.set_xlabel('');
        fig.tight_layout();
        
        # Saving the figure
        plt.savefig(f'assets/boxplots/{numeric_column_names}-boxplot.png', format = 'png');
        plt.close()

def make_histograms(dataframe: pd.DataFrame):

    """
    This function accepts a dataframe as an argument. It loops through
    the numeric columns of the dataframe, producing a histogram
    of the column and saving it in a folder within the working dir
    assets/histograms.

    Parameters:
    ----------
    dataframe : pd.DataFrame
        A dataframe to make histograms off of

    """

    # Create dataframe attributes
    dataframe_attributes_dict = dataframe_attributes(dataframe)

    # Create list of numeric columns
    dataframe_numeric_columns = list(dataframe_attributes_dict['_numeric'].columns)

    # Creating a spot to save the .png files
    os.mkdir('assets/histograms')

    # Making a dir to save the .png files
    for numeric_column_names in dataframe_numeric_columns:

        # Create the figure
        fig, ax = plt.subplots(figsize = (12,7));

        # Create the histogram
        ax.hist(
            x = dataframe[numeric_column_names].values
        );

        # MLS
        ax.set_title(f'Histogram for {numeric_column_names}');
        ax.set_ylabel('Density');
        ax.set_xlabel('Bins');

        # Saving the figure
        plt.savefig(f'assets/histograms/{numeric_column_names}-histogram.png', format = 'png');
        plt.close();

def dataframe_image(dataframe: pd.DataFrame, image_name: str):

    """
    This function accepts a dataframe and an image name as arguments, and saves
    the image of the dataframe in the users working directory under assets/dataframes.

    Parameters:
    ----------
    dataframe : pd.DataFrame
        The dataframe to represent as an image

    image_name : str
        The string of which to make the file name of the dataframe image
        <image_name>-table.png is how it will appear in assets/dataframes.
    """

    # Creating the color scheme
    colors = list(np.repeat(branding_dict['gold'], len(dataframe.columns)));

    # Building the table
    fig, ax = plt.subplots();
    ax.axis('off');
    ax.axis('tight');
    table = ax.table(
        cellText = dataframe.values,
        colLabels = dataframe.columns,
        colColours = colors,
        loc = 'center',
        rowLabels = dataframe.index
    );

    # MLS
    for (row, col), cell in table.get_celld().items():

        # Label specific settings
        if (row == 0) or (col == -1):
            cell.set_text_props(fontproperties = FontProperties(weight = 'bold'));

        # Table wide settings
        cell.set_edgecolor(branding_dict['light-blue']);
        
    # Saving results
    fig.tight_layout();
    fig.savefig(f'assets/dataframes/{image_name}-dataframe.png', format = 'png');