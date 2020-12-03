from pandas.core.arrays import string_
import torch
import numpy as np
import pandas as pd


class Prediction_model:

    def __init__(self, path):

        self.dataframe = pd.read_csv(path)
        self.weathersubset = None
        self.weathersubset_more_parameters = self.dataframe[['time_start','time_end','Light_rain','Broken_clouds']]

        self.stats = None


    def get_stats_by_more_paramters(self,keyword, parameter):

        stats = self.dataframe[self.weathersubset_more_parameters[keyword] >= parameter]

        return stats
        

    def read_file(self):
        
        return self.dataframe, self.dataframe.columns

    def get_subset(self, parameter):

        """the subset will be return the type of parameter to be studied"""
        self.weathersubset = self.dataframe[parameter]

        return self.weathersubset

    def return_stats(self, parameter):

        try:
            self.stats = self.dataframe[self.weathersubset['Light_rain'] > parameter]
            return self.stats
        except Exception as e:
            return str(e)

        else:
            return None

    
    def return_stats_string_parameter(self, parameter):

        # method to get the filter, using strings as paramters
        # to be filtered example: time start or time end
        try:
            self.stats = self.dataframe[self.weathersubset['Light_rain'] > parameter]
            return self.stats
        except Exception as e:
            return str(e)

        else:
            return None





PATH_BEHAVIOR = 'csv/behavior/{}/{}.csv'.format(2017,2017)
PATH_VALUES = 'csv/values/{}/{}.csv'.format(2017,2017)


# instances objects
behavior_model = Prediction_model(PATH_BEHAVIOR)
#values_model = Prediction_model(PATH_VALUES)


# print("Printing the dataframe")
# print(behavior_model.dataframe)

# SET THE PARAMETER
#print(behavior_model.get_subset('Light_rain'))
# print(behavior_model.dataframe.columns)


# WE GONNA TO PRINT USING MORE PARAMETERS AS SUBSET
# print(behavior_model.weathersubset_more_parameters)



# NOW IN THE STATS MODEL, PUT 2 AS MAIN PARAMETER TO
# TO FECH THE FILTER BETWEEN LIGHT RAIN AND BROKEN CLOUDS


# print("Printing the subset with the parameters")
# print(behavior_model.weathersubset_more_parameters)


"""
counter = 0
for x in behavior_model.weathersubset_more_parameters['Light_rain']:
    print(counter,"               ", x)
    counter += 1
    # printing the keywords or the headers
"""    




# Declare an objects wherever xD to do comparations


dataframe_value = pd.read_csv(PATH_VALUES)
subset_value = dataframe_value[['time_start', 'time_end','temperature','precips']]

#print(subset_value)



# print("Printing the filtered dataframes")
# this one gonna print the filtered as dataframe[ parameter >= value]

# define a variable

value = behavior_model.get_stats_by_more_paramters('Light_rain',2)
print('printing the values filtered with the parameter {} are greater or equal to {}'.format('light_rain',2))
print(value)
value_array = value.to_numpy()


print(value_array)


print("Printing valyes from light rain")
for x in value_array:
    # Asign the time_start parameterm into the instance wherever i have called 

    parameters_insterestings = dataframe_value[subset_value['time_start'] == x[0]][['temperature','precips']]

    print(parameters_insterestings['temperature'].to_numpy()[0].split(", ")) # to fetch in array type splited (', ' )
    # print(len(parameters_insterestings['temperature'].to_numpy()[0]))
