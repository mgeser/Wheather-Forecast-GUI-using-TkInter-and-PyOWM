import pyowm
get=pyowm.OWM('be9adf1beea879e4a05ec1aa8966aef4')
city = str(input('Enter city: '))
weather = get.weather_at_place(city)
getweather = weather.get_weather()
wind = getweather.get_wind('miles_hour')['speed']
status = getweather.get_status()
print(f'The weather now in {city} City is {status}')
print(f'The wind speed is {wind} MPH')