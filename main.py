import requests

def display_name(response, lookup_name):
    for item in response['results']:
        item_url=item['url']
        item_index = (item_url.split('/'))
        item_id = item_index[5]
        print(item_id, item[lookup_name])

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
    url, lookup_name, item_id = data
    response = requests.get(url).json()
    get_results(response, lookup_name)

    more = input("Would you like to see detail about a specific record? Y/n ").lower()
    if more == 'y':
        detail = input("Enter the number of the record you'd like to see: ")
        detail_url = url + "/" + detail
        response = requests.get(detail_url).json()

        for key, value in response.items():
            if key == 'films' and key != None:
                films = value
                value_list = []
                for film in films:
                    response = requests.get(film).json()
                    films = value_list.append(response['title'])
                    value = value_list

            elif key == 'species' and key != None:
                species = value
                value_list = []
                for species in species:
                    response = requests.get(species).json()
                    species = value_list.append(response['name'])
                    value = value_list

            elif key == 'vehicles' and key != None:
                vehicles = value
                value_list = []
                for vehicle in vehicles:
                    response = requests.get(vehicle).json()
                    vehicles = value_list.append(response['model'])
                    value = value_list

            elif key == 'starships' and key != None:
                starships = value
                value_list = []
                for starship in starships:
                    response = requests.get(starship).json()
                    starships = value_list.append(response['name'])
                    value = value_list

            elif key == 'characters' and key != None:
                characters = value
                value_list = []
                for character in characters:
                    response = requests.get(character).json()
                    characters = value_list.append(response['name'])
                    value = value_list

            elif key == 'planets' and key != None:
                planets = value
                value_list = []
                for planet in planets:
                    response = requests.get(planet).json()
                    planets = value_list.append(response['name'])
                    value = value_list

            elif key == 'homeworld' and key != None:
                planets = value
                value_list = []
                response = requests.get(planets).json()
                planets = value_list.append(response['name'])
                value = value_list

            print(key, ":", value, "\n")



choice = int(input("""
    Choose which to lookup:
    1: Characters
    2: Films
    3: Vehicles
    """))

choice_dict = {
1: ["http://swapi.co/api/people", 'name', 'item_id'],
2: ["http://swapi.co/api/films", 'title', 'item_id'],
3: ["http://swapi.co/api/vehicles", 'name', 'item_id']
}
make_api_call(choice_dict[choice])
