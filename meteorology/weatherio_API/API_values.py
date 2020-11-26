import requests
from urllib.request import urlopen
from urllib.error import HTTPError
import torch

class API_values:

    def __init__(self, latitude, longitude, time_start, time_end):
        
        """
        @parameters latitude, longitud, time_start, time_end
        time_start and time_end must be Strings, because the algorythm it's getting 
        the time using for loops with timedelta
        """
        self.latitude = latitude
        self.longitude = longitude
        self.time_start = time_start
        self.time_end = time_end

        self.weatherbi_key = 'c96c2aa02b1b43e184580f8efe648f59'

        self.url = 'https://api.weatherbit.io/v2.0/history/hourly?lat={}&lon={}&start_date={}&end_date={}&tz=local&key={}'.format(self.latitude,
            self.longitude,self.time_start,self.time_end,self.weatherbi_key)

        self.response_data = requests.get(self.url).json()

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
    def get_parameters(self,parameter):

        # Here the first question is "How many parameters i must to cross to get the descriptions
        # of sky are in the weather data ?"

        for x in self.response_data['data']:
            print(x[parameter])

    def get_parameters_sky_behavior(self):

        for x in self.response_data['data']:

            print(x['weather']['description'])


    
    

        