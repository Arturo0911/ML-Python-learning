""" IN THIS FILE, WE GONNA TEST THE DATA, USING COMPARATIONS BETWEEN DATAS, AND PARAMETERS
    
"""
import time
from datetime import time
from Interface_objects import make_list
from Math_process import Math_process
from os import O_TRUNC
from Create_days import Create_days as cd

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

    def read_dataframe(self, object_parameters):
        # Return the dataframe with all the values in the data
        # set the names of parameters, to avoid get verbose mode on the algorithm

        cloud_param = object_parameters['values']['cloud_parameter']
        year_param = object_parameters['values']['year_activity']
        data_frame = pd.read_csv(self._path.format(
            cloud_param, year_param, year_param))
        return data_frame

    def make_subset(self, object_parameters):
        """
            get the parameters with the object parameters
            set cloud parameters in differents years
            create variables to avoid big names into the methods
            the variable first_param_year will be used two times, 
            because the directory and the file has the same name

            Structure of the parameters to be evaluated
            object_parameters => {

                'value': {'cloud_parameter': Behavior cloud: Broken_clouds, Light_rain, 
                            Clear_Sky,'year_activity': None,'filter': 'the filter is the
                             header of each column to be evaluated'}
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
        """
        get the values from the dictionary object_parameters
        set the range of the filter that we wanna show
        """

        subset = self.make_subset(object_parameters)

        data_range = self.dataframe_weather[subset >= float(range)]

        return data_range

    def _comparative_between_three_years(self):
        """
        In this method, we will called all the values, parsed and draw a 
        charted scattered, but presenting in a loop for the three years, 
        we already have stored in csv files.
        """

        # Instance from the another main classes

        math_process = Math_process()

        create_days = cd()
        create_days.generate_appends()

        # Object
        final_object = []

        # for x in create_days.get_objects():
        for x in make_list():

            # print(x)

            # Loop in each year stored 2017 2018 2019; comming soon 2020.

            # Now we can get the antoher parameters of the sky such overcastered
            # from the make_list() function
            change_object = []

            for y in create_days.get_objects():
                print(y)

                # Initializers
                # the only reason is for to generate a list with the time start at the list_date
                # and temperature values at the list_temperature
                list_humidity = list()
                list_temperature = list()

                objects_ = {
                    'values': {
                        'cloud_parameter': x,
                        'year_activity': y
                    }
                }

                # set the subset, temperature, is the best parameter to filter by.
                dataframe_filtered = self.read_dataframe(
                    objects_)[self.read_dataframe(objects_)['temperature'] > 0]

                # LOOPS FOR APPENDS
                for i in dataframe_filtered['relative_humidity']:
                    list_humidity.append(i)

                for j in dataframe_filtered['temperature']:
                    list_temperature.append(j)

                # set the object_data with the values.
                # print(x)
                object_data = {
                    'x': list_humidity,
                    'y': list_temperature
                }

                # print(object_data)

                # print(math_process.check_covariance(object_data))

                if math_process.check_covariance(object_data) > 0:
                    # print("Parameters %s %s"%(x,y))
                    # print("Presenting the obeject to be evaluated: ", objects_)
                    # print("Dataframe filtered")
                    # print(dataframe_filtered)
                    # print("\n")
                    # print("[*] Covariance is more than 1")
                    # print("[*] Covariance: ", math_process.check_covariance(object_data), end="")

                    # print("[*] Correlation coefficent: ", math_process.correlation_coefficent(object_data))

                    final_object.append({

                        'parameter': x,
                        'year': y,
                        'covariance': math_process.check_covariance(object_data),
                        'correlation_coefficent': math_process.correlation_coefficent(object_data)

                    })

                    """change_object.append({
                        str(y): list_temperature
                    })"""
                    print(final_object)

                    """plt.scatter(object_data['x'], object_data['y'])
                    plt.xlabel("Dates")
                    plt.ylabel("Temperature")
                    plt.show()"""

                elif math_process.check_covariance(object_data) == 0:
                    # print("Covariance: ", math_process.check_covariance(object_data), end="")
                    # print("[0] Covariance is Zero")
                    pass
                else:
                    # print("Covariance: ", math_process.check_covariance(object_data), end="")
                    #print("[x] Covariance is negative")
                    pass
            
            #print(change_object)
            """if len(change_object) == 3:
                math_process.set_relation_three_years(change_object)"""


def test_function_with_parameters():
    """
        This function, only will be read the instancies, from the main Class
    """
    test_init = Init_test()
    test_init._comparative_between_three_years()


test_function_with_parameters()


"""
            objects_ = {
                'values': {
                'cloud_parameter': 'Scattered_clouds',
                'year_activity': x
                }
            }
            # set the subset, temperature, is the best parameter to filter by.
            dataframe_filtered = self.read_dataframe(objects_)[self.read_dataframe(objects_)['temperature'] > 0]

            # LOOPS FOR APPENDS
            for i in dataframe_filtered['relative_humidity']:
                list_humidity.append(i)

            for j in dataframe_filtered['temperature']:
                list_temperature.append(j)
            
            # set the object_data with the values.
            # print(x)
            object_data = {
                'x': list_humidity,
                'y':list_temperature
            }
            # print(object_data)

            # print(math_process.check_covariance(object_data))

            if math_process.check_covariance(object_data) > 0:
                print("[*] Covariance is", end="")
                print(True)
            else:
                print(False)
            """

"""
        # Commented until the test of covariance from the years
        # printing using pyplot data in a scattered chart.

        plt.scatter(object_data['x'], object_data['y'])
        plt.xlabel("Dates")
        plt.ylabel("Temperature")
        plt.show()
    """

# pprint(final_object)

# pprint(change_object)
