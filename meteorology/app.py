from Meteorology import Meteorology as mt

if __name__ == "__main__":
    
    meteorology = mt('Guayaquil')

    print(len(meteorology.res))

    for x in meteorology.res:
        print(x, x.values)
    #meteorology.read_data()
