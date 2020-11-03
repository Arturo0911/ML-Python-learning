#!/usr/bin/python3



import random
#from main import Neuronal_networks as nn

global data





data = {}
data['feedback'] = [] # aquí van los valores que no deben ser incluídos como parte del análisis.

# =======================================================================================================================================

def test_1():
    return 7


def get_weight_1():
    
    weight_1 = random.uniform(0.1,0.9)
    return weight_1


def test_2():
    return 7

def get_weight_2():

    weight_2 = random.uniform(0.1,0.9)
    return weight_2

# =======================================================================================================================================


def first_test():

    nota1 = 7
    return (nota1 * get_weight_1())

def second_test():

    nota2 = 7
    return (nota2 * get_weight_2())

def final_test(weight1, weight2):
    
    nota_final  = float((first_test() + second_test())/(weight1 + weight2))
    return nota_final



# Método para crear un archivo .json y con este poder guardar los datos para que me sirva como parte del feedback
"""
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

def store_(value_1, value_2):
    data['feedback'].append({'peso_1': value_1, 'peso_2': value_2})


def check_data(value_1, value_2):

    with open('data.json') as file:
        reader = json.load(file)

        if (len(reader['feedback']) == 0):
            pass
        else:
            for x in reader['feedback']:

                if (value_1 <= x['peso_1'] and value_2 <= x['peso_2']):
                    #print(type(x['peso_1']))
                    #print(type(x['peso_2']))
                    pass 
                else:

                    data['feedback'].append({'peso_1': value_1, 'peso_2': value_2})
    
counter = 0
if __name__ == '__main__':
    print('[*] Starting the training...')


    while True:
        print(data['feedback'])
        if (os.path.isfile('data.json') is False):
            created_json_file(data)
        else:
            feed_back()

        if (len(data['feedback']) == 0):
            pass
        else:
            pass
            

        final_weigth_1 = get_weight_1()
        final_weigth_2 = get_weight_2()
        value_final  = final_test(final_weigth_1,final_weigth_2)
        print("valor final:  %s y los valores de los pesos 1 y 2 son %s <=> %s  "%(value_final, final_weigth_1,final_weigth_2))

        time.sleep(1)

        

        if (value_final > 7.0):
            
            print()
            #check_data(get_weight_1(),get_weight_2())
            store_(final_weigth_1, final_weigth_2)
            
            break
        elif(value_final <= 7.0):

            counter += 1


    created_json_file(data)
    print("la calificación final: ",value_final)
    #print("El peso de la nota 1: ",peso1, " el peso de la nota 2:", peso2 )
    print("Las veces que se realizó un recorrido son: ", counter)
    #print("Los valores descartados son: ", data)
"""
