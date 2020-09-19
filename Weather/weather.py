#!/Users/benjaminculver/anaconda3/bin/python
import json, requests, datetime, sys
from colorama import Fore, Back, Style


# Getting city code given city and state
def get_city_id(city:str, state:str):
    with open("/Users/benjaminculver/PythonProjects/Deployed/Weather/city_list.json", "r") as f:
        c = city
        s = state
        cities = json.load(f)
        for city in cities:
            if city["name"].upper() == c.upper() and city["state"].upper() == s.upper():
                return city["id"]


def get_weather(city_id):
    if not city_id:
        return (f"That city name was not found\n"
                f"Pleas try again and enter another city near by"
        )

    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&units=imperial&APPID=581919d5c3cf448cd889299a469fe4ac"
    response = requests.get(url).text
    info = json.loads(response)
    
    name = info["name"]
    description = info['weather'][0]['description']
    current_temp = str(round(info["main"]["temp"])) + "°" 
    feels_like = str(round(info["main"]["feels_like"])) + "°"
    temp_min = str(round(info["main"]["temp_min"])) + "°"
    temp_max = str(round(info["main"]["temp_max"])) + "°"
    humidity = str(round(info["main"]["humidity"])) + "%"
    cloud_percentage = str(info["clouds"]["all"]) + "%"
    sunset = datetime.datetime.fromtimestamp(info["sys"]["sunset"]).strftime("%I:%M %p")

    result = (
        Fore.YELLOW + f"{name} - " + 
        Fore.GREEN + Style.BRIGHT + f"Current Temp" + Fore.LIGHTMAGENTA_EX + ": " + Fore.YELLOW + f"{current_temp}F - " +
        Fore.GREEN + Style.BRIGHT + f"Feels Like" + Fore.LIGHTMAGENTA_EX + ": " + Fore.YELLOW + f"{feels_like}F - " +
        Fore.GREEN + Style.BRIGHT + f"Min/Max" + Fore.LIGHTMAGENTA_EX + f": " + Fore.YELLOW + f"{temp_min}/{temp_max} - " +
        Fore.GREEN + Style.BRIGHT + f"Humidity" + Fore.LIGHTMAGENTA_EX + f": " + Fore.YELLOW + f"{humidity}"
        )

    return result

def main(args):
    if len(args) == 1:
        print("More arguments needed")
    elif len(args) > 1:
        city = str(args[0])
        state = str(args[1])

        city_id = get_city_id(city, state)
        result = get_weather(city_id)
        print(result)
    else:
        result = get_weather(4574324)
        print(result)

if __name__ == '__main__':
    main(sys.argv[1:])

