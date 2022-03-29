def Yelp_rating_search(location):
    """
    
    Args: location 

    Returns: function returns list of buisness names 
    and list of associated avg ratings
    
    """
    #import matplotlib.pyplot as plt
    import requests
    from API_setup import api_key
    
    API_KEY = api_key
    API_HOST = 'https://api.yelp.com'
    SEARCH_PATH = '/v3/businesses/search'
    ENDPOINT = "https://api.yelp.com/v3/businesses/search"
    API_AUTH = {'Authorization': 'bearer %s' % API_KEY}
    PARAMETERS = {'location':location,
                    'limit':10,#limits to 20 searches
                    'radius':1000,#radius is 
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

Yelp_rating_search('Boston')