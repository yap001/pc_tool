import requests

def get_weather(city):
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        weather_desc = weather_data['weather'][0]['description']
        return temperature, weather_desc
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

# List of cities
cities = ['London', 'New York', 'Tokyo', 'Paris', 'Sydney']
current_city = 'Your City'

print(f"Weather for {current_city}:")
current_temp, current_desc = get_weather(current_city)
if current_temp and current_desc:
    print(f'Temperature: {current_temp}°C')
    print(f'Description: {current_desc}')
else:
    print('Failed to fetch weather data for the current city.')

print('\nWeather for major cities:')
for city in cities:
    print(f"Weather for {city}:")
    temp, desc = get_weather(city)
    if temp and desc:
        print(f'Temperature: {temp}°C')
        print(f'Description: {desc}')
    else:
        print(f'Failed to fetch weather data for {city}.')
    print()  # Add a new line for readability
