'''
This file gonna be the loader of all features to the files to store the data
'''

import csv
from calendar import monthrange
from datetime import date, timedelta
import json
import os 
from os.path import *

from Math_process import Math_process

# ------------------------------------------------------------------------------------------------- #
# generated from CSV.py file                                                                        #
# The main directory whenever the data gonna be stored                                              #
# Here we will storage about cloud behavior                                                         #
# how have the clouds been                                                                          #
# ['Overcast clouds', 'Broken clouds', 'Scattered clouds', 'Light rain', 'Few clouds', 'Clear Sky'] #
# MAIN_DIRECTORY = '.csv_api'                                                                       #
# CO_MAIN_DIRECTORY = '.clouds_parameters'                                                          #
# ------------------------------------------------------------------------------------------------- #

""" BEHAVIOR CLOUDS """
def create_file(directory_name,file_name):

    with open('csv'+'/behavior/'+str(directory_name)+'/'+str(file_name)+'.csv', 'w') as csv_file:

        # HEADERS
        writer = csv.writer(csv_file)
        writer.writerow(["time_start", "time_end", 'Overcast_clouds', 'Broken_clouds', 
            'Scattered_clouds', 'Light_rain', 'Few_clouds', 'Clear_Sky'])
    

def create_file_with_parameters(directory_name,file_name, time_start, time_end,list_values):

    with open('csv'+'/behavior/'+str(directory_name)+'/'+str(file_name)+'.csv', 'a') as csv_file:

        writer = csv.writer(csv_file)
        writer.writerow([time_start,time_end, list_values.count('Overcast clouds'),list_values.count('Broken clouds'),
            list_values.count('Scattered clouds'),list_values.count('Light rain'),list_values.count('Few clouds'),
            list_values.count('Clear Sky')])


""" VALUES FROM API """



def create_values_csv_file(directory_name, file_name):

    with open('csv'+'/values/'+str(directory_name)+'/'+str(file_name)+'.csv', 'w') as csv_file:
        
        # HEADERS
        writer = csv.writer(csv_file)
        writer.writerow(["time_start", "time_end","temperature", "precips", "clouds"])

