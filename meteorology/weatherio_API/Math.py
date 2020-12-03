


def Generate_average(list_values):
    

    first_sum = 0
    
    for x in list_values:

        first_sum += int(x)

    average = first_sum / len(list_values)
    average = "{0:.3f}".format(average)

    return average
