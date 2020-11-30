import torch
import numpy as np
import pandas as pd






class Prediction_from_files:

    def __init__(self, path):

        self.dataframe = pd.read_csv(path)
        

    

    # Behavior methods
    def read_file_behavior(self):
        
        return self.dataframe, self.dataframe.columns

    

    # Values methods

    def read_file_values(self):
        pass
        
    