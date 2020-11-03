
import random
import time
import csv
import json
import os
import sys


#test_1, test_2, weigth_1, weigth_2

class Neuronal_networks:   

    def __init__(self):

        print('[*] Starting the training...')
        
        #self.test_1 = test_1
        #self.test_2 = test_2
        #self.weigth_1 = weigth_1
        #self.weigth_2 = weigth_2

        self._store = {}
        self._store['neuronal'] = []

        time.sleep(2)

        print('[*] Initialize neuronal networks...')

        if (os.path.isfile('network/neuronal.json') is False):

            with open('network/neuronal.json', 'w') as f:
                json.dump(self._store, f,indent=4 )
        
        
    # 4
    def store_into_json_file(self, data_to_storage):
        
        with open('network/neuronal.json', 'w') as file:

            json.dump(data_to_storage, file, indent=4)


    # 3
    def feed_back(self, value_1, value_2):

        with open('network/neuronal.json') as read_file:
            reader = json.load(read_file)

            if (len(reader['neuronal']) > 0):

                for x in reader['neuronal']:

                    if ((value_1 >= x['peso_1'] ) and ( value_2 >= x['peso_2'])):
                        self._store['neuronal'].append({'peso_1': value_1, 'peso_2': value_2})
            else:
                pass

        return self._store
                    
    # 1
    def read_from_storage(self):

        with open('network/neuronal.json') as file_to_read:
            reader = json.load(file_to_read)
            
            print('funcion read_from_storage: ',len(reader['neuronal']))
            print(reader)
            print(reader['neuronal'])
            if (len(reader['neuronal']) > 0):

                for i in reader['neuronal']:

                    self._store['neuronal'].append({'peso_1': i['peso_1'], 'peso_2':i['peso_2']})
            else:
                pass

    # 2
    def _storage(self, parameter_1, parameter_2):

        self._store['neuronal'].append({'peso_1': parameter_1, 'peso_2': parameter_2})


    def _compare(self):
        pass