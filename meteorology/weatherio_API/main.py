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

# the arrays with the dates to be storage


class Meteorology:
    
    def __init__(self) -> None:
        pass

    def initializer(self):
        pass



api_key = 'ba199bd058f45b1a54e0d25ba95d1ca9'
weatherbi_key = 'c96c2aa02b1b43e184580f8efe648f59' # fetch api data from historic, using latitude and longitude
#latitude = '-2.335017'
latitude = '-2.3352106'
#longitude = '-80.229769'
longitude = '-80.2300508'
weatherstack_key = 'e57f178396859a0e95647a48f82b4504'
url = 'https://api.weatherbit.io/v2.0/history/hourly?lat=-2.335017&lon=-80.229769&start_date=2020-11-18&end_date=2020-11-19&tz=local&key=c96c2aa02b1b43e184580f8efe648f59'

# time to start and end
# examples we use 2016 in October
time_start = '2016-10-21'
time_end = '2016-10-22'



url_parameters = 'https://api.weatherbit.io/v2.0/history/hourly?lat={}&lon={}&start_date={}&end_date={}&tz=local&key={}'.format(latitude,longitude,time_start,time_end,weatherbi_key)
response = requests.get(url_parameters).json()
pprint(response)
#pprint(response['data'])   



# the arrays with the dates to be storage

list_years = list()
# 2016 - 2017 period
october_2016 = date(2016, 10, 1)
january_2017 = date(2017,1, 31)

delta_2017 = january_2017 - october_2016

# period 2017 - 2018
october_2017 = date(2017,10,1)
january_2018 = date(2018,1,31)

delta_2018 = january_2018 - october_2017

# period 2018 - 2019
october_2018 = date(2018,10,1)
january_2019 = date(2019,1,31)

delta_2019 = january_2019 - october_2018


for x in range(delta_2017.days + 1):
  days = october_2016 + timedelta(days=x)
  list_years.append(str(days))


for x in range(delta_2018.days + 1):
  days = october_2017 + timedelta(days=x)
  list_years.append(str(days))

for x in range(delta_2019.days +1):
  days = october_2018 + timedelta(days= x)
  list_years.append(str(days))


print(list_years)
print(len(list_years))




class Create_days:

    def __init__(self) -> None:
        pass


