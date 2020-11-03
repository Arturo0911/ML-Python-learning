

from network.neuronal import Neuronal_networks as nn


if __name__ == '__main__':

    neuronal = nn(7,7,0.5,0.5)
    neuronal.read_from_storage()
    neuronal._storage(0.12,0.95)
    print(neuronal._store)
    neuronal.store_into_json_file(neuronal._store)
    #print(neuronal.feed_back(0.8,0.9))