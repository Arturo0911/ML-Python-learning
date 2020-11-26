import requests
from urllib.request import urlopen
from urllib.error import HTTPError

class API_values:

    def __init__(self, latitude, longitud, time_start, time_end):
        
        """
        @parameters latitude, longitud, time_start, time_end
        """
        self.latitude = latitude
        self.longitud = longitud
        self.time_start = time_start
        self.time_end = time_end

        self.weatherbi_key = 'c96c2aa02b1b43e184580f8efe648f59'

        self.url = 'https://api.weatherbit.io/v2.0/history/hourly?lat={}&lon={}&start_date={}&end_date={}&tz=local&key={}'.format(self.latitude,
            self.longitude,self.time_start,self.time_end,self.weatherbi_key)

        self.response_data = None

    def get_api_key(self):

        return self.weatherbi_key

    def check_lat_long(self):

        return self.latitude, self.longitud


    # keys from the json data requested
    def get_keys(self):

        pass

        