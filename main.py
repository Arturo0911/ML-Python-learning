

from network.neuronal import Neuronal_networks as nn
from network.Test import Test as ts

if __name__ == '__main__':
    counter = 0

    # Llamamos a las clases para las pruebas

    test = ts()
    neuronal = nn()
    neuronal.read_from_storage()
    
    #print(neuronal._store)
    neuronal.store_into_json_file(neuronal._store)
    #print(neuronal.feed_back(0.8,0.9))
    
    
    while True:
        
        # aqui empezamos a generar pesos aleatorios
        test._generate_weigth()
        #print(test._calculate())
        print(test.weigth_1)
        print(test.weigth_2)
        if ((test._calculate() > 6.5)):
            counter += 1
            print("Los pesos 1 y 2 son %s y %s "%(test.weigth_1, test.weigth_2))
            
            neuronal.feed_back(test.weigth_1, test.weigth_2)
            #neuronal._storage(test.weigth_1, test.weigth_2)
            neuronal.store_into_json_file(neuronal._store)
            print(test._calculate())
            break
        else:
            counter += 1

    
    print("Número de loops: ", counter)