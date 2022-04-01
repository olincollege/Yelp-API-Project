"""
Test functions.
"""
import csv
import requests
#import matplotlib.pyplot as plt
import numpy as np
from api_setup import API_KEY

from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image

dataset = open("sampleWords.txt", "r").read()
defcreate_word_cloud(string):
   maskArray = npy.array(Image.open("cloud.png"))
   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
   cloud.generate(string)
   cloud.to_file("wordCloud.png")
dataset = dataset.lower()
create_word_cloud(dataset)



ENDPOINT = "https://api.yelp.com/v3/businesses/search"
API_AUTH = {'Authorization': 'bearer %s' % API_KEY}

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
                    'limit':50,#limits # of searches 50 max
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
word_cloud("tokyo")



