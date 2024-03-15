import requests
from pprint import pprint as print

API_URL = 'https://jsonplaceholder.typicode.com/users/'

response = requests.get(API_URL)

parsed_data = response.json()
dummy_data=[]
for i in range(10):
    name = {'company' : parsed_data[i]['company']['name'],
                'lat' : parsed_data[i]['address']['geo']['lat'],
                  'lng' : parsed_data[i]['address']['geo']['lng'],
                    'name' : parsed_data[i]['name']}
    if -80 < float(parsed_data[i]['address']['geo']['lat']) < 80:
        if -80< float(parsed_data[i]['address']['geo']['lng']) < 80:
            dummy_data.append(name)


print(dummy_data)