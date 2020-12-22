
""" MATH PROCESS  """

from os import truncate
from typing import final



class Math_process:

    def Generate_average_from_list(self, list_values):
        # This one, gonna be util, whenever we want to get average 
        # from the API values

        average = "{0:.3f}".format(sum(list_values) / len(list_values))

        return average

    def Generate_parameters_from_regretion(self, objects_data):        
        # β1 and β0
        # the Math model of linear regretion
        # Y = β0 + β1*x
        """
        β1 =  Sumatory of products between differences the x's and y's with respectives averages/ in sumatory in
                pow difference between x and her average

        β0 = Y - β1X


        Structure of the obejcts_data = {
            
            'x': list,
            'y': list

        }
        """

        # Define list
        list_x = list()
        list_y = list()
        list_pow = list()


        x_average = self._define_average(sum(objects_data['x']), len(objects_data['x']))
        y_average = self._define_average(sum(objects_data['y']), len(objects_data['y']))


        for x in objects_data['x']:
            list_x.append(float(x  - x_average))

        for y in objects_data['y']:
            list_y.append(float(y - y_average))


        for z in objects_data['x']:
            list_pow.append(float(pow((z - x_average), 2)))


        CONST_LENGHT = len(list_x)
        total_sum = 0
        # Assuming, that both lists, has the same length

        for i in range(CONST_LENGHT):
            total_sum += (float(list_x[i] *list_y[i]))


        β1 = float("{0:.3f}".format((total_sum / (sum(list_pow)))))
        β0 = float( y_average - (β1*x_average))

        prediction_model = {

            'β1': β1,
            'β0':β0,
            'x_average':x_average,
            'y_average': y_average

        }

        return prediction_model




    def _define_average(self,number, length):

        average = "{0:.2f}".format(number/length)
        return float(average)


    def average(self, _object_, description):
        # This method insert into the csv files, all the data 

        if len(_object_) > 0:

            temp_sum = 0
            clouds_sum = 0
            precip_sum = 0
            relative_humidity_sum = 0

            for x in _object_:

                if x['temperature'] is not None:
                    temp_sum += int(x['temperature'])

                if x['clouds'] is not None:
                    clouds_sum += int(x['clouds'])

                if x['precipitation'] is not None:
                    precip_sum += int(x['precipitation'])

                if x['relative_humidity'] is not None:
                    relative_humidity_sum += int(x['relative_humidity'])

            final_object = {

                'cloud_description': description,
                'icon':_object_[0]['icon'],'relative_humidity':self._define_average(relative_humidity_sum, 
                len(_object_)) ,'code': _object_[0]['code'],
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
                'icon':None,'relative_humidity':None,'code': None,
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
        # asssume that the values of x and y has the same length
        

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

        average_x = float(sum(object_values['x'])/X_SIZE)
        average_y = float(sum(object_values['y'])/Y_SIZE)
        
        # X
        for x in object_values['x']:
            list_x.append(float(x - average_x))

        # Y
        for y in object_values['y']:
            list_y.append(float(y - average_y))



        for i in range(X_SIZE):
            
            covariance += list_x[i] * list_y[i] 

        Sxy = float("{0:.3f}".format(covariance /( X_SIZE - 1)))
        
               
        return Sxy

    def variance(self, object_values):
        # As the whole values both x and y has the same lenght, 
        # then use only a constant to set the length
        # asssume that the values of x and y has the same length


        SIZE_VALUES = len(object_values['x'])

        list_x = list()
        list_y = list()

        # define average from both values
        average_x = float((sum(object_values['x']) /SIZE_VALUES))
        average_y = float((sum(object_values['y']) /SIZE_VALUES))


        # First loops to store the difference between the value and her average
        for x in object_values['x']:

            list_x.append(float(pow(float(x - average_x),2)))

        for y in object_values['y']:

            list_y.append(float(pow(float(y - average_y),2)))
        
        # Set the Variance from both values, the format is with 3 decimals

        # print(sum(list_x)/9)
        # print(sum(list_y) /9)

        Sx = float("{0:.3f}".format(pow(float("{0:.3f}".format((sum(list_x))/(SIZE_VALUES - 1))),0.5)))
        Sy = float("{0:.3f}".format(pow(float("{0:.3f}".format((sum(list_y))/(SIZE_VALUES - 1))),0.5)))

        # Return the Variance from both values
        # Doing the testing in the test_model_weather_parameters.py
        """
            [
                {'correlation_coefficent': 0.615,
                'covariance': 33.663,
                'parameter': 'Overcast_clouds',
                'year': 2017},
                {'correlation_coefficent': 0.411,
                'covariance': 10.164,
                'parameter': 'Overcast_clouds',
                'year': 2018},
                {'correlation_coefficent': 0.176,
                'covariance': 13.742,
                'parameter': 'Overcast_clouds',
                'year': 2019},
                {'correlation_coefficent': 0.089,
                'covariance': 6.043,
                'parameter': 'Broken_clouds',
                'year': 2019},
                {'correlation_coefficent': 0.018,
                'covariance': 1.088,
                'parameter': 'Scattered_clouds',
                'year': 2019}
            ]

        """
        return Sx, Sy

        # print(Sx, Sy)

    def correlation_coefficent(self, object_values):

        Sxy = self.check_covariance(object_values)
        Sx, Sy = self.variance(object_values)

        

        return float("{0:.3f}".format((Sxy) / (Sx *Sy)))



    def set_relation_three_years(self, object_values):
        # How mucho is the difference between the actual value
        # of the parameter and the value of the average between the
        # the three years
        
        """
            principla_object = [
                {'2017':[list of values]},
                {'2018':[list of values]},
                {'2019':[list of values]}
            ]
        """

        average_2017 = float("{0:.3f}".format((sum(object_values[0]['2017']))/(len(object_values[0]['2017']))))
        average_2018 = float("{0:.3f}".format((sum(object_values[1]['2018']))/(len(object_values[1]['2018']))))
        average_2019 = float("{0:.3f}".format((sum(object_values[2]['2019']))/(len(object_values[2]['2019']))))

        """print(average_2017)
        print(average_2018)
        print(average_2019)"""
        
        final_average = float("{0:.3f}".format((average_2017 + average_2018 + average_2019)/3))

        # print(final_average)
        print("Variation from the year 2017 is: %s percent  "%"{0:.3f}".format(((final_average - average_2017)/final_average)*100))
        print("Variation from the year 2018 is: %s percent "%"{0:.3f}".format(((final_average - average_2018)/final_average)*100))
        print("Variation from the year 2019 is: %s percent "%"{0:.3f}".format(((final_average - average_2019)/final_average)*100))
        
        

