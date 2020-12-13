
""" MATH PROCESS  """

from typing import final

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


    def check_covariance(self, list_values):
        # list values is the list with whole the parameters, without the NaN parameter
        # define a Sx and Sy as the covariance methods
        
        
        
        
        
        
        pass




        
