
import torch
import pandas as pd

from Scrapper import Scrapper as sc

global url_name
global csv_file_name

global country_list



"""
# fifa players csv dataframe
another_url_name = "https://raw.githubusercontent.com/amanthedorkknight/fifa18-all-player-statistics/master/2019/data.csv"
fifaplayers = pd.read_csv(another_url_name)
subset = fifaplayers[['Overall','Age','International Reputation', 'Weak Foot',
       'Skill Moves']]

#print(fifaplayers)

players = torch.tensor(subset.values).float()
print(players.type())

"""



# ===========================================================
url_name = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
csv_file_name = "WHO-COVID-19-global-data.csv"

data_frame =  pd.read_csv(url_name)

#print(data_frame)

#print(data_frame.columns)

#subset = data_frame[[ ' New_cases']]
#columns = subset.columns[1:]
#countries_afected = torch.tensor(subset.values).float()


country_subset = data_frame[[' Country']]


print(type(country_subset))
#print(len(country_subset))

#print("for in country_subset")
#for x in country_subset:
#    print(x)


"""
print("Subset")
print(subset)

print("subset.values")
print(subset.values)
"""
#print(countries_afected)
