
import torch
import pandas as pd

from Scrapper import Scrapper as sc

global url_name
global csv_file_name

url_name = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
csv_file_name = "WHO-COVID-19-global-data.csv"

data_frame =  pd.read_csv(url_name)

#print(data_frame)

#print(data_frame.columns)

subset = data_frame[[' Country', ' New_cases']]
columns = subset.columns[1:]
#countries_afected = torch.tensor(columns.values).float()







print(subset)
print(columns)
print(subset.values)

#print(countries_afected)