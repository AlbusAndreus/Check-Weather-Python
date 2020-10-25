import requests
from pprint import pprint

city = input('Enter your city : ')

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=6b071478ac2009a6ab81f316636fe01f&units=imperial'.format(city)

res = requests.get(url)

data = res.json()

#print(res)

#print(data)

temp = data['main']['temp']
wind_speed = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']

pressure = data['main']['pressure']
humidity = data['main']['humidity']

description = data['weather'][0]['description']

print('Temperature : {} degrees Fahrenheit'.format(temp))
print('Wind Speed : {} f/s'.format(wind_speed))
print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
print('Pressure : {} millibars'.format(pressure))
print('Humidity : {} %'.format(humidity))
print('Description : {}'.format(description))
