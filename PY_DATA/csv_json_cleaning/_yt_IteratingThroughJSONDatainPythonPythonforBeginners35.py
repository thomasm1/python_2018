import urllib.parse
import requests

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'
 
while True:
    address = input('Address: ')
    url = main_api + urllib.parse.urlencode({'address': adress})
    print(url)
    json_data = requests.get(url).json()
    json_status = json_data['status']

    formatted_address = json_data['restuls'][0]['formatted_address']
    print()
    print(formatted_address)
