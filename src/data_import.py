# Package Import
import pandas as pd
import numpy as np

# Class definitions
class loading_dock:
    
    def __init__(self, dataframe: pd.DataFrame) -> None:
        
        # Assign Dataframe
        self.dataframe = dataframe
        
    def cat(self) -> pd.DataFrame:
        
        """
        This method returns the categorical columns of the dataframe
        """
        
        return self.dataframe.select_dtypes(include = object)
    
    def num(self) -> pd.DataFrame:
        
        """
        This method returns the numeric columns of the dataframe
        """
        return self.dataframe.select_dtypes(include = np.number)
    
    def columns(self) -> list:
        
        """
        This method returns the columns of the dataframe
        """
        return self.dataframe.columns
    
    def nobs(self) -> int:
        
        """
        This method returns the number of rows of the dataframe
        """
        return self.dataframe.shape[0]
    
    def ndim(self) -> int:
        
        """
        This method returns the number of overall columns
        """
        return self.dataframe.shape[1]