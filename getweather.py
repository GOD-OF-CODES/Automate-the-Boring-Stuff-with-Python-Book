import requests
import json
import sys

def get_weather(city, country):
    # You'll need an API key from a weather service
    API_KEY = "564e28d93bae7370b3b4e9c512f7222f"  
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Format city name for URL (replace spaces with +)
    city = city.replace(" ", "+")
    
    # Construct the URL
    url = f"{base_url}?q={city},{country}&appid={API_KEY}"
    
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python getweather.py [city] [country]")
        sys.exit(1)
        
    city = sys.argv[1]
    country = sys.argv[2]
    
    result = get_weather(city, country)
    print(result)
