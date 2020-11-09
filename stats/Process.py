
import torch
import pandas as pd

from Scrapper import Scrapper as sc

"""
LINELA REGRETION MODEL: Y= β0 + β1X   
"""


class Analysis:
    
    def __init__(self):

        self.url_name = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
        self.dataframe = pd.read_csv(self.url_name)
        self.country_subset = self.dataframe[' Country']
        
        # variables to be called after the class is instantiated 
        self.country_data = ""
        self.target = ""

        

    def load(self):
        
        return self.dataframe

    def get_country_stats(self, country):

        self.country_data =  self.dataframe[self.country_subset == country]
        


    def get_new_cases(self):

        return [self.country_subset] 

    def get_mean_(self):

        self.target = torch.tensor( self.country_data[[' New_cases']].values).float()
        
        mean_data = torch.mean(self.target, dim= 0)
        std_data = torch.std(self.target, dim= 0)

        return mean_data, std_data #self.country_data[[' New_cases']]

    def get_std_(self, country):
        pass




if __name__ == "__main__":
    

    # country to test
    # country = "Ecuador"
    # First instance
    analisis = Analysis()
    analisis.get_country_stats("Ecuador")
    #print(analisis.dataframe)
    #print(analisis.get_country_stats("Ecuador"))
    #print("country_data: ", analisis.country_data)


    mean_value, std_value = analisis.get_mean_()
    print("MEAN: ",mean_value)
    print("", mean_value[0])
    #print("STD: ", std_value)
    #print(analisis.coutry_data)
    #print(analisis.load())
    #print(analisis.new_cases)

    #print()

"""

# fifa players csv dataframe
another_url_name = "https://raw.githubusercontent.com/amanthedorkknight/fifa18-all-player-statistics/master/2019/data.csv"
fifaplayers = pd.read_csv(another_url_name)
subset = fifaplayers[['Overall','Age','International Reputation', 'Weak Foot',
       'Skill Moves']]

#print(fifaplayers)

players = torch.tensor(subset.values).float()
print(players.type())





# ===========================================================
url_name = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
csv_file_name = "WHO-COVID-19-global-data.csv"

data_frame =  pd.read_csv(url_name)

#print(data_frame)

#print(data_frame.columns)

#subset = data_frame[[ ' New_cases']]
#columns = subset.columns[1:]
#countries_afected = torch.tensor(subset.values).float()


country_subset = data_frame[' Country']

print(data_frame[country_subset == "Ecuador"])

new_cases = data_frame[country_subset == "Ecuador"][[' New_cases']]
print(new_cases)



#obtener la desviación, y la media.

target = torch.tensor(new_cases.values).float()


std = torch.std(target, dim=0)
mean = torch.mean(target, dim=0)
print("El promedio: ",mean)
print("La desviación: ", std)







#print(type(data_frame[country_subset == "Ecuador"]))
#print(len(data_frame[country_subset == "Ecuador"]))




#print(data_frame[country_subset == "Ecuador"][2,3])

#print(country_subset)
#print(type(country_subset))
#print(len(country_subset))

#print("for in country_subset")


#print(data_frame[data_frame[' Country']])


print("Subset")
print(subset)

print("subset.values")
print(subset.values)
"""
#print(countries_afected)
