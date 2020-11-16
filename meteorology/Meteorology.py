
import torch
import numpy as np
import pandas as pd
from urllib.request import urlopen
import requests


#key = 'ba199bd058f45b1a54e0d25ba95d1ca9'

class Meteorology:

    def __init__(self, city):

        self.city = city
        self.url = 'https://api.openweathermap.org/data/2.5/weather?q='+self.city+'&appid=ba199bd058f45b1a54e0d25ba95d1ca9&units=metric'
        self.res = requests.get(self.url).json()
        
    def read_data(self):

        print(self.res)