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
    print(len(days.get_objects()))
    print(days.get_objects().keys())


    # Initialize process

    new_query = API_values(latitude, longitude)


    


    # Generate a iterator to fetch values from dates
    
    for i in range(1, len(days.get_objects()[2018])):

        time_start = days.get_objects()[2018][i-1]
        time_end = days.get_objects()[2018][i]

        # Instantiate from API_values class
            
        print(time_start, time_end)
    
        new_query.generate_process(time_start, time_end)
        new_query.get_parameters()
        #print(new_query.get_api_key())
        #print(new_query.get_keys())
        #print(new_query.check_location())

        #print("========================================== %s %s"%(time_start, time_end),"==========================================")


    #new_query.get_parameters_sky_behavior()





# the arrays with the dates to be storage
"""

api_key = 'ba199bd058f45b1a54e0d25ba95d1ca9'
weatherbi_key = 'c96c2aa02b1b43e184580f8efe648f59' # fetch api data from historic, using latitude and longitude
#latitude = '-2.335017'
latitude = '-2.3352106'
_latitude = '-2.3408677'
#longitude = '-80.229769'
longitude = '-80.2300508'
_longitude = '-80.2104828'
weatherstack_key = 'e57f178396859a0e95647a48f82b4504'
url = 'https://api.weatherbit.io/v2.0/history/hourly?lat=-2.335017&lon=-80.229769&start_date=2020-11-18&end_date=2020-11-19&tz=local&key=c96c2aa02b1b43e184580f8efe648f59'

# time to start and end
# examples we use 2016 in October
time_start = '2016-10-21'
time_end = '2016-10-22'



url_parameters = 'https://api.weatherbit.io/v2.0/history/hourly?lat={}&lon={}&start_date={}&end_date={}&tz=local&key={}'.format(latitude,longitude,time_start,time_end,weatherbi_key)
response = requests.get(url_parameters).json()
#pprint(response)
#pprint(response['data'])   

#pprint(len(response['data']))


for x in response['data']:

    print('clouds values: ',x['clouds'])



class Create_days:

    def __init__(self):
        

        self.year_2017 = list()
        self.year_2018 = list()
        self.year_2019 = list()

        self.october_2016 = date(2016, 10, 1)
        self.january_2017 = date(2017, 1, 31)

        self.october_2017 = date(2017,10,1)
        self.january_2018 = date(2018,1,31)

        self.october_2018 = date(2018,10,1)
        self.january_2019 = date(2019,1,31)


        self.objects = {}

    def generate_appends(self):
        
        delta_2017 = self.january_2017 - self.october_2016
        delta_2018 = self.january_2018 - self.october_2017
        delta_2019 = self.january_2019 - self.october_2018


        for x in range(delta_2017.days + 1):
            days = self.october_2016 + timedelta(days=x)
            self.year_2017.append(str(days))

        self.objects[2017] = self.year_2017

        for x in range(delta_2018.days + 1):
            days = self.october_2017 + timedelta(days=x)
            self.year_2018.append(str(days))
        self.objects[2018] = self.year_2018


        for x in range(delta_2019.days +1):
            days = self.october_2018 + timedelta(days= x)
            self.year_2019.append(str(days))
        self.objects[2019] = self.year_2019


    def json_generate(self):
        
        with open('neuronal.json', 'w') as f:
            json.dump(self.objects,f,indent=4)

    


    def get_objects(self):
        
        return self.objects

if __name__ == "__main__":
    
    days = Create_days()
    days.generate_appends()
    days.json_generate()
    #print(days.get_objects())
"""




