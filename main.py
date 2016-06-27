import requests

url = "http://swapi.co/api/"

response = requests.get(url).json()

choice = int(input("""
    Choose which to lookup:
    1: Characters
    2: Films
    3: Vehicles
    """))

choice_dict = {
1: "http://swapi.co/api/people",
2: "http://swapi.co/api/films",
3: "http://swapi.co/api/vehicles",
}
if choice == 1: #87 results
    url = choice_dict[choice]
    response = requests.get(url).json()
    if response['next']:
        while response['next']:
            for item in response['results']:
                print(item['name'])
            url = response['next']
            response = requests.get(url).json()
        else:
            for item in response['results']:
                print(item['name'])

if choice == 2: #7 results
    url = choice_dict[choice]
    response = requests.get(url).json()
    if response['next']:
        while response['next']:
            for item in response['results']:
                print(item['title'])
            url = response['next']
            response = requests.get(url).json()
        else:
            for item in response['results']:
                print(item['title'])
                
if choice == 3: #39 results
    url = choice_dict[choice]
    response = requests.get(url).json()
    if response['next']:
        while response['next']:
            for item in response['results']:
                print(item['name'])
            url = response['next']
            response = requests.get(url).json()
        else:
            for item in response['results']:
                print(item['name'])
