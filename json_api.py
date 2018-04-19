from urllib.parse import urlencode as ue
import requests


with open('api_key.txt') as f:
    key = f.readline().rstrip()

url = 'https://maps.googleapis.com/maps/api/geocode/json?key={}&'.format(key)

print('### WELCOME ###\n')

while True:
    address = input(' => Type address:\n')

    quits = ('quit', 'q', 'stop', 'bye', 'byebye')
    if address.lower() in quits:
        print('\nBYE BYE :)')
        break

    full_url = url + ue({'address': address})
    print(full_url)

    json_data = requests.get(full_url).json()
    # print(type(json_data))

    json_status = json_data['status']
    # print(type(json_status))
    print('API Status: ' + json_status + '\n')

    if json_status == 'OK':
        for each in json_data['results'][0]['address_components']:
            print(each['long_name'])

        formatted_address = json_data['results'][0]['formatted_address']
        print()
        print(formatted_address + '\n')
