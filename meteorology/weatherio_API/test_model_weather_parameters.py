""" IN THIS FILE, WE GONNA TEST THE DATA, USING COMPARATIONS BETWEEN DATAS, AND PARAMETERS
    
"""

import numpy as np
import pandas as pd
import torch
from pprint import pprint

""" Libraries of the data storage """


from Interface_objects import make_list # this one return the list o behavior to be instantiated.



class Init_test:     

    def __init__(self,cloud_parameter, year_consult):
        # initialize the parameters to be the query
        
        self.path = '.csv/.clouds_parameters/.'+ cloud_parameter+'/.'+str(year_consult)+'/.'+str(year_consult)+'.csv'
        self._path = '.csv/.clouds_parameters/.{}/.{}/.{}.csv'
        self.dataframe_weather = pd.read_csv(self.path)
        

    def read_dataframe(self):
        # Return the dataframe with all the values in the data
        
        return self.dataframe_weather

    def make_subset(self, object_parameters):
        # get the parameters with the object parameters
        # set cloud parameters in differents years


        """
        object_parameters = {

            'first_parameter': {'cloud_parameter': None, 'year_activity': None},
            'second_parameter': {'cloud_parameter': None, 'year_activity': None},
        }
        """

        first_param_cloud = object_parameters['values']['cloud_parameter']
        first_param_year = object_parameters['values']['year_activity']
        first_param_filter = object_parameters['values']['filter']

        """second_param_cloud = None
        second_param_year = None
        second_param_filter = None"""

        first_data_frame_subset = pd.read_csv(self._path.format(first_param_cloud,first_param_year
        ,first_param_year))


        """second_data_frame_subset = pd.read_csv(self._path.format(object_parameters['second_parameter']['cloud_parameter'],
        object_parameters['first_parameter']['year_activity'], object_parameters['first_parameter']['year_activity']))
        """

        # taking the first_data_parameter, put the parameter to be filtered

        subset_first = self.read_dataframe()[first_param_filter]


        #return first_data_frame_subset , second_data_frame_subset

        # this one gonna return the subset with the filter
        return subset_first

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
object_parameters = {

    'values': {
        'cloud_parameter': 'Broken_clouds', 
        'year_activity': 2017, 
        'filter': 'temperature'
        }
    }
test_init = Init_test('Broken_clouds', 2017)
pprint(object_parameters)

firstparam = test_init.make_subset(object_parameters)

print(firstparam)

#print(test_init.read_dataframe())
# first_parameter, second_parameter = test_init.make_subset('Broken_cloud', 'Ligth_rain')



#print(first_parameter)








