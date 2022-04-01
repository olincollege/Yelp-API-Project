"""
This file contains functions used in our yelp_api_functions.
Things are imported in the first section as well as defining the endpoint
and API authorization. Then the code for the functions follows and the file
ends with a few lines of code which creates a graph using the functions.

"""
import csv
import requests
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

    #allows you to specify what data you want to pull
    parameters = {'location':location,
                    'limit':50,#limits number of searches 50 max
                    'radius':1000,
                    'term':'Fast Food'}#optional term like coffee


    response = requests.get(url=ENDPOINT,
                            params=parameters,
                            headers=API_AUTH)

    yelp_data = response.json()

    business_list = []
    rating_list = []
    for rate in yelp_data['businesses']:
        business_list.append(rate['name'])
        rating_list.append(rate['rating'])

    print(business_list)
    print(rating_list)

    #saving data to csv file
    #this way saves data to data storage/stored_data
    np.savetxt('data_storage/single_stored_data.csv', \
    list(zip(business_list, rating_list)), delimiter=',', fmt='%s')





def expanded_search(locations_list):
    """

    Allows user to enter multiple locations and have data in the same csv file
    locations entered MUST be in the form of a list example below
    instead of Boston tokyo New York City proper form is
    ['Boston','Tokyo','New York City']
    this fucntion expands what information is recieved
    by including location as a column in the created csv file

    Args: a list of locations in proper specified form

    Returns: returns a csv file titled expandeddata.csv
    in the folder data_storage


    """
    #defining lists to append data to later in the function
    city_list = []
    multi_buisness_list = []
    multi_rating_list = []
    file_name = "data_storage/expandeddata.csv"

    for location in locations_list:

        parameters = {'location':location,
                    'limit':50,#limits number of searches 50 max
                    'radius':1000,

                    'term':'Fast Food'}#optional term like coffee

        response = requests.get(url=ENDPOINT,
                            params=parameters,
                            headers=API_AUTH)

        #setting the response from API as a variable
        yelp_data = response.json()

        #appends data to the buisness and ratings list
        for data in yelp_data['businesses']:
            multi_buisness_list.append(data['name'])
            multi_rating_list.append(data['rating'])
            #had to spec
            city_list.append(data['location']['city'])

        #appends new data to file
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            for index, _ in enumerate(multi_buisness_list):
                writer.writerow([city_list[index],multi_buisness_list[index], \
                multi_rating_list[index]])
        file.close()






def word_cloud(location):

    """
    Enter a location and a list of 10-50 fast food buisnesses
    will be saved as a txt file
    in the directory datastorage/stored_data.csv
    location must be enetered as 'location' not location
    everytime this function is run it saves data over the original
    data in the stored_data.csv file

    Args: location

    Returns: function returns txt file containing names of all fast
    food businesses in specified location
    """

    #allows you to specify what data you want to pull
    parameters = {'location':location,
                    'limit':50,#limits number of searches 50 max
                    'radius':1000,
                    'term':'Fast Food'}#optional term like coffee


    response = requests.get(url=ENDPOINT,
                            params=parameters,
                            headers=API_AUTH)

    yelp_data = response.json()

    names_list = []

    for rate in yelp_data['businesses']:
        names_list.append(rate['name'])

    big_name = ""
    for name in names_list:
        big_name = big_name + " " + name

    #saving as a txt file
    #this way saves data to data storage/stored_data
    with open("data_storage/cloud_txt.txt","w") as list_file:
        list_file.write(big_name)
        list_file.close()
