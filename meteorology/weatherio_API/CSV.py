import csv
from calendar import monthrange
from datetime import date, timedelta
import json
from os import write

from requests.api import options
from main import Create_days


class Create_csv:

    def __init__(self):

        pass

    def create_file(self):

        days = Create_days()
        days.generate_appends()
        days.json_generate()
        print(days.get_objects())

        with open('neuronal.csv', 'w', newline='') as csv_file:
            
            writer = csv.writer(csv_file)
            writer.writerow(["date_reported"])

            for x in days.get_objects()[2017]:
                print(type(x))
                writer.writerow(x)


csv_files = Create_csv()
csv_files.create_file()