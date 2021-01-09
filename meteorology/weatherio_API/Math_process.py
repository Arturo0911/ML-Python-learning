#!/usr/bin/python3


""" MATH PROCESS  """
import math
from pprint import pprint


class Math_process:

    def Generate_average_from_list(self, list_values):
        # This one, gonna be util, whenever we want to get average
        # from the API values

        average = "{0:.3f}".format(sum(list_values) / len(list_values))

        return average

    def Generate_parameters_from_regression(self, objects_data):

        #----------------------------------------------#
        #      Generate_parameters_from_regression     #
        #           Y = β0 + β1*x                      #
        #----------------------------------------------#

        #----------------------------------------------#
        #       β1 = ⅀((x - x⁻)*(y - y⁻))              #
        #                 ⅀ ( x - x²)                  #
        #----------------------------------------------#

        #----------------------------------------------#
        #    Structure of the obejcts_data = {         #
        #            'x': list,                        #
        #            'y': list                         #
        #           }                                  #
        #----------------------------------------------#

        # Define parameters
        list_x = list()
        list_y = list()
        list_pow = list()
        MAX_X = sorted(objects_data['x'])[len(objects_data['x']) - 1]
        MIN_X = sorted(objects_data['x'])[0]

        x_average = self._define_average(
            sum(objects_data['x']), len(objects_data['x']))
        y_average = self._define_average(
            sum(objects_data['y']), len(objects_data['y']))

        for x in objects_data['x']:
            list_x.append(float(x - x_average))

        for y in objects_data['y']:
            list_y.append(float(y - y_average))

        for z in objects_data['x']:
            list_pow.append(float(pow((z - x_average), 2)))

        # Assuming, that both lists, has the same length
        CONST_LENGHT = len(list_x)
        total_sum = 0

        for i in range(CONST_LENGHT):
            total_sum += (float(list_x[i] * list_y[i]))

        β1 = float("{0:.3f}".format((total_sum / (sum(list_pow)))))
        β0 = float(y_average - (β1*x_average))

        prediction_model = {
            # is necessary set the MAX and MIN value
            # in each test, the value cannot be much more
            # of max value and lesser than min value

            'β1': float("{0:.3f}".format(β1)),
            'β0': float("{0:.3f}".format(β0)),
            'x_average': x_average,
            'y_average': y_average,
            'max_value': MAX_X,
            'min_value': MIN_X
        }

        #----------------------------------------------#
        #               Y = β0 + β1*x                  #
        #----------------------------------------------#

        return prediction_model

    # Use the math model to test the prediction

    def test_math_model(self, objects_data, x_data):
        # Where x_data is the list of values to be proveds,
        # to calculated the aprox of the value requiered
        # Every value rejected will be stored in an array,
        # after that, calculate which is the percent of wins
        # under the total of the values inserteds

        # Set the list of contain the values
        rejected_list = list()
        winner_list = list()
        cases = 1
        rejected_cases = 0

        # Assign the prediction model to the variable, to access all the stored data.
        object_model = self.Generate_parameters_from_regression(objects_data)
        y = 0
        print("[*] The prediction model is Y  = %s + X * %s  " %
              (object_model['β0'], object_model['β1']))
        """print("[*] The value to be tested in the model %s" % x_data)

        print("[*] The max %s and min %s value to be take in account" %
            (object_model['max_value'], object_model['min_value']))"""
        # print(x_data)
        # try catch statement
        try:
            # initialized ttry catch with loop insided
            for x in x_data:
                # print(x)
                if float(x) > object_model['max_value'] or float(x) < object_model['min_value']:
                    # print(bcolors.WARNING+"[x] this value cannot be used, because 
                    # it is not in the stablished range.")
                    # print("[x] CASE %s  value %s    Rejected."%(cases,x))
                    rejected_cases += 1
                    rejected_list.append(x)
                else:
                    y = float("{0:.3f}".format(
                        float(object_model['β0']) + (float(object_model['β1']) * float(x))))
                    print("[*] CASE %s  Passed  value %s." % (cases, x))
                    winner_list.append(x)
                    # print (bcolors.OKBLUE+"the prediction is: %s"%y)
                cases += 1

        except Exception as e:
            print("Error by: "+str(e))
        else:
            # print("rejected list %s and winner list %s"%(rejected_list, winner_list))
            print("\n")
            print("[*] Total cases %s, number of passed cases %s and rejected %s" %
                  (len(x_data), (len(x_data) - rejected_cases), (rejected_cases)))
            pass
        finally:

            rejecteds_percents = float((len(rejected_list) / len(x_data))*100)
            accepted_percents = float((len(winner_list) / len(x_data))*100)
            # print("rejected percents of values: "+ "{0:.3f}".format(rejecteds_percents)+" %")
            prediction = {
                'rejected_elements': len(rejected_list),
                'acepted_elements': len(winner_list),
                'rejected_percents': float("{0:.3f}".format(rejecteds_percents)),
                'acepted_percents': float("{0:.3f}".format(accepted_percents)),
            }
            print("\n")
            pprint(prediction)

    def learning_supervised(self):
        #--------------------------------------------------#
        # This method will evaluate the value of percents  #
        # of the test in the self method test_math_model   #
        #--------------------------------------------------#
        pass

    def _define_average(self, number, length):

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
                'icon': _object_[0]['icon'], 
                'relative_humidity': self._define_average(relative_humidity_sum,len(_object_)), 
                'code': _object_[0]['code'],
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
                'icon': None, 'relative_humidity': None, 'code': None,
                'temperature': None,
                'clouds': None,
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

        Sxy = float("{0:.3f}".format(covariance / (X_SIZE - 1)))

        return Sxy

    def variance(self, object_values):
        # As the whole values both x and y has the same lenght,
        # then use only a constant to set the length
        # asssume that the values of x and y has the same length

        SIZE_VALUES = len(object_values['x'])

        list_x = list()
        list_y = list()

        # define average from both values
        average_x = float((sum(object_values['x']) / SIZE_VALUES))
        average_y = float((sum(object_values['y']) / SIZE_VALUES))

        # First loops to store the difference between the value and her average
        for x in object_values['x']:

            list_x.append(float(pow(float(x - average_x), 2)))

        for y in object_values['y']:

            list_y.append(float(pow(float(y - average_y), 2)))

        # Set the Variance from both values, the format is with 3 decimals

        # print(sum(list_x)/9)
        # print(sum(list_y) /9)

        Sx = float("{0:.3f}".format(
            pow(float("{0:.3f}".format((sum(list_x))/(SIZE_VALUES - 1))), 0.5)))
        Sy = float("{0:.3f}".format(
            pow(float("{0:.3f}".format((sum(list_y))/(SIZE_VALUES - 1))), 0.5)))

        # Return the Variance from both values
        # Doing the testing in the test_model_weather_parameters.py

        return Sx, Sy

        # print(Sx, Sy)

    def correlation_coefficent(self, object_values):

        Sxy = self.check_covariance(object_values)
        Sx, Sy = self.variance(object_values)

        return float("{0:.3f}".format((Sxy) / (Sx * Sy)))

    def set_relation_three_years(self, object_values):
        # How much is the difference between the actual value
        # of the parameter and the value of the average between the
        # the three years
        """
            principla_object = [
                {'2017':[list of values]},
                {'2018':[list of values]},
                {'2019':[list of values]}
            ]
        """

        average_2017 = float("{0:.3f}".format(
            (sum(object_values[0]['2017']))/(len(object_values[0]['2017']))))
        average_2018 = float("{0:.3f}".format(
            (sum(object_values[1]['2018']))/(len(object_values[1]['2018']))))
        average_2019 = float("{0:.3f}".format(
            (sum(object_values[2]['2019']))/(len(object_values[2]['2019']))))

        """print(average_2017)
        print(average_2018)
        print(average_2019)"""

        final_average = float("{0:.3f}".format(
            (average_2017 + average_2018 + average_2019)/3))

        # print(final_average)
        print("Variation from the year 2017 is: %s percent  " %
              "{0:.3f}".format(((final_average - average_2017)/final_average)*100))
        print("Variation from the year 2018 is: %s percent " % "{0:.3f}".format(
            ((final_average - average_2018)/final_average)*100))
        print("Variation from the year 2019 is: %s percent " % "{0:.3f}".format(
            ((final_average - average_2019)/final_average)*100))
