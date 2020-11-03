

from network.neuronal import Neuronal_networks as nn
from network.Test import Test as ts

if __name__ == '__main__':
    counter = 0

    """
    neuronal = nn(7,7,0.5,0.5)
    neuronal.read_from_storage()
    neuronal._storage(0.12,0.95)
    print(neuronal._store)
    neuronal.store_into_json_file(neuronal._store)
    #print(neuronal.feed_back(0.8,0.9))
    """
    test = ts()
    while True:
        
        # aqui empezamos a generar pesos aleatorios
        test._generate_weigth()
        #print(test._calculate())
        print(test.weigth_1)
        print(test.weigth_2)
        if ((test._calculate() > 6.5)):
            counter += 1
            print("Los pesos 1 y 2 son %s y %s "%(test.weigth_1, test.weigth_2))
            
            print(test._calculate())
            break
        else:
            counter += 1

    print("las vueltas: ", counter)