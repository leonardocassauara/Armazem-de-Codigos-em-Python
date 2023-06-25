import requests

api_key = 'your_key'
latitude_x = 'your_latitude'
longitude_y = 'your_longitude'

parâmetros = {'access_key': f'{api_key}',
              'query': f'{latitude_x}, {longitude_y}'}

req = requests.get('http://api.weatherstack.com/current', parâmetros)

api_req = req.json()

print(f'{api_req["location"]["name"]} - {api_req["current"]["temperature"]}℃')