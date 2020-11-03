
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
        self.note_2 = 6

        self.final_test = 0
        
        

    # doesn't return 
    def _generate_weigth(self):

        self.weigth_1 = random.uniform(0.1,0.9)
        self.weigth_2 = random.uniform(0.1,0.9)

        #return self.weigth_1, self.weigth_2
        
    # this one return final qualification
    def _calculate(self):

        self.final_test = float((float(self.note_1 * self.weigth_1) + float(self.note_2 * self.weigth_2)) /(self.weigth_1 + self.weigth_2) )

        return self.final_test

