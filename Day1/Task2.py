import requests, json

api_key = "b6527822cd9f4872af87465080b10830"
url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = "Cape Town"

fullUrl = url + "appid=" + api_key + "&q=" + city_name

response = requests.get(fullUrl)
#if cod not 401/or ==200
if(response.status_code == 200):
    data = json.loads(response.content)
    
    print("Weather data for " + city_name)
    print("Temperature: " , data['main']['temp'])
else:
    print("Error", response.status_code)
print(response.json())



