import csv  
import matplotlib.pyplot as plt
import numpy as np

def avg_finder(csv_data):
    """
    csv_data must be obtained from the expanded_search function
    csv file MUST have 3 columns the function is specifically
    built to read files with 3 columns

    Args:
        csv_data: data obtained from expanded_search function


    Returns: returns a dictionary called city_dict
    this dictionary will return in the format of
    City: associated with a list of ratings
    example: 'Boston': ['3.0', '3.5', '3.0']
            'Brooklyn': ['3.0', '3.5', '3.0']
    
    """
    city_dict = {}
    with open(csv_data, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            city = row[0]
            if city in city_dict.keys():
                city_dict[city].append(row[2])
            else:
                city_dict[city]=[row[2]]

    for i, value in city_dict.items():
        new_list = []
        for item in value:
            new_list.append(float(item))
        city_dict[i] = np.mean(new_list)
    
    return(city_dict)

        #return(ans)
    #return(city_dict) #sanity check to make sure it puts in proper form
    
city_dict = avg_finder('data_storage/expandeddata.csv')

xlabels = []
ylabels = []

for key, value in city_dict.items():
    xlabels.append(key)
    ylabels.append(value)
   
plt.bar(xlabels,ylabels)
plt.title('avg rating of cities')
plt.xlabel('cities')
plt.ylabel('avg ratings')
plt.show()
