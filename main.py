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
    for person in response['results']:
        print(person['name'])
if choice == 2: #7 results
    url = choice_dict[choice]
    response = requests.get(url).json()
    for film in response['results']:
        print(film['title'])
if choice == 3: #39 results
    url = choice_dict[choice]
    response = requests.get(url).json()
    for film in response['results']:
        print(film['name'])
