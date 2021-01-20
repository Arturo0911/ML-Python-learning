""" 
IN THIS FILE, WE GONNA TEST THE DATA, USING COMPARATIONS BETWEEN DATAS, AND PARAMETERS   
"""
import time
from datetime import time
from Interface_objects import make_list
from Math_process import Math_process
from os import O_TRUNC, listxattr
from Create_days import Create_days as cd

from pandas.io import api
import numpy as np
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import seaborn as sns

from concurrent.futures import ThreadPoolExecutor


""" Libraries of the data storage """

# this one return the list o behavior to be instantiated.
# supervised machine learning


class Init_test:

    def __init__(self):
        # initialize the parameters to be the query

        self._path = '.csv/.clouds_parameters/.{}/.{}/.{}.csv'

    def read_dataframe(self, object_parameters):
        # Return the dataframe with all the values in the data
        # set the names of parameters, to avoid get verbose mode on the algorithm
        '''
            objects_ = {
                'values': 
                    {
                        'cloud_parameter': x,
                        'year_activity': y
                    }
                }
        '''

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

        dataframe = pd.read_csv(self._path.format(
            first_param_cloud, first_param_year, first_param_year))

        # taking the first_data_parameter, put the parameter to be filtered
        # this one gonna return the subset with the filter
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

        # Lists
        coefficient_positive = list()
        coefficient_negative = list()

        # =======================================
        scattered_cloud = list()
        broken_cloud = list()
        light_rain = list()
        few_clouds = list()
        clear_sky = list()
        overcast_clouds = list()

        for x in make_list():
            # Loop in each year stored 2017 2018 2019 2020.
            # Now we can get the antoher parameters of the sky such overcastered
            # from the make_list() function

            for y in create_days.get_objects():
                # Initializers
                # the only reason is for to generate a list with the time start at the list_date
                # and temperature values at the list_temperature

                list_humidity = list()
                list_temperature = list()
                list_time_prediction = list()

                # get the list of clouds parameters and year activity
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

                for k, l in zip(dataframe_filtered['time_start'], dataframe_filtered['time_end']):
                    list_time_prediction.append(k+" - "+l)

                # set the object_data with the values.

                object_data = {
                    'x': list_humidity,
                    'y': list_temperature,
                    'time_prediction': list_time_prediction,
                }

                # group by cloud type and add their properties
                if x == "Overcast_clouds":
                    overcast_clouds.append({x: {'cloud_type': x, str(y): object_data,
                                                'coefficient_correlation': math_process.correlation_coefficient(object_data)}})
                elif x == "Broken_clouds":
                    broken_cloud.append({x: {'cloud_type': x, str(y): object_data,
                                             'coefficient_correlation': math_process.correlation_coefficient(object_data)}})
                elif x == "Scattered_clouds":
                    scattered_cloud.append({x: {'cloud_type': x, str(y): object_data,
                                                'coefficient_correlation': math_process.correlation_coefficient(object_data)}})
                elif x == "Few_clouds":
                    few_clouds.append({x: {'cloud_type': x, str(y): object_data,
                                           'coefficient_correlation': math_process.correlation_coefficient(object_data)}})
                elif x == "Clear_Sky":
                    clear_sky.append({x: {'cloud_type': x, str(y): object_data,
                                          'coefficient_correlation': math_process.correlation_coefficient(object_data)}})
                elif x == "Light_rain":
                    light_rain.append({x: {'cloud_type': x, str(y): object_data,
                                           'coefficient_correlation': math_process.correlation_coefficient(object_data)}})
                else:
                    pass

                # use correlation_coefficient() instead of check_covariance()
                if math_process.correlation_coefficient(object_data) > 0:
                    # here prove that the coefficient is greater than 0
                    coefficient_positive.append({'cloud_type': x, str(y): object_data,
                                                 'coefficient_correlation': math_process.correlation_coefficient(object_data)})

                elif math_process.correlation_coefficient(object_data) == 0:
                    pass

                else:
                    coefficient_negative.append({'cloud_type': x, str(y): object_data,
                                                 'coefficient_correlation': math_process.correlation_coefficient(object_data)})

        coefficients = {
            'Overcast_clouds': overcast_clouds,
            'Broken_clouds': broken_cloud,
            'Scattered_clouds': scattered_cloud,
            'Few_clouds': few_clouds,
            'Clear_Sky': clear_sky,
            'Light_rain': light_rain
        }
        # return coefficient_positive, coefficient_negative
        return coefficients, coefficient_positive, coefficient_negative


