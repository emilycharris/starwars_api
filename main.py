import requests
from urllib.parse import urlparse

def display_name(response, lookup_name):
    for item in response['results']:
        item_url=item['url']
        item_index = (item_url.split('/'))
        index = item_index[5]
        print(index, item[lookup_name])

def get_results(response, lookup_name):
    if response['next']:
        while response['next']:
            display_name(response, lookup_name)
            url = response['next']
            response = requests.get(url).json()
        else:
            display_name(response, lookup_name)
    else:
        display_name(response, lookup_name)
    
def make_api_call(data):
    url, lookup_name = data
    response = requests.get(url).json()
    get_results(response, lookup_name)

choice = int(input("""
    Choose which to lookup:
    1: Characters
    2: Films
    3: Vehicles
    """))

choice_dict = {
1: ["http://swapi.co/api/people", 'name'],
2: ["http://swapi.co/api/films", 'title'],
3: ["http://swapi.co/api/vehicles", 'name']
}

make_api_call(choice_dict[choice])
