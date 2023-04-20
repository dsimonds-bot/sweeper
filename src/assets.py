# Package Import
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
import io
from matplotlib.font_manager import FontProperties
from util import branding_dict

# Settings
style.use('ggplot')
matplotlib.use('Agg')

# Function definitions
def make_boxplots(dataframe: pd.DataFrame) -> dict:
    
    """
    This function takes a dataframe as an argument, and creates
    boxplots for each columns. These are then converted into a
    bytes object, and stored in a dictionary. The key-name to access
    this bytes obkect is the name of the dataframe column.
    
    Parameters:
    ----------
    dataframe: pd.DataFrame
        The dataframe to make the box plots off of
    
    Returns:
    -------
    boxplot_dict: dict
        A dictionary with the key representing the given
        column name, and the value being the bytes object
        corresponding to a boxplot for that variable. 
    """
    
    # Loop through the columns and make a boxplot asset for them
    boxplot_dict = {}
    for idx, numeric_column_names in enumerate(dataframe.columns):
        
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
        buf = io.BytesIO()
        fig.savefig(buf, format = 'jpeg');
        buf.seek(idx)
        fig_data = buf.getvalue()
        boxplot_dict[numeric_column_names] = fig_data
        buf.close()
        plt.close()
        
    return boxplot_dict

def make_histograms(dataframe: pd.DataFrame) -> dict:

    """
    This function accepts a dataframe as an argument, and creates a
    histogram for each column. It then converts that histogram into
    a bytes object, and stores it in a dictionary. The key to access
    this histogram is the column name for the corresponding pandas
    column.

    Parameters:
    ----------
    dataframe: pd.DataFrame
        A dataframe to make histograms off of
        
    Returns:
    -------
    histograms_dict: dict
        A dictionary with the key representing the given
        column name, and the value being the bytes object
        corresponding to a histogram for that variable.
    """

    # Making a dir to save the .png files
    histograms_dict = {}
    for idx, numeric_column_names in enumerate(dataframe.columns):

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
        buf = io.BytesIO()
        fig.savefig(buf, format = 'jpeg')
        buf.seek(idx)
        figs_data = buf.getvalue()
        histograms_dict[numeric_column_names] = figs_data
        buf.close()
        plt.close()
    
    return histograms_dict
        

def dataframe_image(dataframe: pd.DataFrame) -> bytes:

    """
    This function accepts a dataframe and an image name as arguments, and saves
    the image of the dataframe in the users working directory under assets/dataframes.

    Parameters:
    ----------
    dataframe : pd.DataFrame
        The dataframe to represent as an image

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
    buf = io.BytesIO()
    fig.savefig(buf, format = 'jpeg')
    buf.seek(0)
    figs_data = buf.getvalue()
    buf.close()
    plt.close()

    return figs_data
    
def make_value_counts(dataframe: pd.DataFrame) -> dict:

    """
    This function accepts a dataframe as an argument, and loops through each
    column, creating a bar chart of the population size for each distinct
    category within that column. It then coverts that bar chart into a bytes
    object, and stores it within a dictionary. This is then accessed with the
    key corresponding to the given column name. 

    Parameters:
    ----------
    dataframe: pd.DataFrame
        The dataframe to loop through
        
    Returns:
    -------
    value_counts_dict: dict
        The dictionary of value counts. Keys correspond to a given
        column name for the dataframe argument. Values are the bar
        charts for the unique values for each column
    """

    # Loop through columnd
    value_counts_dict = {}
    for idx, categorical_column_names in enumerate(dataframe.columns):

        # Identify number of distinct values
        n_distinct = len(dataframe[categorical_column_names].unique())

        # Identify number of bars to show
        n_bars = min(n_distinct, 10)

        # Make a subset of the data
        value_counts = dataframe[categorical_column_names].value_counts()

        # Make plot
        fig, ax = plt.subplots();
        
        value_counts.iloc[0:n_bars].plot(
            kind = 'barh',
            ax = ax,
            color = branding_dict['gold']
        )

        # MLS
        ax.set_title(f'Value Counts for {categorical_column_names}');
        ax.set_xlabel('Value Counts');

        # Saving figure
        buf = io.BytesIO()
        fig.savefig(buf, format = 'jpeg')
        buf.seek(idx)
        figs_data = buf.getvalue()
        value_counts_dict[categorical_column_names] = figs_data
        buf.close()
        plt.close()
        
    return value_counts_dict