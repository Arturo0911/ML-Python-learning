import pandas as pd

import numpy as np
import torch

from Model import Prediction_from_files

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

#  print her methods
# print(len(columns_values))

# print(columns_behavior)
# print(prediction_values.return_stats())

# print(len(prediction_values.return_stats()))
# print(type(prediction_values.return_stats()))



# As parameter we put 2 value, CUZ the behavior cloud
# must be greater than 2
# print(prediction_values.return_stats(2))
# print(prediction_values.return_stats(2)['time_start'])
# print(prediction_values.return_stats(2)['time_end'])


list_provitional = []

for x in prediction_values.return_stats(2):
    print(x)
    if x == 'time_start' or  x == 'time_end':
         list_provitional.append(prediction_values.return_stats(2)[x])

print(list_provitional)


# for x in prediction_values.return_stats():
#    print(prediction_values.return_stats()[x])

# to stablish a filter to store
# subset_datetimes = prediction.read_file_behavior(path_1)['time_start']
# print(subset_datetimes)



