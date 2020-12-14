
""" MATH PROCESS  """

from os import truncate
from typing import final
import matplotlib.pyplot as plt

class Math_process:

    def Generate_average_from_list(self, list_values):
        # This one, gonna be util, whenever we want to get average 
        # from the API values

        average = "{0:.3f}".format(sum(list_values) / len(list_values))

        return average

    def Generate_parameters_from_regretion(self):        
        # β1 and β0

        pass

    def _define_average(self,number, length):

        average = "{0:.2f}".format(number/length)
        return float(average)


    def average(self, _object_, description):

        if len(_object_) > 0:

            temp_sum = 0
            clouds_sum = 0
            precip_sum = 0

            for x in _object_:

                if x['temperature'] is not None:
                    temp_sum += int(x['temperature'])

                if x['clouds'] is not None:
                    clouds_sum += int(x['clouds'])

                if x['precipitation'] is not None:
                    precip_sum += int(x['precipitation'])

            final_object = {

                'cloud_description': description,
                'icon':_object_[0]['icon'],'code': _object_[0]['code'],
                'temperature': self._define_average(temp_sum, len(_object_)),
                'clouds': self._define_average(clouds_sum, len(_object_)),
                'precipitation': self._define_average(precip_sum, len(_object_))
                }

            return final_object
        else:
            final_object = {
                # In case that the result will not do any with the value
                # 'None' then i will change None by "None" as String

                'cloud_description': description,
                'icon':None,'code': None,
                'temperature': None,
                'clouds':None,
                'precipitation': None                
                }

            return final_object


    def check_covariance(self, object_values):
        # This method will be return True o False
        # object values is the list with all the parameters, without the NaN parameter
        # define a Sx and Sy as the covariance methods
        # set the media of values
        # use values with 3 decimals
        

        """
            Structure from the list values
            object_values = {
                'x':None,
                'y':None
            }

        """

        # initializers
        
        covariance = 1
        list_x = list()
        list_y = list()

        # Set the size of list

        X_SIZE = len(object_values['x'])
        Y_SIZE = len(object_values['y'])

        average_x = float("{0:.3f}".format(sum(object_values['x'])/X_SIZE))
        average_y = float("{0:.3f}".format(sum(object_values['y'])/Y_SIZE))

        # print("two averages, %s %s"%(average_x,average_y))
        
        # X
        for x in object_values['x']:
            list_x.append(float("{0:.3f}".format(x - average_x)))

        # Y
        for y in object_values['y']:
            list_y.append(float("{0:.3f}".format(y - average_y)))


        # print(list_x)
        # print(list_y)
    
        # asssume that the values of x and y has the same length

        for i in range(X_SIZE):
            #print()
            covariance += list_x[i] * list_y[i] 

        Sxy = float("{0:.3f}".format(covariance /( X_SIZE - 1)))
        
        if Sxy > 0: # if Sxy there is direct (positive) dependence
            return Sxy
            #  print(Sxy)
        else:
            return Sxy
            #print(Sxy)
                
        return


mathematician = Math_process()


"""
objectives = {
    'x': [22,23,25,23,25,44,32],
    'y':[7,8,9,7,8,7,8]
}
"""

test_list_x = [39,43,21,64,57,43,38,75,34,52]
test_list_y = [65
,75
,52
,82
,92
,80
,73
,98
,56
,75]

objetivo = {
    'x':test_list_x,
    'y':test_list_y
}


# mathematician.check_covariance(objetivo)
print(mathematician.check_covariance(objetivo))
"""
plt.scatter(objetivo['x'], objetivo['y'])
plt.xlabel('Nota parcial')
plt.ylabel('Nota final')
plt.show()
"""

