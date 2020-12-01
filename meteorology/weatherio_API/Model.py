import torch
import numpy as np
import pandas as pd






class Prediction_from_files:

    def __init__(self, path):

        self.dataframe = pd.read_csv(path)
        self.weathersubset = None

        self.stats = None
        

    

    # Behavior methods
    def read_file(self):
        
        return self.dataframe, self.dataframe.columns

    def get_subset(self, parameter):

        """the subset will be return the type of parameter to be studied"""
        self.weathersubset = self.dataframe[parameter]

        return self.weathersubset

    def return_stats(self, parameter):

        try:
            self.stats = self.dataframe[self.weathersubset > parameter]
            return self.stats
        except Exception as e:
            return str(e)

        else:
            return None
        


            
    
        
    