
import random
import time
import json

class Test:

    def __init__(self):


        # definimos los pesos iniciales,
        # claro que esto cambiará a continuación. 
        self.weigth_1 = 0.5
        self.weigth_2 = 0.5

        self.note_1 = 7
        self.note_2 = 7

        self.final_test = 0
        
        

    # doesn't return 
    def _generate_weigth(self):

        self.weigth_1 = random.uniform(0.1,0.9)
        self.weigth_2 = random.uniform(0.1,0.9)

        #return self.weigth_1, self.weigth_2
        
    # this one return final qualification
    def _calculate(self):

        self.final_test = float( float / float(self.weigth_1 + self.weigth_2) )

        return self.final_test

