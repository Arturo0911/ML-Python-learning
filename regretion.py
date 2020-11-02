#!/usr/bin/python3

# predecir como un profesor aplicará las calificaciones. 


import random
import time
import csv
import json


global data


data = {}
data['feedback'] = [] # aquí van los valores que no deben ser incluídos como parte del análisis.




global nota1
global nota2 


class Machine_learning:
    
    def __init__(self):
        pass

    def _save_into_json_file(self):
        pass

    def _feed_back(self):
        pass




def first_test():

    
    global peso1

    nota1 = 7
    peso1 = random.uniform(0.1,0.9)

    return (nota1 * peso1)

def second_test():

    
    global peso2

    nota2 = 7
    peso2 = random.uniform(0.1,0.9)

    return (nota2 * peso2)

def final_test():
    
    nota_final  = float((first_test() + second_test())/(peso1 + peso2))

    return nota_final



# Método para crear un archivo .json y con este poder guardar los datos para que me sirva como parte del feedback

def created_json_file(data_to_storage):
    

    #data['feedback'].append({'peso_1': value_1, "peso_2": value_2})
    with open('data.json', 'w') as file:
        json.dump(data_to_storage, file, indent=4)

    

# read file again and after that storage again the data
def feed_back():

    with open('data.json') as file:
        reader = json.load(file)

        for x in reader['feedback']:
            data['feedback'].append({'peso_1':x['peso_1'], 'peso_2':x['peso_2']})
feed_back()
def store_(value_1, value_2):
    data['feedback'].append({'peso_1': value_1, 'peso_2': value_2})


#print(data['feedback'])



counter = 0
if __name__ == '__main__':
    print('[*] Starting the training...')


    while True:
        final_test()
        #print("la calificación final: ",nota_final)
        #print("El peso de la nota 1: ",peso1, " el peso de la nota 2:", peso2 )
        time.sleep(1)

        """
        nota_final = (first_test() + second_test())
        print(nota_final)
        break
        """
        if (final_test() > 7.0):
            #print("la calificación final: ",nota_final)
            #print("El peso de la nota 1: ",peso1, " el peso de la nota 2:", peso2 )
            break
        elif(final_test() <= 7.0):
            

            #dataset.append([peso1, peso2])
            store_(peso1, peso2)
            #created_json_file(peso1, peso2)
            #nota1 = random.randint(7,10)
            #nota2 = random.randint(7,10)
            counter += 1


    created_json_file(data)
    print("la calificación final: ",final_test())
    print("El peso de la nota 1: ",peso1, " el peso de la nota 2:", peso2 )
    print("Las veces que se realizó un recorrido son: ", counter)
    print("Los valores descartados son: ", data)