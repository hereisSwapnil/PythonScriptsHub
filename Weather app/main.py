import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    api_key = "49762d02afb569bad642ebb28c4a4d31"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")

    weather_data = get_weather(api_key, city)

    if weather_data:
        print(f"Weather in {city}:")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Weather data not found. Please check the city name or try again later.")

if __name__ == "__main__":
    main()
