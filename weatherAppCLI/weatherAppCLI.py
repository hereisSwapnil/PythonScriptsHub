import python_weather
import asyncio

async def fetch_weather(city):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(city)
    return weather

if __name__ == "__main__":
    city = input("Enter a city: ")
    loop = asyncio.get_event_loop()
    weather = loop.run_until_complete(fetch_weather(city))
  
    print(f"=== Weather in {city} ===")
    print(f"Current Temperature: {weather.current.temperature}°C")
    print("") 
    print(f"=== 3-Day Forecast ===")
    for forecast in weather.forecasts:  # Taking only first 3 days for demonstration
        print(f"\nDate: {forecast.date}")
        print(f"Temperature: {forecast.temperature}°C")
        print(f"Moon Phase: {forecast.astronomy.moon_phase}")
        print(f"Sunrise: {forecast.astronomy.sun_rise}")
        print(f"Sunset: {forecast.astronomy.sun_set}")
        
        print("Hourly Forecast:")
        for hourly in forecast.hourly:  # Taking only first 4 hours for demonstration
            print(f"  {hourly.time}: {hourly.temperature}°C, {hourly.description}")

