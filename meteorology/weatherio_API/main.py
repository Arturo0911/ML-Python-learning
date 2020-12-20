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
import Interface_objects

# CONSTANTS
latitude = '-2.335017'
longitude = '-80.229769'

scattered_cloud_object = list()
broken_cloud_object = list()
light_rain_object = list()
few_clouds_object = list()
clear_sky_object = list()
overcasted_clouds_objects= list()


# Create a object with the values 
url_from_API = {
    'latitude': '-2.335017',
    'longitude':'-80.229769',
    'key_url_api':'c96c2aa02b1b43e184580f8efe648f59'
}


if __name__ == "__main__":

    # Instantiate from Create_days class

    days = Create_days()
    days.generate_appends()

    # Initialize process

    new_query = API_values(latitude, longitude)
    CSV.create_hidden_directories()
    # CSV.create_file(2018,2018)

    # Generate a iterator to fetch values from dates
    # print(days.return_days_keys())

    for x in days.get_objects():
        
        # first of all, call csv to create new files into the directories exists

        for i in Interface_objects.make_list():

             # this one gonna be return None value, it's only process xD


            CSV.create_headers_into_hidden_directories(x,x,i)

        for y in range(1,len(days.get_objects()[x])):

            # time start and time end
            time_start = days.get_objects()[x][y-1]
            time_end = days.get_objects()[x][y]
            # print(time_start,time_end)

            new_query.generate_process(time_start, time_end) # process is called, and keys from the API is used
            # pprint(new_query.response_data['data'])

            # print(Interface_objects.create_objects_from_clouds(new_query.response_data['data']))

            
            for j in Interface_objects.create_objects_from_clouds(new_query.response_data['data']):

                CSV.generate_data_into_csv_files(x,x,time_start,time_end, j,Interface_objects.create_objects_from_clouds(new_query.response_data['data'])[j])
            






