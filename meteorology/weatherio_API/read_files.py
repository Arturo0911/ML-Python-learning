import pandas as pd

import numpy as np
import torch

from Model import Prediction_from_files

# comparation from the same years
# define constants
path_1 = 'csv/values/{}/{}.csv'.format(2017,2017)
path_2 = 'csv/behavior/{}/{}.csv'.format(2017,2017)

# those constante will be included into the object to 
# be compared

time_start = ""
time_end = ""



# define object
prediction_behavior = Prediction_from_files(path_2)
prediction_values = Prediction_from_files(path_1)

# call methods
dataframe_values, columns_values = prediction_values.read_file_behavior()
dataframe_behavior, columns_behavior = prediction_behavior.read_file_behavior()


#  print her methods
print(len(columns_values))

print(columns_behavior)

for x in columns_values:
    print(x)

# to stablish a filter to store
# subset_datetimes = prediction.read_file_behavior(path_1)['time_start']
# print(subset_datetimes)



