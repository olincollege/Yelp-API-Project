""""
Program designed to use Yelp API in order to identify buisnesses in
different demographical areas and comparing reviews

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

API_KEY = api_key
CLIENT_ID = client_id
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'

#this endpoint allows a max of 1000 buisnesses to be returned
#when using specific search parameters
ENDPOINT = "https://api.yelp.com/v3/businesses/search"

#API_AUTH is a header that allows us to pass through our API key
#this allows us be authenticated and use the API
API_AUTH = {'Authorization': 'bearer %s' % API_KEY}



#searching buisnesses based on these parameters
PARAMETERS = {'location':'New York',
                'limit':20,#limits to 20 searches
                'radius':1000,#radius is 
                'term':'McDonalds'}#optional term like coffee


#this line requests buisnesses fitting out parameters, from specified endpoint
#this will return as a str but in the j form
response = requests.get(url=ENDPOINT, 
                        params=PARAMETERS, 
                        headers=API_AUTH)

#need this line to convert out of j form
yelp_data = response.json()  

# printing data
print(json.dumps(yelp_data, indent = 2))


#now that data can be successfully gathered I just need to webscrape 
#for demographically different areas then input that as location
#then I use the API review search to see if different demographics 
#truly do effect reviews/how good an establishment is
