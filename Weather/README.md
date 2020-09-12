## Requires your own OpenWeather API Key
get a free one [here](https://openweathermap.org/price)\
It may take a few hours for your Key to be active.


## Setup
Once your key is active insert it in the 'url' assignment
```python
def get_weather(city_id):
    if not city_id:
        return (f"That city name was not found\n"
                f"Pleas try again and enter another city near by"
        )

    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&units=imperial&APPID=<ENTER YOUR API KEY HERE>" 
    response = requests.get(url).text
    info = json.loads(response)
```

Replace "city_list.json" with the full path to the city_list.json file


```python
def get_city_id(city:str, state:str):
    with open("city_list.json", "r") as f:
```

## Usage
Enter a city name and two letter state code as arguments\
```./weather.py "savannah" "ga"```

The current output is a rather dull f-string
```bash
                 SAVANNAH
It is currently broken clouds and 87.82° but it feels like 89.11°
The humidity is 66%
The min/max temps today are 86° and 89.6°
The cloud cover is currently 75%
Sunset is at 07:34 PM
```

Note that while there are millions of city codes, if you live in a particularly\
small town you may have to use a city near by.

### Default city Id provided
The city Id for Charleston SC is already provided.\
This was so I could get my local weather without entering city and state.\
It also lets you run it as soon as your Key is active and see it work\
To set your own city as the default find your city Id in city_list.json\
and replace the city Id in the else block of main()
```python
 else:
        result = get_weather(4574324)
        print(result)
```
