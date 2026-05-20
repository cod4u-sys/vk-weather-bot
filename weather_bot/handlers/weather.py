import requests
class Weather_Actions:
    @staticmethod
    def get_coordinates(city_name: str):
        
        url = "https://geocoding-api.open-meteo.com/v1/search"
        params = {
            "name": city_name,
            "count": 5,
            "language": "ru",
            "format": "json"
        }
        response = requests.get(url, params=params)
        data = response.json()
        if data.get("results"):
            for result in data["results"]:
                if result.get("country") == "Russia":
                    return {
                        "name": result["name"],
                        "country": result["country"],
                        "latitude": result["latitude"],
                        "longitude": result["longitude"]
                        }
        return None
    
    @staticmethod
    def get_weather(latitude: float, longitude: float):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": "true",
            "temperature_unit": "celsius",
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data if "current_weather" else None
        except requests.exceptions.Timeout:
            return None
        except requests.exceptions.ConnectionError:
            return None
        except requests.exceptions.HTTPError:
            return None
        except Exception:
            return None
        
    @staticmethod
    def get_weather_emoji(weathercode, is_day):
        if weathercode == 0:
            return "☀️" if is_day else "🌙"# либо день либо ночь
        elif weathercode in [1, 2, 3]:
            return "☁️"  # облачно
        elif weathercode in [45, 48]:
            return "🌫️"  # туман
        elif weathercode in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
            return "🌧️"  # дождь
        elif weathercode in [71, 73, 75, 77]:
            return "❄️"  # снег
        elif weathercode in [95, 96, 99]:
            return "⛈️"  # гроза
        else:
            return "🌡️"  # на всякий случай