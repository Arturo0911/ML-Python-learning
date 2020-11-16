from Meteorology import Meteorology as mt
from pprint import pprint


if __name__ == "__main__":
    
    meteorology = mt('Guayaquil')

    print(meteorology.res)


    print("\n")

    
    pprint(meteorology.res)
    #for x, y in zip(meteorology.res, meteorology.res.values()):
    #print(x,y)
    #meteorology.read_data()



# -2.882325
# -79.009294
# http://186.42.174.241/InamhiPronostico/  => INAMHI

# api.openweathermap.org/data/2.5/weather?lat=-2.882325&lon=-79.009294&appid=ba199bd058f45b1a54e0d25ba95d1ca9