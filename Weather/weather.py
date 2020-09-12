import json, requests, datetime, sys

def get_city_id(city:str, state:str):
    with open("city_list.json", "r") as f:
        c = city
        s = state
        cities = json.load(f)
        for city in cities:
            if city["name"].upper() == c.upper() and city["state"].upper() == s.upper():
                return city["id"]


def get_weather(city_id):
    if not city_id:
        return (f"That city name was not found\n"
                f"Please try again and enter another city near by"
        )

    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&units=imperial&APPID=<ENTER YOUR API KEY HERE>"
    response = requests.get(url).text
    info = json.loads(response)
    
    name = info["name"]
    description = info['weather'][0]['description']
    current_temp = str(info["main"]["temp"]) + "°" 
    feels_like = str(info["main"]["feels_like"]) + "°"
    temp_min = str(info["main"]["temp_min"]) + "°"
    temp_max = str(info["main"]["temp_max"]) + "°"
    humidity = str(info["main"]["humidity"]) + "%"
    cloud_percentage = str(info["clouds"]["all"]) + "%"
    sunset = datetime.datetime.fromtimestamp(info["sys"]["sunset"]).strftime("%I:%M %p")

    result = (f"{name.upper():>25}\n"
        f"It is currently {description} and {current_temp} but it feels like {feels_like}\n"
        f"The humidity is {humidity}\n"
        f"The min/max temps today are {temp_min} and {temp_max}\n"
        f"The cloud cover is currently {cloud_percentage}\n"
        f"Sunset is at {sunset}"
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
        result = get_weather(4574324) # Defaults to Charleston SC if no arguments are given
        print(result)

if __name__ == '__main__':
    main(sys.argv[1:])

