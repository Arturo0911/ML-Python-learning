import pandas as pd

import numpy as np
import torch

from Model import Prediction_from_files


""" THIS FILE WILL BE LAUNCH THE PROJECT """




# comparation from the same years
# define constants
# 2017
path_values = 'csv/values/{}/{}.csv'.format(2017,2017)
path_behavior = 'csv/behavior/{}/{}.csv'.format(2017,2017)

# 2018
# path_values = 'csv/values/{}/{}.csv'.format(2018,2018)
# path_behavior = 'csv/behavior/{}/{}.csv'.format(2018,2018)




# those constante will be included into the object to 
# be compared

time_start = ""
time_end = ""

first_parameter = 'Light_rain'
# second_paramter = 'Broken_clouds'



# define object
prediction_behavior = Prediction_from_files(path_values)
prediction_values = Prediction_from_files(path_behavior)

# call methods
dataframe_values, columns_values = prediction_values.read_file()
dataframe_behavior, columns_behavior = prediction_behavior.read_file()
prediction_values.get_subset(first_parameter)

# call subset attribute
prediction_behavior.get_subset('time_start')



# print(prediction_values.return_stats(2).to_numpy())


prediction_value_array = prediction_values.return_stats(2).to_numpy()

list_parameters = list()



for x in prediction_value_array:
    print(x, '\n')

for x in prediction_value_array:

    list_parameters.append({'time_start':x[0], 'time_end':x[1]})


# print(list_parameters)


for x in list_parameters:

    # now we get the values from the day that already has a specific behavior 
    # on her clouds, for example light rain is the other parameter 
    # to be taken into account

    any_value = prediction_behavior.return_stats_string_parameter(x['time_start'])

    print(any_value.to_numpy())
    break


# We'll be analyze the temperature data to get any pattern
analyzer = prediction_behavior.return_stats_string_parameter(list_parameters[0]['time_start'])


print("TEMPERATURE")
print(analyzer.to_numpy()[0][2]) # Because is converted from datadframe to numpy array, matrix in this case
print(type(analyzer.to_numpy()[0][2]))


for x in analyzer.to_numpy()[0][2]:
    print(x)









"""

        That is the output, taken the parameters like time_start
        time_start    time_end                                        temperature                                            precips                                             clouds
    98  2017-01-07  2017-01-08  [28, 27, 26, 26, 26, 26, 26, 26.2, 27, 28, 30,...  [0, 0, 0, 0, 0, 0, 0, 0.1, 0.1, 0, 0.1, 0.1, 0...  [94, 93, 90, 88, 91, 92, 91, 86, 90, 94, 95, 9...
        time_start    time_end                                        temperature                                            precips                                             clouds
    99  2017-01-08  2017-01-09  [24.4, 24, 24, 23, 23, 23, 23.3, 23.7, 23.8, 2...  [0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.2, 0.6, 0.5, ...  [98, 98, 98, 98, 97, 97, 96, 96, 96, 95, 95, 9...
        time_start    time_end                                        temperature                                            precips                                             clouds
    100  2017-01-09  2017-01-10  [25, 24, 23, 23, 23, 23, 23, 23.1, 23, 24, 25,...  [3.5, 4.1, 4.3, 3.8, 2.7, 1.7, 1, 0.2, 0.1, 0....  [98, 98, 98, 98, 94, 83, 72, 68, 64, 65, 70, 7...
        time_start    time_end                                        temperature                                            precips                                             clouds
    101  2017-01-10  2017-01-11  [23.8, 23.6, 23.4, 23.2, 23, 24, 24, 23.7, 23,...  [1, 1, 1, 1, 0.8, 0.6, 0.4, 0.2, 0.1, 0.1, 0.1...  [98, 97, 95, 94, 92, 90, 85, 82, 83, 81, 65, 3...
        time_start    time_end                                        temperature                                            precips                                             clouds
    111  2017-01-20  2017-01-21  [27, 27, 26, 26, 26, 26, 24, 24.4, 25, 25, 24....  [0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.6, 0.9, ...  [94, 93, 93, 91, 88, 89, 86, 80, 83, 88, 88, 8...
        time_start    time_end                                        temperature                                            precips                                             clouds
    117  2017-01-26  2017-01-27  [26, 26, 26, 25, 24, 23, 24, 25, 26, 27, 27.7,...  [0.4, 0.4, 0.3, 0.3, 0.2, 0.1, 0.1, 0.3, 0.3, ...  [84, 84, 86, 85, 88, 73, 78, 83, 88, 93, 94, 9...
        time_start    time_end                                        temperature                                            precips                                             clouds
    120  2017-01-29  2017-01-30  [24.8, 24.6, 24.4, 24.2, 24, 24, 24, 24, 24, 2...  [0, 0, 0, 0, 0, 0, 0, 0.3, 0.2, 0.2, 0.2, 0.2,...  [97, 97, 97, 97, 97, 97, 89, 80, 70, 61, 55, 4...
        time_start    time_end                                        temperature                                            precips                                             clouds
    121  2017-01-30  2017-01-31  [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 2...  [1.2, 1.1, 1, 0.9, 0.8, 0.7, 0.8, 1.1, 1, 0.9,...  [94, 95, 96, 98, 97, 98, 98, 98, 98, 98, 98, 9...


"""

#print(prediction_behavior.return_stats_string_parameter(list_parameters[0]['time_start']))



