#!/usr/bin/python3

# predecir como un profesor aplicará las calificaciones. 

import random
import time

nota1 = 0
nota2 = 0




def first_test():

    global nota1
    global peso1

    nota1 = 6
    peso1 = random.uniform(0.1,0.9)

    return (nota1 * peso1)

def second_test():

    global nota2 
    global peso2

    nota2 = 7
    peso2 = random.uniform(0.1,0.9)

    return (nota2 * peso2)



counter = 0
if __name__ == '__main__':
    print('[*] Starting the training...')


    while True:
        nota_final = float(((first_test() + second_test()))/(peso1 + peso2))
        #print("la calificación final: ",nota_final)
        #print("El peso de la nota 1: ",peso1, " el peso de la nota 2:", peso2 )
        time.sleep(1)

        """
        nota_final = (first_test() + second_test())
        print(nota_final)
        break
        """
        if (nota_final > 7.0):
            print("la calificación final: ",nota_final)
            print("El peso de la nota 1: ",peso1, " el peso de la nota 2:", peso2 )
            break
        elif(nota_final < 6.0):
            

            print("la calificación final: ",nota_final)
            print("El peso de la nota 1: ",peso1, " el peso de la nota 2:", peso2 )
            counter += 1
        

    print("Las veces que se realizó un recorrido son: ", counter)