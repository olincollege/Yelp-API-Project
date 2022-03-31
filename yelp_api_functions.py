import csv  
import requests
import matplotlib.pyplot as plt
import numpy as np
from api_setup import API_KEY


ENDPOINT = "https://api.yelp.com/v3/businesses/search"
API_AUTH = {'Authorization': 'bearer %s' % API_KEY}

def single_use_rating_search(location):
    """
    
    Enter a location and a list of 10-25 fast food buisnesses 
    and their associated ratings will be saved as a csv file
    in the directory datastorage/stored_data.csv
    location must be enetered as 'location' not location
    everytime this function is run it saves data over the original
    data in the stored_data.csv file

    Args: location 

    Returns: function returns csv file. column 1 is buisness names
    column 2 is buisnesses associated average rating
    
    """

    PARAMETERS = {'location':location,
                    'limit':10,#limits # of searches 
                    'radius':1000,
                    'term':'Fast Food'}#optional term like coffee
    
    response = requests.get(url=ENDPOINT, 
                            params=PARAMETERS, 
                            headers=API_AUTH)

    yelp_data = response.json()  

    buisness_list = []
    rating_list = []
    for rate in yelp_data['businesses']:
        buisness_list.append(rate['name'])
        rating_list.append(rate['rating'])

    print(buisness_list)
    print(rating_list)

    #saving data to csv file
    #this way saves data to data storage/stored_data
    np.savetxt('data_storage/single_stored_data.csv', [p for p in zip(buisness_list, rating_list)], delimiter=',', fmt='%s')
    





def multi_use_rating_search(locations_list):
    """

    Allows user to enter multiple locations and have data in the same csv file
    locations entered MUST be in the form of a list example below
    instead of Boston tokyo New York City proper form is
    ['Boston','Tokyo','New York City']

    Args: a list of locations in proper form

    Returns: returns a csv file titled multidata.csv
    
    
    """
    multi_buisness_list = []
    multi_rating_list = []
    file_name = "data_storage/multidata.csv"

    for location in locations_list:
 
        PARAMETERS = {'location':location,
                    'limit':10,#limits # of searches 
                    'radius':1000,
                    'term':'Fast Food'}#optional term like coffee
    
        response = requests.get(url=ENDPOINT, 
                            params=PARAMETERS, 
                            headers=API_AUTH)

        yelp_data = response.json()  

    #appends data to the buisness and ratings list
        for rate in yelp_data['businesses']:
            multi_buisness_list.append(rate['name'])
            multi_rating_list.append(rate['rating'])
    

        #appends new data to file
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            for index in range(len(multi_buisness_list)):
                writer.writerow([multi_buisness_list[index],multi_rating_list[index]])
        file.close()



  

def expanded_search(locations_list):
    """

    Allows user to enter multiple locations and have data in the same csv file
    locations entered MUST be in the form of a list example below
    instead of Boston tokyo New York City proper form is
    ['Boston','Tokyo','New York City']
    this fucntion expands what information is recieved
    so that we can can create a list of the average data by city

    Args: a list of locations in proper specified form

    Returns: returns a csv file titled expandeddata.csv 
    in the folder data_storage
    
    
    """
    city_list = []
    multi_buisness_list = []
    multi_rating_list = []
    file_name = "data_storage/expandeddata.csv"

    for location in locations_list:

        PARAMETERS = {'location':location,
                    'limit':10,#limits # of searches 
                    'radius':1000,
   
                    'term':'Fast Food'}#optional term like coffee
  
        response = requests.get(url=ENDPOINT, 
                            params=PARAMETERS, 
                            headers=API_AUTH)

        yelp_data = response.json()  

    #appends data to the buisness and ratings list
        for data in yelp_data['businesses']:
            multi_buisness_list.append(data['name'])
            multi_rating_list.append(data['rating'])
            city_list.append(data['location']['city'])

        #appends new data to file 
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            for index in range(len(multi_buisness_list)):
                writer.writerow([city_list[index],multi_buisness_list[index],multi_rating_list[index]])
        file.close()

expanded_search(['Boston','New York City','Tokyo'])







def basic_graph_data(csv_file,title,x_label, y_label):
    """

    insert data you want plotted here along with title, x label, and y label
    the csv file MUST have same number of values in columns
    csv file MUST also have only 2 columns
    all entries must be in '___' form example below
    instead of dog.csv proper form is 'dog.csv'

    Args:
        csv_file: data must have only 2 columns 
        title: input the title of the graph
        x_label: input what you want your x label to be
        y_label: input what you want you y label to be


    Returns: interprets file and graphs data according to user defined parameters

    
    """
    
    x_axis = []
    y_axis = []
    with open(csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            x_axis.append(row[0])
            y_axis.append(row[1])

    plt.bar(x_axis,y_axis)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
#basic_graph_data('data_storage/single_stored_data.csv','test','test2','test3')



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

