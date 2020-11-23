import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
from urllib.error import HTTPError
from pprint import pprint
import requests

api_key = 'ba199bd058f45b1a54e0d25ba95d1ca9'
weatherbi_key = 'c96c2aa02b1b43e184580f8efe648f59' # fetch api data from historic, using latitude and longitude
latitude = '-2.335017'
longitude = '-80.229769'
weatherstack_key = 'e57f178396859a0e95647a48f82b4504'
#url = 'https://api.weatherbit.io/v2.0/history/hourly?lat=-2.335017&lon=-80.229769&start_date=2020-11-18&end_date=2020-11-19&tz=local&key=c96c2aa02b1b43e184580f8efe648f59'

url_parameters = 'https://api.weatherbit.io/v2.0/history/hourly?lat={}&lon={}&start_date=2020-11-18&end_date=2020-11-19&tz=local&key={}'.format(latitude,longitude,weatherbi_key)
response = requests.get(url_parameters).json()
pprint(response)
#pprint(response['data'])