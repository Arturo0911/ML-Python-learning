import csv
from calendar import monthrange
from datetime import date, timedelta
import json
from os import write

from requests.api import options
from main import Create_days





class Create_csv:

    """
        Define parameters and values will be storage 
        in CSV file
    """

    # the file name will be contain the year of the query realizated
    def __init__(self, file_name):

        self.file_name = file_name
    

    # first method to created files
    def create_file(self):

        days = Create_days()
        days.generate_appends()
        days.json_generate()
        #print(days.get_objects())

        with open(self.file_name+'.csv', 'w') as csv_file:

            # ['Overcast clouds', 'Broken clouds', 'Scattered clouds', 'Light rain', 'Few clouds', 'Clear Sky']
            # ['Broken clouds', 'Overcast clouds', 'Scattered clouds', 'Few clouds', 'Clear Sky', 'Light rain']


            
            writer = csv.writer(csv_file)
            writer.writerow(["time_start", "time_end", 'Overcast_clouds', 'Broken_clouds', 'Scattered_clouds', 'Light_rain', 'Few_clouds', 'Clear_Sky'])

            for x in days.get_objects()[2017]:
                    
                writer.writerow([x])
            
            for x in days.get_objects()[2018]:
                
                writer.writerow([x])
            
            for x in days.get_objects()[2019]:

                writer.writerow([x])

    def create_file_with_parameters(self, time_start, time_end, ):
        pass

