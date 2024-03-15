import requests
from pprint import pprint as print

API_URL = 'https://jsonplaceholder.typicode.com/users/'

response = requests.get(API_URL)

parsed_data = response.json()
dummy_data = []

for i in range(10):
    name = {'company' : parsed_data[i]['company']['name'],
                'lat' : parsed_data[i]['address']['geo']['lat'],
                  'lng' : parsed_data[i]['address']['geo']['lng'],
                    'name' : parsed_data[i]['name']}
    if -80 < float(parsed_data[i]['address']['geo']['lat']) < 80:
        if -80< float(parsed_data[i]['address']['geo']['lng']) < 80:
            dummy_data.append(name)

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(user_list):
    censored_user_list = {}
    for user in user_list:
        if censorship(user):
            censored_user_list[user['company']] = [user['name']]
    return censored_user_list


def censorship(user_info):
    if user_info['company'] in black_list:
        print(f'{user_info["company"]} 소속의 {user_info["name"]} 은/는 등록할 수 없습니다.')
        return False
    else:
        print("이상 없습니다.")
        return True

print(create_user(dummy_data))
