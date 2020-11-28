import pandas as pd
import numpy as np
import torch



def read_csv_file(dir_name, file_name):


    """
    with open('csv/values/'+str(dir_name)+'/'+str(file_name)+'.csv') as target:
        

        dataframe  = pd.read_csv(target)

        print(dataframe)
    """

    # Using the path of the files, we can open and read dataframes
    dataframe  = pd.read_csv('csv/values/'+str(dir_name)+'/'+str(file_name)+'.csv')

    print(dataframe[['time_start',  'time_end']])


read_csv_file(2017, 2017)

