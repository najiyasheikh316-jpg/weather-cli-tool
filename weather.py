import requests

API_KEY = "7be9e795c090f8b1fff0b12d096de94c"

def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            wind = data["wind"]["speed"]

            print(f"\n📍 {city.upper()}")
            print(f"🌡️  Temperature : {temp}°C")
            print(f"🌥️  Condition   : {condition.title()}")
            print(f"💧  Humidity    : {humidity}%")
            print(f"💨  Wind Speed  : {wind} km/h")
            print("-" * 30)
            # Save to history file
            with open("history.txt", "a") as f:
                f.write(f"{city.upper()} | Temp: {temp}°C | {condition.title()} | Humidity: {humidity}% | Wind: {wind} km/h\n")
        else:
            print("❌ City not found! Please check the name.")

    except requests.exceptions.ConnectionError:
        print("❌ No internet connection! Please check your network.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out! Try again.")

while True:
    city = input("\nEnter city name (or 'quit' to exit): ")
    if city.lower() == "quit":
        print("👋 Goodbye!")
        break
    get_weather(city)