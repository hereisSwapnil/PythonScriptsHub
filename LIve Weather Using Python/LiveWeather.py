import requests
from plyer import notification

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
api_key = '6f42afa4f1275a6802a554ad79114ccd'


# Define the city and country code for the location you want to track
city = 'New York'
country_code = 'US'

# Define the URL for the OpenWeatherMap API
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}'

# Function to get weather data and send a notification
def get_weather_and_notify():
    try:
        response = requests.get(url)
        data = response.json()

        if data['cod'] != 200:
            raise Exception(data['message'])

        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']

        notification_title = f'Weather in {city}'
        notification_message = f'{weather_description.capitalize()}. Temperature: {temperature}°C'

        notification.notify(
            title=notification_title,
            message=notification_message,
            app_name='Weather App',
            timeout=10  # Notification timeout in seconds
        )

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    get_weather_and_notify()
