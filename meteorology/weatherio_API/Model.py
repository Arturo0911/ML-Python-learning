import torch
import numpy as np
import pandas as pd






class Prediction_from_files:

    def __init__(self, path):

        self.dataframe = pd.read_csv(path)
        self.wathersubset = None

        self.stats = None
        

    

    # Behavior methods
    def read_file(self):
        
        return self.dataframe, self.dataframe.columns

    def get_subset(self, parameter):

        """the subset will be return the type of parameter to be studied"""
        self.wathersubset = self.dataframe[parameter]

        return self.wathersubset

    def return_stats(self):

        self.stats = self.dataframe[self.wathersubset > 2]

        return self.stats
    
        
    