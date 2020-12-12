""" IN THIS FILE, WE GONNA TEST THE DATA, USING COMPARATIONS BETWEEN DATAS, AND PARAMETERS
    
"""

import numpy as np
import pandas as pd
import torch


""" Libraries of the data storage """









from Interface_objects import make_list # this one return the list o behavior to be instantiated.



class Init_test:
    
     

    def __init__(self,cloud_parameter, year_consult):
        # initialize the parameters to be the query
        
        self.path = '.csv/.clouds_parameters/.'+ cloud_parameter+'/.'+str(year_consult)+'/.'+str(year_consult)+'.csv'
        self.dataframe_weather = pd.read_csv(self.path)
        

    def read_dataframe(self):

        return self.dataframe_weather


    def compare_parameters(self,):
        # compare two or more clouds behavior
        # using the states, we can compare into the dataframe values
        

        

        pass


# Print whole behavior clouds
# If the value is NaN is because nothing happened with that behavior

for x in (make_list()):

    test_init = Init_test(x, 2017)
    print(test_init.read_dataframe())



