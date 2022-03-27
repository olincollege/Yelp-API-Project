""""
Program designed to use Yelp API in order to...

In the creation of this code 
https://github.com/Yelp/yelp-fusion/blob/master/fusion/python/sample.py
was used as reference for how to utilize Yelp API

"""

#importing needed libraries
import argparse
import json
import pprint
import requests
import sys
import urllib
from API_setup import api_key
from API_setup import client_id


#set up of API key and required variables
# decided to put actual API and Client key in different file for protection 

API_key = api_key
client_id = client_id
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'


#creating function to request info from yelp API
def yelp_request(host, path, API_key):
    """
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_key (str): the API key


    Returns:

    
    
    """



