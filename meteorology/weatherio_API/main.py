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


# CONSTANTS
latitude = '-2.335017'
longitude = '-80.229769'

scattered_cloud_object = list()
broken_cloud_object = list()
light_rain_object = list()
few_clouds_object = list()
clear_sky_object = list()
overcasted_clouds_objects= list()









if __name__ == "__main__":

    # Instantiate from Create_days class

    days = Create_days()
    days.generate_appends()

    # Initialize process

    new_query = API_values(latitude, longitude)
    # CSV.create_file(2018,2018)

    # Generate a iterator to fetch values from dates
    # print(days.return_days_keys())

    for x in days.get_objects():
        
        # first of all, call csv to create new files into the directories exists
        #CSV.create_hidden_directories() # this one gonna be return None value, it's only process xD
        #CSV.create_headers_into_hidden_directories(x,x)

        for y in range(1,len(days.get_objects()[x])):

            # time start and time end
            time_start = days.get_objects()[x][y-1]
            time_end = days.get_objects()[x][y]
            # print(time_start,time_end)

            new_query.generate_process(time_start, time_end) # process ins called, and keys from the API is used
            #pprint(new_query.response_data['data'])

            for z in new_query.response_data['data']:
                lista_values = list()

                # waiting for test. automatizate a function
                if z['weather']['description'] == "Few clouds":
                    few_clouds_object.append({'cloud_description':z['weather']['description'],'icon':z['weather']['icon'],
                    'code':z['weather']['code'] ,'temperature': z['temp'],
                    'clouds':z['clouds'], 'precipitation':z['precip'] })
                
                break
            break












    """
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

