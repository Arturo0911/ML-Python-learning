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
        self._path = '.csv/.cloud_parameters/.{}/.{}/.{}.csv'.format(cloud_parameter, year_consult, year_consult)
        self.dataframe_weather = pd.read_csv(self.path)
        

    def read_dataframe(self):
        # Return the dataframe
        
        return self.dataframe_weather

    def make_subset(self):
        
        data_frame_subset = None

        return None


    """def make_subset(self,first_parameter, second_parameter):
        # compare two or more clouds behavior
        # Each parameter is for the clouds behavior
        # using the states, we can compare into the dataframe values
        # Return both subsets

        subset_first = self.dataframe_weather[first_parameter]
        subset_second = self.dataframe_weather[second_parameter]

        return subset_first, subset_second"""


# Print whole behavior clouds
# If the value is NaN is because nothing happened with that behavior

"""
for x in (make_list()):

    test_init = Init_test(x, 2017)
    print(test_init.read_dataframe())

"""

test_init = Init_test('Broken_clouds', 2017)
print(test_init.read_dataframe())
# first_parameter, second_parameter = test_init.make_subset('Broken_cloud', 'Ligth_rain')



#print(first_parameter)








