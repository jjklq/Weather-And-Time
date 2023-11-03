import requests


API_KEY = '585f657f03a9c3de9401448ae4a0c188'

def get_weather(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}  # 'units' to get temperature in Celsius

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data['cod'] == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            return temperature, description
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    city = input("Enter a city name: ")
    weather_data = get_weather(city)

    if weather_data:
        temperature, description = weather_data
        print(f"Current temperature in {city}: {temperature}°C")
        print(f"Weather conditions: {description}")
    else:
        print("Unable to retrieve weather data.")
