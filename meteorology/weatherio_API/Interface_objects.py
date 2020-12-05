



#  Function to append new instances from the api


def create_objects_from_clouds(api_object):

    # to be stored
    scattered_cloud_object = list()
    broken_cloud_object = list()
    light_rain_object = list()
    few_clouds_object = list()
    clear_sky_object = list()
    overcasted_clouds_objects= list()

    for x in api_object:

        if x['weather']