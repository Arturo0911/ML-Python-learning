import csv
from calendar import monthrange
from datetime import date, timedelta
import json
from os import write



# Here we will storage about cloud behavior
# how have the clouds been
# ['Overcast clouds', 'Broken clouds', 'Scattered clouds', 'Light rain', 'Few clouds', 'Clear Sky']

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


""" STORE TAKEN IN CARE WHICH PARAMETERS APPEAR WHENEVER THE BEHAVIOR CLOUD IS SHOWIG [LIGHT RAIN, HAS HER SELF PARAMETERS SUCH
    TEMPERATURE, PRECIPITATION, AND THE CODES OF THE CLOUDS]
    EVERY DIRECTORY MUST BE CREATED WITH A POINT IN THE BEGGINING TO BE OCCULT FROM THE ANOTHERS READERS, SUCH THE OS GONNA BE ANDROID
    BASED IN LINUX KERNEL, AND HER BASED ON UNIX, WE WILL MAKE OCCULT THE FILES AN DIRECTORIES"""


def store_values():
    pass
