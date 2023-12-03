import requests

api_key = "7d537ec8000f82e080fff4dbb838b92d"
city = input("Provide city name: ")


def make_apiurl(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    return url

def get_data(url):
    response = requests.get(url)
    data = response.json()
    weather = data["weather"][0]["main"]
    weather_description = data["weather"][0]["description"]
    return f"The weather in {city} is {weather}, described as {weather_description}"

print(get_data(make_apiurl(api_key, city)))