def main():
    """
        This function, only will be read the instancies, from the main Class
        humidity relative is the X variable and the temperature is Y
    """
    test_init = Init_test()
    coefficients, positive, negative = test_init._comparative_between_three_years()

    # optimization('Overcast_clouds', '2017','2017')
    # print("\n")
    optimization()

    '''with ThreadPoolExecutor(max_workers=2) as executors:

        optimization_1 = optimization('Overcast_clouds','2017')
        
        executors.submit(optimization_1)
        executors.submit(optimization, 'Overcast_clouds','2018')
        #print("\n")
        executors.submit(optimization, 'Overcast_clouds','2019')
        executors.submit(optimization, 'Overcast_clouds','2020')
        #print("\n")
        # optimization('Overcast_clouds','2017')
    # print("\n")
    
    #optimization('Overcast_clouds','2018')
    #print("\n")
    
    #optimization('Overcast_clouds','2019')
    # print("\n")
    
    #optimization('Overcast_clouds','2020')
    # pprint(coefficients[x])'''


def optimization():#cloud_type,year_model):

    list_years = ['2017','2018','2019','2020']
    list_accuracy = list()
    list_predictions = list()
    list_dates_predictions_matched = list()

    '''for x in range(0,len(list_years)):

        if year_model != list_years[x]:

            # print(year_model,"          ",list_years[x])
            # pprint(testing_models('Overcast_clouds', year_model, list_years[x]))
            list_predictions.append({list_years[x]:testing_models(cloud_type, year_model, list_years[x])})


    for x in range(0,len(list_years)):

        if year_model != list_years[x]:
            list_accuracy.append(testing_models(cloud_type, year_model, list_years[x])['accuracy'])
            # list_accuracy.append(testing_models(cloud_type, year_model,list_years[x])['accuracy'])
            # list_accuracy.append(testing_models(cloud_type, year_model, '2020')['accuracy'])

    for x in range(0,len(list_years)):

        if year_model != list_years[x]:
            list_dates_predictions_matched.append(testing_models(cloud_type, year_model, list_years[x])['dates_accuracy'])
            # list_dates_predictions_matched.append(testing_models(cloud_type, '2017', '2019')['dates_accuracy'])
            # list_dates_predictions_matched.append(testing_models(cloud_type, '2017', '2020')['dates_accuracy'])


    object_optimization = {
        'year_model': year_model,
        'average_accuracy': float("{0:2f}".format(sum(list_accuracy)/len(list_accuracy))),
        'average_dates': float("{0:2f}".format(sum(list_dates_predictions_matched)/len(list_dates_predictions_matched))),
        # 'list_predictions':len(list_predictions)

    }

    print(object_optimization)



    '''
    testing_models('Overcast_clouds', '2017', '2018')
    print("\n")
    testing_models('Overcast_clouds', '2017', '2019')
    print("\n")
    testing_models('Overcast_clouds', '2017', '2020')

    # pprint(testing_models('Overcast_clouds', '2017', '2019'))
    # print("\n")
    # pprint(testing_models('Overcast_clouds', '2017', '2020'))
    # print("\n")
    '''pprint(testing_models('Overcast_clouds', '2018', '2017'))
    print("\n")
    pprint(testing_models('Overcast_clouds', '2018', '2019'))
    print("\n")
    pprint(testing_models('Overcast_clouds', '2018', '2020'))'''


def testing_models(cloud_type, year_init, year_to_predict):

    init_test = Init_test()
    coefficients, positive, negative = init_test._comparative_between_three_years()
    Model_train = None
    Model_test = None

    try:
        if year_init == '2017':
            Model_train = coefficients[cloud_type][0][cloud_type][year_init]
        elif year_init == '2018':
            Model_train = coefficients[cloud_type][1][cloud_type][year_init]
        elif year_init == '2019':
            Model_train = coefficients[cloud_type][2][cloud_type][year_init]
        elif year_init == '2020':
            Model_train = coefficients[cloud_type][3][cloud_type][year_init]
        else:
            pass
    except Exception as e:
        print(str(e))

    try:
        if year_to_predict == '2017':
            Model_test = coefficients[cloud_type][0][cloud_type]['2017']
        elif year_to_predict == '2018':
            Model_test = coefficients[cloud_type][1][cloud_type]['2018']
        elif year_to_predict == '2019':
            Model_test = coefficients[cloud_type][2][cloud_type]['2019']
        elif year_to_predict == '2020':
            Model_test = coefficients[cloud_type][3][cloud_type]['2020']
        else:
            pass
    except Exception as e:
        print(str(e))

    # print(test_model_2017[cloud_type]['2017'])

    '''return Math_process().testing_mathematician_model(
        Model_train,
        Model_test['x'],
        Model_test['y'],
        year_to_predict,
        cloud_type,
        Model_train['time_prediction'],
        Model_test['time_prediction'])'''

    Math_process().optimization_gradient_descent(
        Model_train,
        Model_test['x'],
        Model_test['y'],
        year_to_predict,
        cloud_type,
        Model_train['time_prediction'],
        Model_test['time_prediction']
    )


main()



