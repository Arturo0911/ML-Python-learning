""" IN THIS FILE, WE GONNA TEST THE DATA, USING COMPARATIONS BETWEEN DATAS, AND PARAMETERS
    
"""

from Interface_objects import make_list
from Math_process import Math_process
from os import O_TRUNC

from pandas.io import api
import numpy as np
import pandas as pd
import torch
from pprint import pprint
import matplotlib.pyplot as plt

""" Libraries of the data storage """

# this one return the list o behavior to be instantiated.


class Init_test:

    def __init__(self):  # cloud_parameter, year_consult):
        # initialize the parameters to be the query

        # self.path = '.csv/.clouds_parameters/.'+ cloud_parameter+'/.'+str(year_consult)+'/.'+str(year_consult)+'.csv'
        self._path = '.csv/.clouds_parameters/.{}/.{}/.{}.csv'
        # self.dataframe_weather = pd.read_csv(self.path)

    
    def read_dataframe(self,object_parameters):
        # Return the dataframe with all the values in the data
        # set the names of parameters, to avoid get verbose mode on the algorithm

        cloud_param = object_parameters['values']['cloud_parameter']
        year_param = object_parameters['values']['year_activity']
        data_frame = pd.read_csv(self._path.format(cloud_param, year_param, year_param))
        return data_frame

    def make_subset(self, object_parameters):
        # get the parameters with the object parameters
        # set cloud parameters in differents years
        # create variables to avoid big names into the methods
        # the variable first_param_year will be used two times, because the directory and the file has the same name
        """

        Structure of the parameters to be evaluated
        object_parameters = {

            'value': {'cloud_parameter': Behavior cloud: Broken_clouds, Light_rain, Clear_Sky, 'year_activity': None, 'filter': 'the filter is the header 
                    of each column to be evaluated'}
        }
        """

        first_param_cloud = object_parameters['values']['cloud_parameter']
        first_param_year = object_parameters['values']['year_activity']
        first_param_filter = object_parameters['values']['filter']

        dataframe = pd.read_csv(self._path.format(
            first_param_cloud, first_param_year, first_param_year))

        # taking the first_data_parameter, put the parameter to be filtered

        # subset_first = self.read_dataframe()[first_param_filter]

        # return first_data_frame_subset , second_data_frame_subset

        # this one gonna return the subset with the filter
        # return subset_first

        return dataframe

    def set_parameters(self, object_parameters, range):
        # get the values from the dictionary object_parameters
        # set the range of the filter that we wanna show
        
        subset = self.make_subset(object_parameters)

        data_range = self.dataframe_weather[subset >= float(range)]

        return data_range

    def _comparative_between_three_years(self, parameter_list):
        """
        In this method, we will called all the values, parsed and draw a charted scattered, but presenting 
        in a loop for the three years, we already have stored in csv files.
        """

        for x in parameter_list:
            pass
        
        return

# Using comparation but in this case using the years as values from future object
"""
    # Structure of the data will be:

        object_callable = {
            '2017': Some data, possible array,
            '2018': "" "" "" "" "" "" "" "",
            '2019': "" "" "" "" "" "" "" ""
        }

        and that's datas, charted on a scattered chart
        but each change or evolution in those 3 years for each query


        object_parameters = {

        'values': {
            'cloud_parameter': 'Broken_clouds', 
            'year_activity': 2017, 
            'filter': 'temperature'
            }
        }

"""

object_parameters = {

    'values': {
        'cloud_parameter': 'Broken_clouds',
        'year_activity': 2017,
        'filter': 'temperature'
    }
}


test_init = Init_test()
print(test_init.read_dataframe(object_parameters))
# print(test_init.make_subset(object_parameters))


"""
# Uncoment this block, whenever you wanna test using comparation from
# two variables



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
print(test_init.set_parameters(object_parameters, 20))
print(len(test_init.set_parameters(object_parameters, 20)))



list_x = list()
list_y = list()
for x,y in zip(test_init.set_parameters(object_parameters, 20)['clouds'],
            test_init.set_parameters(object_parameters, 20)['temperature']):
    # print(x,y)

    list_x.append(x)
    list_y.append(y)


object_parameters_to_compare = {
    'x': list_x,
    'y': list_y
}

# print(object_parameters_to_compare)
#print(test_init.read_dataframe())
# first_parameter, second_parameter = test_init.make_subset('Broken_cloud', 'Ligth_rain')

# instantiate from Math_process
math_process = Math_process()
# print(math_process.check_covariance(object_parameters_to_compare))

#print(first_parameter)

# To set the new parameters, we will to have set new settings
# Maybe using another filters.
# set new object parameters

math_process = Math_process()




####################################################
parameters_object_clouds = {

    'values': {
        'cloud_parameter': 'Broken_clouds', 
        'year_activity': 2017, 
        'filter': 'clouds'
    }
}

parameters_object_temperature = {

    'values': {
        'cloud_parameter': 'Broken_clouds', 
        'year_activity': 2017, 
        'filter': 'temperature'
    }
}

parameters_object_humidity = {
    'values': {
        'cloud_parameter': 'Broken_clouds',
        'year_activity':2017,
        'filter': 'relative_humidity'
    }
}


# print(test_init.make_subset(parameters_object_clouds))
# print(test_init.make_subset(parameters_object_temperature))

# print(test_init.set_parameters(parameters_object_clouds, 0)['clouds'])
# print(test_init.set_parameters(parameters_object_temperature, 0)['temperature'])


# set another test side

list_to_x = list() # clouds
list_to_y = list() # temperature

for x in test_init.set_parameters(parameters_object_humidity, 0)['relative_humidity']:
    list_to_x.append(x)

for y in test_init.set_parameters(parameters_object_temperature, 0)['temperature']:
    list_to_y.append(y)




print("presentation...")
objective = {
    'x': list_to_x,
    'y': list_to_y
}

print(objective)

print(math_process.check_covariance(objective))

print(math_process.correlation_coefficent(objective))

plt.scatter(objective['x'], objective['y'])
plt.xlabel('humidity')
plt.ylabel('temperature')
# the legend doesn't be a object not iterable
# plt.legend(str(math_process.check_covariance(objective)))
plt.show()



test_list_x = [39,43,21,64,57,43,38,75,34,52]
test_list_y = [65
,75
,52
,82
,92
,80
,73
,98
,56
,75]

objetivo = {
    'x':test_list_x,
    'y':test_list_y
}

print(math_process.check_covariance(objetivo))


plt.scatter(objective['x'], objective['y'])
plt.xlabel('clouds')
plt.ylabel('temperature')
# the legend doesn't be a object not iterable
# plt.legend(str(math_process.check_covariance(objective)))
plt.show()

"""
