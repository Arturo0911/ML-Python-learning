import numpy as np
import pandas as pd
import torch


""" Libraries of the data storage """



class Init_test:
    
     

    def __init__(self,cloud_parameter, year_consult):
        # initialize the parameters to be the query
        #

        
        self.path = '.csv/.clouds_parameters/.'+ cloud_parameter+'/.'+str(year_consult)+'/.'+str(year_consult)+'.csv'
        self.dataframe_weather = pd.read_csv(self.path)
        

    def read_dataframe(self):

        return self.dataframe_weather



test_init = Init_test('Broken_clouds', 2017)
print(test_init.read_dataframe())
