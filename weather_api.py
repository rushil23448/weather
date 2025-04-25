import requests

def get_weather(city):
    api_key = "d6f9752e44e5b1917e1732d17de7b334"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"  # Using metric to get temperature in Celsius
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] == 200:
        return data
    else:
        return {"main": {"temp": "N/A"}, "weather": [{"description": "N/A"}]}
