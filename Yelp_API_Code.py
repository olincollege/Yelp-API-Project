""""
Program designed to use Yelp API in order to...

"""

#importing needed libraries
import matplotlib.pyplot as plt
import requests
from API_setup import api_key

#set up of API key and required variables
# decided to put actual API key in different file for protection 

API_KEY = api_key
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'

#this endpoint allows a max of 1000 buisnesses to be returned
#when using specific search parameters
ENDPOINT = "https://api.yelp.com/v3/businesses/search"

#API_AUTH is a header that allows us to pass through our API key
#this allows us be authenticated and use the API
API_AUTH = {'Authorization': 'bearer %s' % API_KEY}



#searching buisnesses based on these parameters
PARAMETERS = {'location':'Boston',
                'limit':10,#limits to 20 searches
                'radius':1000,#radius is 
                'term':'Fast Food'}#optional term like coffee


#this line requests buisnesses fitting out parameters, from specified endpoint
#this will return as a str but in the j form
response = requests.get(url=ENDPOINT, 
                        params=PARAMETERS, 
                        headers=API_AUTH)

#need this line to convert out of j form
yelp_data = response.json()  

# making plot of data
buisness_list = []
rating_list = []
for rate in yelp_data['businesses']:
    buisness_list.append(rate['name'])
    rating_list.append(rate['rating'])

print(buisness_list)
print(rating_list)

plt.bar(buisness_list, rating_list)
plt.title('Buisness ratings')
plt.xlabel('Buisnesses')
plt.ylabel('Average ratings')
plt.show()


