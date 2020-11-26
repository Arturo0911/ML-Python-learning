

class API_values:

    def __init__(self, latitude, longitud):
        
        
        self.latitude = latitude
        self.longitud = longitud
        self.api_key = ''
        self.url = ''

    def get_api_key(self):

        return self.api_key

    def check_lat_long(self):

        return self.latitude, self.longitud


    # keys from the json data requested
    def get_keys(self):

        pass

        