def store_into_values(directory_name,file_name, time_start, time_end,list_temp, list_precip, list_clouds):
    
    with open('csv'+'/values/'+str(directory_name)+'/'+str(file_name)+'.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([time_start, time_end, list_temp,list_precip, list_clouds])


""" 
    STORE TAKEN IN CARE WHICH PARAMETERS APPEAR WHENEVER THE BEHAVIOR CLOUD IS SHOWIG [LIGHT RAIN, HAS HER SELF PARAMETERS SUCH
    TEMPERATURE, PRECIPITATION, AND THE CODES OF THE CLOUDS] EVERY DIRECTORY MUST BE CREATED WITH A POINT IN THE BEGGINING TO BE 
    OCCULT FROM THE ANOTHERS READERS, SUCH THE OS GONNA BE ANDROID BASED IN LINUX KERNEL, AND HER BASED ON UNIX, WE WILL MAKE 
    OCCULT THE FILES ON THE DIRECTORIES 
"""



# create the directory if this one not exists
def create_hidden_directories():

    global new_main_directory
    clouds_behavior_list = ['Overcast_clouds', 'Broken_clouds', 'Scattered_clouds', 
                            'Light_rain', 'Few_clouds', 'Clear_Sky']
    new_main_directory = '.csv/.clouds_parameters/'

    if (exists('.csv')):
        return True
    else:
        os.makedirs(new_main_directory)
        for x in clouds_behavior_list:
            os.makedirs(new_main_directory+'.'+x+'/.2017')
            os.makedirs(new_main_directory+'.'+x+'/.2018')
            os.makedirs(new_main_directory+'.'+x+'/.2019')
        return None
create_hidden_directories()
# reate_main_directories() call this method to access to global variable

# this method must be instantiated first, this one created the headers and the file name
def create_headers_into_hidden_directories(dir_name, file_name, cloud_parameter):
    # Create headers, with the corrects values
    with open(new_main_directory+'.'+cloud_parameter+'/.'+str(dir_name)+'/.'+str(file_name)+'.csv', 'w') as file:

        writer = csv.writer(file)
        writer.writerow(['time_start', 'time_end', 'cloud_description','relative_humidity','clouds' ,'precip', 'temperature', 'icon','code'])

    return


def generate_data_into_csv_files(dir_name, file_name,time_start, time_end, cloud_parameter, objects_values):

    with open(new_main_directory+'.'+cloud_parameter+'/.'+str(dir_name)+'/.'+str(file_name)+'.csv', 'a') as file_csv:
        
        writer = csv.writer(file_csv)
        writer.writerow([time_start,time_end,cloud_parameter, objects_values['relative_humidity'],objects_values['clouds'],objects_values['precipitation'],objects_values['temperature'],
        objects_values['icon'],objects_values['code'] ]) # complete the cells

    return




# ------------------------------------------------------------------------------------------------- #
# from the Create_days.py file                                                                      #
# this file return all the days to be parsed                                                        #                                  
# ------------------------------------------------------------------------------------------------- #


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

    def return_days_keys(self):

        return self.objects.keys()




# ------------------------------------------------------------------------------------------------- #
# from Interface_objects.py file                                                                    #
# Function to append new instances from the api                                                     #                                  
# ------------------------------------------------------------------------------------------------- #

def create_objects_from_clouds(api_object):

    math_process = Math_process()

    global scattered_cloud_object
    global broken_cloud_object
    global light_rain_object 
    global few_clouds_object
    global clear_sky_object
    global overcast_clouds_objects

    
    # to be stored
    scattered_cloud_object = list()
    broken_cloud_object = list()
    light_rain_object = list()
    few_clouds_object = list()
    clear_sky_object = list()
    overcast_clouds_objects = list()

    
    # loop

    for z in api_object:

        if z['weather']['description'] == "Few clouds":
            few_clouds_object.append(
                {'cloud_description':z['weather']['description'],'icon':z['weather']['icon'],
            'relative_humidity':z['rh'],'code':z['weather']['code'] ,'temperature': z['temp'],
            'clouds':z['clouds'], 'precipitation':z['precip']}
            )
            #print(few_clouds_object)
            

        elif z['weather']['description'] == "Broken clouds":
            broken_cloud_object.append(
                {'cloud_description':z['weather']['description'],'icon':z['weather']['icon'],
            'relative_humidity':z['rh'],'code':z['weather']['code'] ,'temperature': z['temp'],
            'clouds':z['clouds'], 'precipitation':z['precip']}
            )
            #print(broken_cloud_object)
            #break
            

        elif z['weather']['description'] == "Overcast clouds":
            overcast_clouds_objects.append(
                {'cloud_description':z['weather']['description'],'icon':z['weather']['icon'],
            'relative_humidity':z['rh'],'code':z['weather']['code'] ,'temperature': z['temp'],
            'clouds':z['clouds'], 'precipitation':z['precip']}
            )
            
            #break

        elif z['weather']['description'] == "Scattered clouds":
            scattered_cloud_object.append(
                {'cloud_description':z['weather']['description'],'icon':z['weather']['icon'],
            'relative_humidity':z['rh'],'code':z['weather']['code'] ,'temperature': z['temp'],
            'clouds':z['clouds'], 'precipitation':z['precip']}
            )
            #print(scattered_cloud_object)
            #break

        elif z['weather']['description'] == "Light rain":
            light_rain_object.append(
                {'cloud_description':z['weather']['description'],'icon':z['weather']['icon'],
            'relative_humidity':z['rh'],'code':z['weather']['code'] ,'temperature': z['temp'],
            'clouds':z['clouds'], 'precipitation':z['precip']}
            )
            #print(light_rain_object)
            #break

        elif z['weather']['description'] == "Clear Sky":
            clear_sky_object.append(
                {'cloud_description':z['weather']['description'],'icon':z['weather']['icon'],
            'relative_humidity':z['rh'],'code':z['weather']['code'] ,'temperature': z['temp'],
            'clouds':z['clouds'], 'precipitation':z['precip']}
            )
            #print(clear_sky_object)
            #break

        else:
            pass

    # print(overcast_clouds_objects)
    # print(len(overcast_clouds_objects))


    """ print(math_process.average(overcast_clouds_objects,'Overcast_clouds'))
    print(math_process.average(broken_cloud_object,'Broken_clouds'))
    print(math_process.average(few_clouds_object,'Few_clouds'))
    print(math_process.average(clear_sky_object,'Clear_Sky'))
    print(math_process.average(light_rain_object,'Light_rain'))
    print(math_process.average(scattered_cloud_object,'Scattered_clouds'))"""



    
    general_object = {
        'Overcast_clouds':math_process.average(overcast_clouds_objects,'Overcast_clouds'),
        'Broken_clouds':math_process.average(broken_cloud_object,'Broken_clouds'),
        'Few_clouds':math_process.average(few_clouds_object,'Few_clouds'),
        'Clear_Sky':math_process.average(clear_sky_object,'Clear_Sky'),
        'Light_rain':math_process.average(light_rain_object,'Light_rain'),
        'Scattered_clouds':math_process.average(scattered_cloud_object,'Scattered_clouds')
        }

    return general_object
    

def make_list():

    description_cloud_list = ['Overcast_clouds','Broken_clouds','Few_clouds', 'Clear_Sky','Light_rain','Scattered_clouds']

    return description_cloud_list




# ------------------------------------------------------------------------------------------------- #
# from API_values.py file                                                                           #
# Get the credentials for the scrape the inthernet                                                  #                                  
# ------------------------------------------------------------------------------------------------- #



import requests
from urllib.request import urlopen
from urllib.error import HTTPError


class API_values:

    def __init__(self, latitude, longitude):
        
        """
        @parameters latitude, longitud, time_start, time_end
        time_start and time_end must be Strings, because the algorythm it's getting 
        the time using for loops with timedelta
        """
        self.latitude = latitude
        self.longitude = longitude
        self.time_start = None
        self.time_end = None
        
        # New api key is c09b8f1a39d14a8bb9d343ccab529441
        # self.weatherbi_key = 'c96c2aa02b1b43e184580f8efe648f59'
        
        self.weatherbi_key = 'c09b8f1a39d14a8bb9d343ccab529441'
        self.url = None
        self.response_data = None


    def generate_process(self, time_start, time_end):
        self.time_start = time_start
        self.time_end = time_end
        self.url = 'https://api.weatherbit.io/v2.0/history/hourly?lat={}&lon={}&start_date={}&end_date={}&tz=local&key={}'.format(self.latitude,
            self.longitude,self.time_start,self.time_end,self.weatherbi_key)

        self.response_data  = requests.get(self.url).json()
        

    def get_api_key(self):

        return self.weatherbi_key

    def check_lat_long(self):

        return self.latitude, self.longitud

    def check_location(self):

        return self.response_data['city_name']


    # keys from the json data requested
    def get_keys(self):

        return self.response_data.keys()


    def get_average_to_clouds(self):
        pass

    
    # One param like clouds, time local
    def get_parameters(self):

        # Here the first question is "How many parameters i must to cross to get the descriptions
        # of sky are in the weather data ?"

        print(len(self.response_data['data'][0]))
        #for x in self.response_data:
        #    print(x['data'])

    def get_parameters_sky_behavior(self):

        lista_value = []

        for x in self.response_data['data']:

            if x['weather']['description'] not in lista_value :
                lista_value.append(x['weather']['description'])

        return lista_value

    
    





