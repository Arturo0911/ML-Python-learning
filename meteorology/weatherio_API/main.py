import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
from urllib.error import HTTPError
from pprint import pprint
import requests
from calendar import monthrange
from datetime import date, timedelta
import json

# import files from directory
import CSV

from API_values import API_values
from Create_days import Create_days

latitude = '-2.335017'
longitude = '-80.229769'
# time_start = '2016-10-21'
# time_end = '2016-10-22'


if __name__ == "__main__":

    # Instantiate from Create_days class

    days = Create_days()
    days.generate_appends()

    # Initialize process

    new_query = API_values(latitude, longitude)
    # CSV.create_file(2018,2018)

    # Generate a iterator to fetch values from dates
    # print(days.return_days_keys())

    CSV.create_file(2019, 2019)
    CSV.create_values_csv_file(2019, 2019)

    for i in range(1, len(days.get_objects()[2019])):

        time_start = days.get_objects()[2019][i-1]
        time_end = days.get_objects()[2019][i]

        # Instantiate from API_values class

        #print(time_start, time_end)

        new_query.generate_process(time_start, time_end)

        list_behavior = list()
        list_temperature = list()
        list_clouds = list()
        list_precipitation = list()

        for j in new_query.response_data['data']:

            # Here store all values of description into weather key
            # after call the function 'create_file_with_parameters()'

            list_behavior.append(j['weather']['description'])
            list_temperature.append(j['temp'])
            list_precipitation.append(j['precip'])
            list_clouds.append(j['clouds'])

            # if j['weather']['description'] not in list_behavior :
            #    list_behavior.append(j['weather']['description'])

        # for l in new_query.response_data['data']:

        CSV.create_file_with_parameters(
            2019, 2019, time_start, time_end, list_behavior)

        CSV.store_into_values(2019, 2019, time_start, time_end,
                              list_temperature, list_precipitation, list_clouds)

    """
    for x in days.return_days_keys():
        
        print(x)
        CSV.create_file(x,x)
        CSV.create_values_csv_file(x,x)

        for i in range(1, len(days.get_objects()[x])):

            time_start = days.get_objects()[x][i-1]
            time_end = days.get_objects()[x][i]

            # Instantiate from API_values class

            #print(time_start, time_end)
        
            new_query.generate_process(time_start, time_end)


            list_behavior = list()
            list_temperature = list()
            list_clouds = list()
            list_precipitation = list()
            

            for j in new_query.response_data['data']:

                # Here store all values of description into weather key
                # after call the function 'create_file_with_parameters()'

                list_behavior.append(j['weather']['description'])
                list_temperature.append(j['temp'])
                list_precipitation.append(j['precip'])
                list_clouds.append(j['clouds'])
                


                # if j['weather']['description'] not in list_behavior :
                #    list_behavior.append(j['weather']['description'])



            #for l in new_query.response_data['data']:



            CSV.create_file_with_parameters(x,x,time_start,time_end,list_behavior)
            
            CSV.store_into_values(x,x, time_start, time_end,list_temperature, list_precipitation, list_clouds)

    """

    """
    for i in range(1, len(days.get_objects()[2018])):

        time_start = days.get_objects()[2018][i-1]
        time_end = days.get_objects()[2018][i]

        # Instantiate from API_values class

        #print(time_start, time_end)
    
        new_query.generate_process(time_start, time_end)
        list_values = list()
        

        for j in new_query.response_data['data']:

            # Here store all values of description into weather key
            # after call the function 'create_file_with_parameters()'

            list_values.append(j['weather']['description'])


            # if j['weather']['description'] not in list_values :
            #    list_values.append(j['weather']['description'])
        CSV.create_file_with_parameters(2018,2018,time_start,time_end,list_values)
    """
