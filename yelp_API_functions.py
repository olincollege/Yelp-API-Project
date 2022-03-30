import csv  
import requests
from API_setup import api_key
import matplotlib.pyplot as plt
import numpy as np

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
    
    

    API_KEY = api_key
    API_HOST = 'https://api.yelp.com'
    SEARCH_PATH = '/v3/businesses/search'
    ENDPOINT = "https://api.yelp.com/v3/businesses/search"
    API_AUTH = {'Authorization': 'bearer %s' % API_KEY}
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

    Args: a list of locations

    Returns: returns a csv file titled multidata.csv
    
    
    """
    print("Here")
    API_KEY = api_key
    API_HOST = 'https://api.yelp.com'
    SEARCH_PATH = '/v3/businesses/search'
    ENDPOINT = "https://api.yelp.com/v3/businesses/search"
    API_AUTH = {'Authorization': 'bearer %s' % API_KEY}
    multi_buisness_list = []
    multi_rating_list = []
    file_name = "data_storage/multidata.csv"

    for location in locations_list:
        print("Here")
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
    
        print("Here")
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

    Args: a list of locations

    Returns: returns a csv file titled expandeddata.csv 
    in the folder data_storage
    
    
    """
    print("Here")
    API_KEY = api_key
    API_HOST = 'https://api.yelp.com'
    SEARCH_PATH = '/v3/businesses/search'
    ENDPOINT = "https://api.yelp.com/v3/businesses/search"
    API_AUTH = {'Authorization': 'bearer %s' % API_KEY}
    city_list = []
    multi_buisness_list = []
    multi_rating_list = []
    file_name = "data_storage/expandeddata.csv"

    for location in locations_list:
        print("Here")
        PARAMETERS = {'location':location,
                    'limit':10,#limits # of searches 
                    'radius':1000,
   
                    'term':'Fast Food'}#optional term like coffee
  
        response = requests.get(url=ENDPOINT, 
                            params=PARAMETERS, 
                            headers=API_AUTH)

        yelp_data = response.json()  

    #appends data to the buisness and ratings list\
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








def graph_data(csv_file,title,X_Label, Y_Label):
    """

    insert data you want plotted here along with title, x label, and y label
    the cvs file MUST have same number of values in columns
    all entries must be in '___' form example below
    instead of dog.csv proper form is 'dog.csv'

    Args: takes in a csv file 

    Returns: interprets file and graphs data

    
    """
    
    plt.bar(csv_file)
    plt.title(title)
    plt.xlabel(X_Label)
    plt.ylabel(Y_Label)
    plt.show()

#currently fixing function





