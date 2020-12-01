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

parameter_to_filter = 'Light_rain'



# define object
prediction_behavior = Prediction_from_files(path_values)
prediction_values = Prediction_from_files(path_behavior)

# call methods
dataframe_values, columns_values = prediction_values.read_file()
dataframe_behavior, columns_behavior = prediction_behavior.read_file()
prediction_values.get_subset(parameter_to_filter)

# call subset attribute
prediction_behavior.get_subset('time_start')



# print(prediction_values.return_stats(2).to_numpy())


prediction_value_array = prediction_values.return_stats(2).to_numpy()

list_parameters = list()



for x in prediction_value_array:
    print(x, '\n')

for x in prediction_value_array:

    list_parameters.append({'time_start':x[0], 'time_end':x[1]})


print(list_parameters)




# now we get the values from the day that already has a specific behavior 
# on her clouds, for example light rain is the other parameter 
# to be taken into account
print(prediction_behavior.return_stats_string_parameter(list_parameters[0]['time_start']))



