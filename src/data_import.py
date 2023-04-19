# Package Import
import pandas as pd
import util

# Class definitions
class loading_dock:
    
    def __init__(self, dataframe: pd.DataFrame) -> None:
        
        # Assign Dataframe
        self.dataframe = dataframe
        
        # Extract attributes
        self.attributes = util.dataframe_attributes(dataframe)
        
    def cat(self) -> pd.DataFrame:
        
        """
        This method returns the categorical columns of the dataframe
        """
        
        return self.attributes['_categorical']
    
    def num(self) -> pd.DataFrame:
        
        """
        This method returns the numeric columns of the dataframe
        """
        return self.attributes['_numeric']
    
    def columns(self) -> list:
        
        """
        This method returns the columns of the dataframe
        """
        return self.attributes['_columns']
    
    def nobs(self) -> int:
        
        """
        This method returns the number of rows of the dataframe
        """
        return self.attributes['_m']
    
    def ndim(self) -> int:
        
        """
        This method returns the number of overall columns
        """
        return self.attributes['_n']