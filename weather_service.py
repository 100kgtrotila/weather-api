import json

import requests
from cache import get_cache
from config import API_KEY

def weathercast_in_city(city_name: str):
    cache = get_cache()

    if cache:
        cache_data = cache.get(f"weather-{city_name.lower()}")
        if cache_data:
            return json.loads(cache_data)

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_name}?key={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        current = data.get("currentConditions", {})

        result = {
            "city": data.get("address"),
            "temperature": current.get("temp"),
            "true temperature": current.get("feelslike"),
            "description": current.get("conditions"),
            "source": "Visual Crossing API"
        }

        if cache:
            cache.set(f"weather-{city_name.lower()}", json.dumps(result), ex=43200)
            print(f"Saved {city_name} to cache")
        return result

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
        return None
